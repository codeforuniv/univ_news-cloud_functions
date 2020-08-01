import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class ICU:
    collection_name = sys._getframe().f_code.co_name
    name = '国際基督教大学'
    url = 'https://www.icu.ac.jp/news/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser') 
        
        c_list = soup.find_all('div',class_="mod-newsbox")
        title_list = [i.find('h3',class_='heading').get_text(strip=True)  for i in c_list]
        img_list = ['https://www.icu.ac.jp'+i.find('img')['src']  for i in c_list]
        date_list = [i.find('div', class_='date').get_text(strip=True).replace('公開日：','')  for i in c_list]
        url_list = ['https://www.icu.ac.jp'+i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = ICU()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)