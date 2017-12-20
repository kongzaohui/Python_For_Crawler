# -*- coding: utf-8 -*-
import datetime


def main():
    current_time = '\'' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '\''
    print(current_time)

if __name__=='__main__':
    main()

