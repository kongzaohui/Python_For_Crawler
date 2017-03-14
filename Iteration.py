# -*- coding: utf-8 -*-
'''
Created on 2017年2月1日
@author: anton.kong
'''
tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'
jiazi = [m + n for i,m in enumerate(tiangan) for j,n in enumerate(dizhi) if (i%2==1 and j%2==1) or (i%2==0 and j%2==0) ]
print(jiazi)

tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'
jiazi = [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]

print(jiazi)
