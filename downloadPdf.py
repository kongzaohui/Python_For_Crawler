# -*- coding: utf-8 -*-
import urllib.request

def run_main():
    """
        主函数
    """
    url = "http://www.cninfo.com.cn/finalpage/2017-10-26/1204071413.PDF"
    file_name = url[url.find('/120') + 1:url.find('PDF')+6]
    urllib.request.urlretrieve(url, 'C:\\Users\zanderkong\Desktop\PycharmPdf\\' + file_name)
    """
    download_file(url)

def download_file(url):
    file_name = "document.pdf"

    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read()  # a `bytes` object
        out_file.write(data)
        #urllib.request.urlretrieve(download_url, file_name)
        print("Completed")
   """

if __name__ == '__main__':
    run_main()
