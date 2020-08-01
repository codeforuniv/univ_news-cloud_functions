import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Tokyo:
    self.collection_name = sys._getframe().f_code.co_name
    self.name = '東京大学'
    self.url = 'https://www.u-tokyo.ac.jp/focus/ja/index.html'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_="l-col-xs-12 l-col-sm-3")
        title_list = [i.find('p', class_='p-top-focus__item-text').get_text(strip=True)  for i in c_list]
        img_list = ['https://www.u-tokyo.ac.jp'+i.find('img')['src']  for i in c_list]
        date_list = [i.find('p', class_='p-top-focus__item-date').get_text(strip=True)  for i in c_list]
        url_list = [i.find('a')['href'] if 'https' in i.find('a')['href'] else 'https://www.u-tokyo.ac.jp' + i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

if __name__ == '__main__':
    instance = Tokyo()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)