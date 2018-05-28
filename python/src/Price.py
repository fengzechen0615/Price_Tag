# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import sys

def get_Data(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    timeout = 10000
    
    temp = requests.get(url, headers=header, timeout=timeout)

    temp.encoding = 'utf-8'
    soup = BeautifulSoup(temp.content, 'html.parser')

    goods = soup.find('div', {'id': 'J_goodsList'})
    wrap = goods.find('ul')
    list = []

    for item in wrap.find_all('li'):
        name = item.find('a', {'target': '_blank'}).get('title')
        price = item.find('div', {'class': 'p-price'}).find('i').string
        data = {'name': name, 'price': price}
        data_json = json.dumps(data, ensure_ascii = False)
        # print(name)
        # print(price.string)
        list.append(data_json)
        print (data_json)


def test(name):
    URL = address(name)
    get_Data(URL)


def address(name):
    URL_front = "https://search.jd.com/Search?keyword="
    URL_back = "&enc=utf-8&wq=&pvid="
    item_Name = name
    URL = URL_front + item_Name + URL_back
    return URL

if __name__ == '__main__':
    #name = sys.argv[1]
    test("大哥")