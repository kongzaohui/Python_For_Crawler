# -*- coding: utf-8 -*-
import re
from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
import json
from json.decoder import JSONDecodeError
import urllib.request
from furl import furl


def get_page_index(pageNum):

    url = 'http://www.cninfo.com.cn/unit/list.html?'
    params ={
        'w':'672',
        't':'1,3',
        's':'/disclosure/fulltext/stocks/hkmblatest/00002.js'
    }
    _url = furl(url).add(params).url
    print(_url)

    try:
        response = requests.get(_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
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

def download_file(url):
	file_name = url[url.find('/120') + 1:url.find('PDF') + 6]
	print(file_name)
	urllib.request.urlretrieve(url, 'C:\\Users\zanderkong\Desktop\PycharmPdf\\' + file_name)

def main(pageNum):
    html = get_page_index(pageNum)
    print(html)
    '''
    for url in parse_page_index(html):
        print(url)
        download_file(url)
    '''

if __name__=='__main__':
    for pageNum in range(10):
        main(pageNum)

