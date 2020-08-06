import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Kobe:
    collection_name = sys._getframe().f_code.co_name
    name = '神戸大学'
    url = 'https://www.kobe-u.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser') 
        
        c_list = [i.find('dl') for i in soup.find_all('section',id=['important','info','research'])]
        title_list = sum([[i.get_text(strip=True) for i in c.find_all('a')] for c in c_list],[])
        img_list = ['https://www.kobe-u.ac.jp/images/common/logo_2014.png' for i in title_list]
        date_list = sum([[i.get_text(strip=True) for i in c.find_all('dt')] for c in c_list],[])
        url_list = sum([['https://www.kobe-u.ac.jp'+i['href'] for i in c.find_all('a')] for c in c_list],[])
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Kobe()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)