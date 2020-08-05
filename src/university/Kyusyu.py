import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Kyusyu:
    collection_name = sys._getframe().f_code.co_name
    name = '九州大学'
    url = 'https://www.kyushu-u.ac.jp/ja/news'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_='img_float_block clearfix')
        title_list = [i.find('dl').find('a').get_text(strip=True) for i in c_list]
        img_list = ['https://www.kyushu-u.ac.jp'+i.find('img')['src'] for i in c_list]
        date_list = [''.join(re.compile('[\d/]').findall(i.find('dt').get_text(strip=True).replace('.','/'))) for i in c_list]
        url_list = ['https://www.kyushu-u.ac.jp'+i.find('dd').find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Kyusyu()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)