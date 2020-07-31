import pandas as pd
import json
import inspect
from google.cloud import firestore
from datetime import datetime, date, timedelta

# collection_nameとscraping.pyの関数名が一致している必要がある
from scraping import University


def crawl(_event, _context):
    instances = [eval('University().' + func_name + '()') for func_name in fetch_funcnames()]
    write_university(instances)
    data = sum_data(instances)
    write_news(instances, data)
    return

def fetch_funcnames():
    '''
    scraping.py内の関数名を取得する
    '''
    return [x[0] for x in inspect.getmembers(University(),inspect.ismethod)]


def sum_data(instances):
    '''
    University().dfから指定の日付のニュースのみを抽出する
    '''
    newsdate = pd.Timestamp(date.today() - timedelta(hours=12))
    db = firestore.Client()
    data = []
    for univ in instances:
        collection_name = univ.collection_name
        df = univ.df

        collection = db.collection('university').document(collection_name).collection('news')
        docs = collection.stream()
        # 新規登録の大学でcollectionsがまだない場合、全ニュースを格納
        if len(list(docs)) == 0:
            df_tolist = df.values.tolist()

        # 既に登録されている大学の場合、前日のニュースを格納
        else:
            df_tolist = df[df.date == newsdate].values.tolist()

        data.append(df_tolist)
    return data


def write_university(instances):
    '''
    関数名に設定されている大学データをuniversityコレクションに追加する
    変更がない場合も一斉に更新をかけるためもしかしたら遅いかも
    '''
    db = firestore.Client()
    collection = db.collection('university')
    # 関数名があるものについて変更がなくても全部更新をかける
    for univ in instances:
        collection_name = univ.collection_name
        
        doc_ref = collection.document(collection_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_ref.set({
                'name': univ.name,
                'url': univ.url,
                'updatedTimestamp': firestore.SERVER_TIMESTAMP
            },merge=True)
        else:
            doc_ref.set({
                'collection_name': univ.collection_name,
                'name': univ.name,
                'url': univ.url,
                'createdTimestamp': firestore.SERVER_TIMESTAMP
            })


def write_news(instances, data):
    '''
    各ニュースをuniversity/大学名/newsサブコレクションに格納する
    '''
    db = firestore.Client()
    for univ, data_l in zip(instances, data):
        collection_name = univ.collection_name

        collection = db.collection('university').document(collection_name).collection('news')
        for d in data_l:
            docs = collection.document()
            docs.set({
                'title': d[0],
                'img': d[1],
                'date': d[2],
                'url': d[3],
                'name': d[4],
                'timestamp': firestore.SERVER_TIMESTAMP
            })
            print(collection_name,d)
