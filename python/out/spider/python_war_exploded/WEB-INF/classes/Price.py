# -*- coding: utf-8 -*-
import bs4
import requests
import json

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

timeout = 10000

def get_Data(url):
    temp = requests.get(url, headers=header, timeout=timeout)
    temp.encoding = 'utf-8'
    soup = BeautifulSoup(temp.content,'html.parser')

    goods = soup.find('div', {'id': 'J_goodsList'})
    wrap = goods.find('ul')

    for item in wrap.find_all('li'):
        name = item.find('a', {'target': '_blank'}).get('title')
        price = item.find('div', {'class': 'p-price'}).find('i').string
        data = {'name': name, 'price': price}
        data_json = json.dumps(data, ensure_ascii = False)
        # print(name)
        # print(price.string)
        print(data_json)
        return data_json


def test(name):
    URL = address(name)
    data = a.get_Data(URL)
    return data

def address(name):
    URL_front = "https://search.jd.com/Search?keyword="
    URL_back = "&enc=utf-8&wq=&pvid="
    item_Name = name
    URL = URL_front + item_Name + URL_back
    print("将从网址：" + URL + " 抓取关于：" + item_Name + " 的数据...")
    return URL
    
print(test("1"))