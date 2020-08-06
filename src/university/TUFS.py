import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class TUFS:
    collection_name = sys._getframe().f_code.co_name
    name = '東京外国語大学'
    url = 'http://www.tufs.ac.jp/NEWS/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser') 
        
        c_list = soup.find('dl',class_='topics_list')
        title_list = [i.get_text(strip=True) for i in c_list.find_all('a')]
        img_list = ['http://www.tufs.ac.jp/assets/img/logo_tufs.svg' for i in title_list]
        date_list = [i.get_text(strip=True) for i in c_list.find_all('time')]
        url_list = ['http://www.tufs.ac.jp' + i['href'] for i in c_list.find_all('a')]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = TUFS()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)