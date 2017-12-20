# -*- coding: utf-8 -*-
import re

def main():
    current_time = '关于2016年年度报告的补充公告'
    current_time2 ='2016年年度报告'
    pattern = re.compile(r".*年年度报告(?!.*公告)")

    match = pattern.match(current_time)
    match2 = pattern.match(current_time2)
    print(match2)
    if match2:
        print(current_time2)

    if match:
        print(current_time)

if __name__=='__main__':
    main()

