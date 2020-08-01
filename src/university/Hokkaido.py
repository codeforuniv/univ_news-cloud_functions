import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Hokkaido:
    collection_name = sys._getframe().f_code.co_name
    name = '北海道大学'
    url = 'https://www.hokudai.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html5lib')
        
        c_list = soup.find('div',id="infoList",class_="topicsWrap01 active").find_all('li')
        title_list = [i.find('a').get_text(strip=True)  for i in c_list]
        img_list = ['https://www.hokudai.ac.jp'+i.find('img')['src']  for i in c_list]
        date_list = [i.find('time').get_text(strip=True)  for i in c_list]
        url_list = ['https://www.hokudai.ac.jp'+i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Hokkaido()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)