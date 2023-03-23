#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:Ai-Link
@User:chenc
@Date:2023/2/14 15:43
用于产测log读取，获取产测时间
"""

import  re
import os

def File_Name(catalogue=''):
    filename = os.listdir(catalogue)
    file_name = str(filename)
    file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
    f = open(catalogue + "\\" + "文件list.txt", "a")
    f.write(file_name)

def File_Read(catalogue='',path=''):
    with open(path, encoding='utf-8') as file:
        content = file.read()
        re_TestTime = re.findall("(TestTime:.*)", content.rstrip())
        CertainTime =(path+"--->"+re_TestTime[1]).split("\\")[-1]+"\n\r"  #拼接内容
        b = float(((re_TestTime[1].split(":"))[1].split("ms"))[0])   #抓取时间
        return catalogue, CertainTime,b

def File_Write(catalogue='',data=''):
    f = open(catalogue + "\\" + "结果.txt", "a")
    f.write(data)

def File_main(catalogue=''):
    path=catalogue+ "\\" +"文件list.txt"
    count=0
    co=0
    with open(path, encoding='utf-8') as file:
        li=file.read().split("\n")
    for i in li:
        ss = catalogue + "\\" +i
        catalogue, CertainTime,b=File_Read(catalogue=catalogue,path=ss)
        File_Write(catalogue, CertainTime)
        count=count+b
        co+=1
    File_Write(catalogue=catalogue,data=f'总计时间：{count}，总次数：{co}，平均时间：{count / co}')



if __name__ == '__main__':
    data='F:\WIN7\LOG\PASS'
    File_Name(data)
    File_main(data)