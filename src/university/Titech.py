import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re

class Titech:
    collection_name = sys._getframe().f_code.co_name
    name = '東京工業大学'
    url = 'https://www.titech.ac.jp/news/'

    def __init__(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        c_list = soup.find_all('div',class_="boxNews01")
        title_list = [i.find('p',class_="title").get_text(strip=True)  for i in c_list]
        img_list = [
            'https://www.titech.ac.jp' + i.find('img')['data-src'] if i.find('img').has_attr('data-src')
            else 'https://www.titech.ac.jp' + i.find('img')['src']
            for i in c_list]
        date_list = [i.find('p',class_="date").get_text(strip=True) for i in c_list]
        url_list = ['https://www.titech.ac.jp' + i.find('p',class_="title").find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list,img_list,date_list,url_list],index=['name','img','date','url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(lambda x:re.sub('[年月]','/',x.replace('日',''))))
        self.df = df

#テスト用
if __name__ == '__main__':
    instance = Titech()
    print('df.shape: {}'.format(instance.df.shape))

    for key,val in instance.df.T.to_dict().items():
        print(key)
        print(val)