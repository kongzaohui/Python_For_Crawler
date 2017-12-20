# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def run_main():

    html = urllib.request.urlopen("http://www.cninfo.com.cn/information/hkinfo_n.html?hk_gem_fulltext?08001")
    bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='uf-8')
    links = bs_obj.findAll("a")
    #links = bs_obj.findAll("a", {"target":"_blank"})
    #for link in links:
    #    print(link['href'])

    # 保存到文件中
    with open('./hk08001.txt', 'w', encoding='utf-8') as f:
        for link in links:
            if link.has_attr('href'):
                f.write('{}\n'.format(link['href']))

if __name__ == '__main__':
    run_main()


