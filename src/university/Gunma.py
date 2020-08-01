import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Gunma:
    collection_name = sys._getframe().f_code.co_name
    name = '群馬大学'
    url = 'https://www.gunma-u.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find('div',id="tab1").find_all('a',class_="linkbox")
        title_list = [i.find('div', class_='linkbox_title').get_text(strip=True)  for i in c_list]
        img_list = [i.find('img')['src']  for i in c_list]
        date_list = [i.find('time', class_='linkbox_time').get_text(strip=True)  for i in c_list]
        url_list = [i['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Gunma()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)