# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
import urllib.request
import datetime, ast, os, errno, time,json
import re, requests, socket

#获取目标股票代码
def get_stock_no():

    # 文件的相对路径
    #txt_filename = 'C:\\Users\\38964\Desktop\codes\stockNo_PRC_new.txt'
    txt_filename = 'C:\\Users\zanderkong\Desktop\\txt\stockNo_PRC_test.txt'

    # 打开文件
    file_obj = open(txt_filename, 'r', encoding='utf-8')

    # 逐行读取
    #stockNos = file_obj.readlines()
    stockNos = file_obj.read().splitlines()

    file_obj.close()
    return stockNos

def get_page_index(pageNum,stockNo):

    data = {
        'stock': stockNo,
        'searchkey':'',
        'category':'',
        'pageNum': pageNum,
        'pageSize': 15,
        'column': 'szse_gem',
        'tabName': 'latest',
        'sortName':'',
        'sortType':'',
        'limit':'',
        'seDate':''
        }
    params = urlencode(data)
    base = 'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/fulltext'
    url = base + '?' + params
    #print(url)

    # 设置socket层的超时时间为30秒
    socket.setdefaulttimeout(30)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

    try:
        response = requests.post(url,data=params, headers = header)
        if response.status_code == 200:
            #print("get_page_index over...")
            # 注意关闭response
            response.close()
            time.sleep(1)
            if (response.text != None):
                print(response.text)
                return response.text
            else:
                write_to_nothing(stockNo)
                return None

        write_to_nothing(stockNo)
        return None
    except ConnectionError:
        print('Connection Error occurred')
        return None

def parse_page_index(html,stockNo):
    pattern1 = re.compile(r".*年年度报告\(?(?!.*取消)(?!.*摘要)\)?")
    pattern2 = re.compile(r".*年年度报告(?!.*通)(?!.*公告)")
    basePdfUrl = "http://www.cninfo.com.cn/"

    i = 0
    #stockNo = ""

    try:
        data = json.loads(html)
        if data and 'classifiedAnnouncements' in data.keys():
            Items = data.get('classifiedAnnouncements')
            if(Items!=None):
                for items in Items:
                    for item in items:
                        announcementTitle = item.get('announcementTitle')
                        match1 = pattern1.match(announcementTitle)
                        match2 = pattern2.match(announcementTitle)
                        #print(match2)
                        if match1 and match2:

                            i += 1
                            stockNo = item.get('secCode')
                            yield basePdfUrl + item.get('adjunctUrl')
                                  #+ '\n' + item.get('announcementTitle')
            else:
                pass
                #write_to_nothing(stockNo)

    except JSONDecodeError:
        pass

    if(i==0) and (stockNo != ""):
        print('in parse_page_index')
        write_to_nothing(stockNo)


def write_to_nothing(stockNo):
    print(stockNo + 'is Empty!!!')
    # 保存到文件中
    with open('C:\\Users\zanderkong\Desktop\\txt\_Nothing_China.txt', 'r+', encoding='utf-8') as f:
        # C:\\Users\\38964\Desktop\codes\_Nothing_HK.txt
        f.write('{}\n'.format(stockNo[1:-1]))


def download_file(url,stockNo):
    file_name = url[url.find('/120') + 1:url.find('PDF') + 6]
    print(file_name)
    folder_path = 'C:\\Users\zanderkong\Desktop\PycharmPdf\PRC\\' + stockNo[1:-1] + '\\'
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    urllib.request.urlretrieve(url, folder_path + file_name)

def main(pageNum,stockNo):
    html = get_page_index(pageNum, stockNo)
    if (html != None):
        urls = parse_page_index(html,stockNo)
        if (urls != None):
            for url in urls:
                # print(url)
                download_file(url, stockNo)
        else:
            write_to_nothing(stockNo)
            pass

    else:
        write_to_nothing(stockNo)
        pass

if __name__=='__main__':
    stockNos = get_stock_no()
    for stockNo in stockNos:
        for pageNum in range(1,7):
            print(stockNo)
            main(pageNum,stockNo)