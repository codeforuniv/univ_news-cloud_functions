import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import re


class University:

    def u_tokyo(self):
        self.collection_name = sys._getframe().f_code.co_name
        print(self.collection_name)
        self.name = '東京大学'
        self.url = 'https://www.u-tokyo.ac.jp/focus/ja/index.html'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find_all('div', class_="l-col-xs-12 l-col-sm-3")
        title_list = [i.find(
            'p', class_='p-top-focus__item-text').get_text(strip=True) for i in c_list]
        img_list = ['https://www.u-tokyo.ac.jp' +
                    i.find('img')['src'] for i in c_list]
        date_list = [i.find(
            'p', class_='p-top-focus__item-date').get_text(strip=True) for i in c_list]
        url_list = [i.find('a')['href'] if 'https' in i.find('a')[
            'href'] else 'https://www.u-tokyo.ac.jp' + i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(
            lambda x: re.sub('[年月]', '/', x.replace('日', ''))))
        self.df = df
        return self

    def akita_international(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '国際教養大学'
        self.url = 'https://web.aiu.ac.jp/aiutopics/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find_all('div', class_="topic_item")
        title_list = [i.find('h5').get_text(strip=True) for i in c_list]
        img_list = [i.find('img')['src'] for i in c_list]
        date_list = [i.find('span', class_='date').get_text(
            strip=True) for i in c_list]
        url_list = [i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df
        return self

    def icu(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '国際基督教大学'
        self.url = 'https://www.icu.ac.jp/news/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find_all('div', class_="mod-newsbox")
        title_list = [i.find('h3', class_='heading').get_text(
            strip=True) for i in c_list]
        img_list = ['https://www.icu.ac.jp' +
                    i.find('img')['src'] for i in c_list]
        date_list = [i.find('div', class_='date').get_text(
            strip=True).replace('公開日：', '') for i in c_list]
        url_list = ['https://www.icu.ac.jp' +
                    i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(
            lambda x: re.sub('[年月]', '/', x.replace('日', ''))))
        self.df = df
        return self

    def hokkaido(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '北海道大学'
        self.url = 'https://www.hokudai.ac.jp/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html5lib')

        c_list = soup.find('div', id="infoList",
                           class_="topicsWrap01 active").find_all('li')
        title_list = [i.find('a').get_text(strip=True) for i in c_list]
        img_list = ['https://www.hokudai.ac.jp' +
                    i.find('img')['src'] for i in c_list]
        date_list = [i.find('time').get_text(strip=True) for i in c_list]
        url_list = ['https://www.hokudai.ac.jp' +
                    i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(
            lambda x: re.sub('[年月]', '/', x.replace('日', ''))))
        self.df = df
        return self

    def tohoku(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '東北大学'
        self.url = 'https://www.tohoku.ac.jp/japanese/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find('div', id="newstab_all").find_all('li')
        title_list = [i.find('a').get_text(strip=True) for i in c_list]
        img_list = [
            'https://www.tohoku.ac.jp/japanese/share/img/logo_header.png' for i in c_list]
        date_list = [i.find('div', class_='date').get_text(
            strip=True) for i in c_list]
        url_list = ['https://www.tohoku.ac.jp' +
                    i.find('a')['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date)
        self.df = df
        return self

    def gunma(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '群馬大学'
        self.url = 'https://www.gunma-u.ac.jp/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find('div', id="tab1").find_all('a', class_="linkbox")
        title_list = [i.find('div', class_='linkbox_title').get_text(
            strip=True) for i in c_list]
        img_list = [i.find('img')['src'] for i in c_list]
        date_list = [i.find('time', class_='linkbox_time').get_text(
            strip=True) for i in c_list]
        url_list = [i['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(
            lambda x: re.sub('[年月]', '/', x.replace('日', ''))))
        self.df = df
        return self

    def kyoto(self):
        self.collection_name = sys._getframe().f_code.co_name
        self.name = '京都大学'
        self.url = 'http://www.kyoto-u.ac.jp/ja/news/'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')

        c_list = soup.find('ul', class_="news-list").find_all('a')
        title_list = [i.find('p', class_='text').get_text(
            strip=True) for i in c_list]
        img_list = [i.find('img')['src'] for i in c_list]
        date_list = [i.find('p', class_='date').get_text(strip=True)
                     for i in c_list]
        url_list = [i['href'] for i in c_list]
        df = pd.DataFrame([title_list, img_list, date_list, url_list], index=[
                          'name', 'img', 'date', 'url']).T
        df['college'] = self.name
        df.date = pd.to_datetime(df.date.map(
            lambda x: re.sub('[年月]', '/', x.replace('日', ''))))
        self.df = df
        return self
