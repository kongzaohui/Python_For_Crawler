# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def run_main():

    html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")
    bs_obj = BeautifulSoup(html, 'lxml', from_encoding='uf-8')
    images = bs_obj.findAll("img", {"src": re.compile(r"\.\./img/gifts/img.*\.jpg")})
    for image in images:
        print(image["src"])




if __name__ == '__main__':
    run_main()


