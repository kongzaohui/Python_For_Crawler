# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def run_main():

    # 文件的相对路径
    txt_filename = './outputLinks3.txt'

    # 打开文件
    file_obj = open(txt_filename, 'r', encoding='utf-8')

    # 逐行读取
    links = file_obj.read()

    for link in links:
        #print(link)

        html = urllib.request.urlopen(link)
        bs_obj = BeautifulSoup(html, 'lxml', from_encoding='uf-8')
        #links = bs_obj.findAll("a", {"href": re.compile(r"http://www.cninfo.com.cn/information")})
        links = bs_obj.findAll("a")


    # 保存到文件中
    with open('./outputLinks3.txt', 'w', encoding='utf-8') as f:
        for link in links:
            if link.has_attr('href'):
                f.write('{}\n'.format(link['href']))

if __name__ == '__main__':
    run_main()


