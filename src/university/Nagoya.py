import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Nagoya:
    collection_name = sys._getframe().f_code.co_name
    name = '名古屋大学'
    url = 'http://www.nagoya-u.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_="post clearfix")
        title_list = [i.find('a').get_text(strip=True) for i in c_list]
        img_list = [i.select('img')[0]['src'] if len(i.select('img'))>0 else 'http://www.nagoya-u.ac.jp/common/img/logo.gif' for i in c_list]
        date_list = [i.find('p',class_='day').get_text(strip=True) for i in c_list]
        url_list = ['http://www.nagoya-u.ac.jp/' + i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        #df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Nagoya()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)