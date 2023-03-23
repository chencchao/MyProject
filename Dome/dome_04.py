#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:Ai-Link
@User:chenc
@Date:2023/3/22 16:33 
"""

a='A6 A6 21 03 00 01 44 4F 4E 45 41 42 43 44 46 31 31 32 32 33 33 34 47'
b=a.split(' ')
c=''
for i in b:
    c=c+i
con=c[20:44]

# print(c[0:6])
# print(c[6:12])
# print(c[12:20])

print(con)