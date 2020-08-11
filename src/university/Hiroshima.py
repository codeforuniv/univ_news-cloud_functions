import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Hiroshima:
    collection_name = sys._getframe().f_code.co_name
    name = '広島大学'
    url = 'https://www.hiroshima-u.ac.jp/news'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = [i for ll in soup.find_all('ul',class_='newsTopicsContent') for i in ll.find_all('li')]
        title_list = [i.find('a').get_text(strip=True)[10:] for i in c_list]
        img_list = ['https://www.hiroshima-u.ac.jp/sites/all/themes/hu/images/common/h1_title.png' for i in c_list]
        date_list = [i.find('span', class_='date').get_text(strip=True) for i in c_list]
        url_list = [self.url + i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Hiroshima()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)