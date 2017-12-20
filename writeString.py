# -*- coding: utf-8 -*-
import datetime


def main():
    stockNos=['600273','600273','600275','600276','600273','600273','600273']
    with open('C:\\Users\zanderkong\Desktop\\txt\_Nothing_China1.txt', 'r+', encoding='utf-8') as f:
        # C:\\Users\\38964\Desktop\codes\_Nothing_HK.txt
        for stockNo in stockNos:
            f.write('{}\n'.format(stockNo))
            f.truncate()
    f.close()

if __name__=='__main__':
    main()

