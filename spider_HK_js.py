# -*- coding: utf-8 -*-

from multiprocessing import Pool
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
import urllib.request
from furl import furl
import datetime, ast, os, errno, time
import re, requests, socket
import json

#获取目标股票代码
def get_stock_no():

    # 文件的相对路径
    txt_filename = 'C:\\Users\\38964\Desktop\Desktop\\txt\stockNo_HK_new.txt'
    #txt_filename = 'C:\\Users\zanderkong\Desktop\\txt\stockNo_HK_new.txt'

    # 打开文件
    file_obj = open(txt_filename, 'r', encoding='utf-8')

    # 逐行读取
    #stockNos = file_obj.readlines()
    stockNos = file_obj.read().splitlines()

    return stockNos

def get_page_index(stockNo):
    #print("get_page_index begin...stockNo--->")
    #print(stockNo)
    stockNo=stockNo[:5]

    if(stockNo<'08000' or stockNo=='80737'):
        url = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkmblatest/'+ stockNo +'.js?'
    else:
        url = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkgemlatest/' + stockNo + '.js?'

    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    params ={
        'ver': current_time
    }
    _url = furl(url).add(params).url
    #print(_url)

    # 设置socket层的超时时间为300秒
    #socket.setdefaulttimeout(300)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

    try:
        response = requests.get(_url, headers=header)
        if response.status_code == 200:
            #print(response.text)
            print("get_page_index over...")
            # 注意关闭response
            response.close()
            time.sleep(0.5)
            if (response.text!=None):
                return response.text
            else:
                write_to_nothing(stockNo)
                return None
    except ConnectionError:
        print('Error occurred')
        #print("get_page_index over...")
        return None

def parse_page_index(html):
    print("parse_page_index begin...")
    #html = get_page_index()
    html = html[html.find('[')+1:html.rfind(']')]
    html = ast.literal_eval(html)
    print(html)

    pattern1 = re.compile(r".*年.?报\(?(?!.*报告)\)?")
    pattern2 = re.compile(r".*年.?报(?!.*通)")
    basePdfUrl = "http://www.cninfo.com.cn/"

    i = 0
    for index,myList in enumerate(html):
        html_text = html[index][2].encode('latin1').decode('gbk')
        #print('html_text--->')
        #print(html_text)

        match1 = pattern1.match(html_text)
        match2 = pattern2.match(html_text)

        if match1 and match2:
            i+=1
            #print(html[0])
            PdfUrl = basePdfUrl + html[index][1]
            #print(PdfUrl)
            #print("parse_page_index over...")
            yield PdfUrl
            #print(html[0][2].encode('latin1').decode('gbk'))

    if(i==0):
        stockNo = html[index][0]
        write_to_nothing(stockNo)
        #return None


def write_to_nothing(stockNo):
    # 保存到文件中
    with open('C:\\Users\\38964\Desktop\codes\_Nothing_HK.txt', 'a', encoding='utf-8') as f:
        # C:\\Users\zanderkong\Desktop\\txt\_Nothing_HK.txt
        f.write('{}\n'.format(stockNo))


def download_file(url,stockNo):
    file_name = url[url.find('/120') + 1:url.find('PDF') + 6]
    #print(file_name)

    #folder_path = 'C:\\Users\zanderkong\Desktop\PycharmPdf\HK\\' + stockNo + '\\'
    folder_path = 'D:\\python-projects\HK_PDF\\' + stockNo + '\\'
    #stockNo[0:-1]
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    urllib.request.urlretrieve(url, folder_path + file_name)

def main():
    stockNos = get_stock_no()
    for stockNo in stockNos:
        html = get_page_index(stockNo)
        if (html!=None):
            PdfUrl = parse_page_index(html)
            for url in PdfUrl:
                download_file(url,stockNo)

        else:
            write_to_nothing(stockNo)
            pass

if __name__=='__main__':
    '''
    pool = Pool()
    groups = ([x * 5 for x in range(5)])
    pool.map(main(), groups)
'''
    main()