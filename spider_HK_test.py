# -*- coding: utf-8 -*-
import re
from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
import json
from json.decoder import JSONDecodeError
import urllib.request
from furl import furl
import datetime


def get_page_index(stockNo):
    print("get_page_index begin...stockNo--->")
    print(stockNo)
    stockNo=stockNo[:5]

    if(stockNo<'08000'):
        url = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkmblatest/'+ stockNo +'.js?'
    else:
        url = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkgemlatest/' + stockNo + '.js?'

    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    params ={
        'ver': current_time
    }
    _url = furl(url).add(params).url
    print(_url)

    try:
        response = requests.get(_url)
        if response.status_code == 200:
            print(response.text)
            print("get_page_index over...")
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        print("get_page_index over...")
        return None

def parse_page_index(html):
    pattern = re.compile(r".*年.?报告$")
    basePdfUrl = "http://www.cninfo.com.cn/"
    try:
        data = json.loads(html)
        if data and 'classifiedAnnouncements' in data.keys():
            for items in data.get('classifiedAnnouncements'):
                for item in items:
                    announcementTitle = item.get('announcementTitle')
                    match = pattern.match(announcementTitle)
                    if(match):
                        yield basePdfUrl + item.get('adjunctUrl')
                              #+ '\n' + item.get('announcementTitle')
    except JSONDecodeError:
        pass

def main():
    stockNo = '00784'
    html = get_page_index(stockNo)
    print(html)

if __name__=='__main__':
    main()

