import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class AkitaInternational:
    collection_name = sys._getframe().f_code.co_name
    name = '国際教養大学'
    url = 'https://web.aiu.ac.jp/aiutopics/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_="topic_item")
        title_list = [i.find('h5').get_text(strip=True)  for i in c_list]
        img_list = [i.find('img')['src']  for i in c_list]
        date_list = [i.find('span', class_='date').get_text(strip=True)  for i in c_list]
        url_list = [i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = AkitaInternational()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)