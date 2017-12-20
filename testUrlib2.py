# -*- coding: utf-8 -*-
import urllib.request

def run_main():
    """
        主函数
    """
    download_file("http://www.cninfo.com.cn/cninfo-new/disclosure/szse_sme/bulletin_detail/true/1204071413?announceTime=2017-10-26")

def download_file(download_url):
    response = urllib.request.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == '__main__':
    run_main()
