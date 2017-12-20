# -*- coding: utf-8 -*-
import urllib.request
import re

def run_main():
    """
        主函数
    """
    url = "http://www.cninfo.com.cn/finalpage/2017-10-26/1204071413.PDF"
    file_name = url[url.find('/120')+1:url.find('PDF')]
    print(file_name)

    str = "000001 平安银行"
    str = str[0:str.find(' ')]
    print(str)

if __name__ == '__main__':
    run_main()
