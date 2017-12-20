# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

def run_main():

    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    # 创建对象
    bs_obj = BeautifulSoup(html_doc, 'html.parser')

    # 提取所有链接
    print('1. 提取所有链接')
    link_list = bs_obj.find_all('a')
    for link in link_list:
        print(link.name, link['href'], link.get_text())

    #提取所有段落
    print('2. 提取所有段落')
    parag_list = bs_obj.find_all('p')
    for parag in parag_list:
        print(parag.name, parag['class'], parag.get_text())

    # 提取一条链接
    print('3. 提取一条链接')
    link = bs_obj.find('a', id='link2')
    print(link.name, link['href'], link.get_text())

    # 再提取一条链接
    print('4. 再提取一条链接')
    link = bs_obj.find('a', class_='sister')
    print(link.name, link['href'], link.get_text())

if __name__ == '__main__':
    run_main()


