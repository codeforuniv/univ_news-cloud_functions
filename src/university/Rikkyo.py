import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Rikkyo:
    collection_name = sys._getframe().f_code.co_name
    name = '立教大学'
    url = 'https://www.rikkyo.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find('ul',class_='news-top-hed-list').find_all('li')
        title_list = [i.find('p',class_='news-top-hed-list-title').get_text(strip=True) for i in  c_list]
        img_list = ['https://www.rikkyo.ac.jp'+i.find('div',class_='news-top-hed-list-image')['style'].split('(')[1].split(')')[0] for i in c_list]
        date_list = [i.find('time').get_text(strip=True).split('(')[0] for i in c_list]
        url_list = ['https://www.rikkyo.ac.jp'+i.find('a')['href'] if 'http' not in i.find('a')['href']  else  i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Rikkyo()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)