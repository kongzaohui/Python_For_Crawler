# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

def run_main():
    """
        主函数
    """
    test_url = "http://www.baidu.com"

    html = urllib.request.urlopen(test_url)
    bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8');
    print("title tag: ", bs_obj.title.get_text())

if __name__ == '__main__':
    run_main()


