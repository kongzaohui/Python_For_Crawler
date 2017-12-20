# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def run_main():

    html = urllib.request.urlopen("http://www.cninfo.com.cn/cninfo-new/information/companylist")
    bs_obj = BeautifulSoup(html, 'lxml', from_encoding='uf-8')
    links = bs_obj.findAll("a", {"href": re.compile(r"http://www.cninfo.com.cn/information")})
    #links = bs_obj.findAll("a")
    for link in links:
        print(link['href'])

    # 保存到文件中
    with open('C:\\Users\\38964\Desktop\Desktop\outputLinks.txt', 'w', encoding='utf-8') as f:
        for link in links:
            if link.has_attr('href'):
                f.write('{}\n'.format(link['href']))

    with open('C:\\Users\\38964\Desktop\Desktop\outputLinkName.txt', 'w', encoding='utf-8') as f:
        for link in links:
            if link.has_attr('href'):
                f.write('{}\n'.format(link.get_text()))

if __name__ == '__main__':
    run_main()


