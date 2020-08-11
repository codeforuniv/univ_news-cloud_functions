import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Keio:
    collection_name = sys._getframe().f_code.co_name
    name = '慶應義塾大学'
    url = 'https://www.keio.ac.jp/ja/news/2020/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find_all('dl',class_='infoOuter')
        title_list = [i.find('span',class_='infoText').get_text(strip=True) for i in c_list]
        img_list = ['https://www.keio.ac.jp/ja/assets/common/images/title_01.png' for i in c_list]
        date_list = [i.find('span',class_='infoDate').get_text(strip=True) for i in c_list]
        url_list = [i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Keio()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)