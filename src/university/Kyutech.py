import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Kyutech:
    collection_name = sys._getframe().f_code.co_name
    name = '九州工業大学'
    url = 'https://www.kyutech.ac.jp/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all("li", class_="news__list-item")[6:]
        title_list = [i.find('h3',class_='news__list-ttl').get_text(strip=True) for i in  c_list]
        img_list = ['https:'+i.find('img')['src'] for i in c_list]
        date_list  = [i.find('span',class_="news__date").get_text(strip=True) for i in c_list]
        url_list = [i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Kyutech()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)