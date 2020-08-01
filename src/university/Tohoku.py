import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Tohoku:
    collection_name = sys._getframe().f_code.co_name
    name = '東北大学'
    url = 'https://www.tohoku.ac.jp/japanese/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find('div',id="newstab_all").find_all('li')
        title_list = [i.find('a').get_text(strip=True)  for i in c_list]
        img_list = ['https://www.tohoku.ac.jp/japanese/share/img/logo_header.png'  for i in c_list]
        date_list = [i.find('div',class_='date').get_text(strip=True)  for i in c_list]
        url_list = ['https://www.tohoku.ac.jp'+i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Tohoku()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)