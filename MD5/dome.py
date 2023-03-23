#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:Ai-Link
@User:chenc
@Date:2023/2/17 17:24 
"""
import hashlib

# 创建MD5对象，可以直接传入要加密的数据
m = hashlib.md5('E:\Windows\Desktop\临时\AilinkStudio_M9263_MT7921_1.2.8_155.59.7z'.encode(encoding='utf-8'))

print(hashlib.md5('E:\Windows\Desktop\临时\AilinkStudio_M9263_MT7921_1.2.8_155.59.7z'.encode(encoding='utf-8')).hexdigest())
print(m)
print(m.hexdigest())  # 转化为16进制打印md5值

