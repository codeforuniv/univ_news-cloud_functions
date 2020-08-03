import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Osaka:
    collection_name = sys._getframe().f_code.co_name
    name = '大阪大学'
    url = 'https://www.osaka-u.ac.jp/ja/news/topics'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_="post clearfix")
        title_list = [i.find('dd').find('a').get_text(strip=True) for i in c_list]
        img_list = [i.find('div',class_='photo').select('img')[0]['src'] if len(i.find('div',class_='photo').select('img')) > 0 else 'https://www.osaka-u.ac.jp/add_201507_logo.png' for i in c_list]
        date_list = [i.find('span',class_='date').get_text(strip=True).split('(')[0] for i in c_list]
        url_list = [i.find('dd').find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Osaka()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)