#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:My_Proj
@software:PyCharm
@User:chenchao
@contact: 601652621@qq.com
@file:dome_01
@Date:2023/3/23 22:00 
@desc:WEB端页面
"""
from flask import Flask
from time import *


app=Flask(__name__)
@app.route('/')
def hello():
    #返回服务器的时间
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))

if __name__ == '__main__':
    app.run()