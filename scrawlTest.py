# -*- coding: utf-8 -*-
import urllib.request
import http.cookiejar

def run_main():
    """
        主函数
    """
    test_url = "http://www.google.com"

    # 通过cookie访问

    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(test_url)
    print(response.getcode())  # 200 表示访问成功
    print(response.read())
    print(cookie_jar)

if __name__ == '__main__':
    run_main()
