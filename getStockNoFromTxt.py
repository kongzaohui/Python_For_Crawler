# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def run_main():

    # 文件的相对路径
    txt_filename = 'C:\\Users\\38964\Desktop\Desktop\outputLinkName.txt'

    # 打开文件
    file_obj = open(txt_filename, 'r', encoding='utf-8')

    # 逐行读取
    links = file_obj.readlines()

    # 保存到文件中
    with open('C:\\Users\\38964\Desktop\Desktop\outputStockNo.txt', 'w', encoding='utf-8') as f:
        for link in links:
            #print(link)
            link = link[0:link.find(' ')]
            link = '\'' + link + '\''
            print(link)
            f.write('{}\n'.format(link))

if __name__ == '__main__':
    run_main()


