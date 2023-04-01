# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: ReadINI.py
@software: PyCharm
@time: 2022/5/14 23:29
@desc: 
"""
import configparser

class reades:

    def __init__(self):
        pass

    def config(self):
        path = r"config.ini"
        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8-sig")
        return config

    def __del__(self):
        pass

if __name__ == '__main__':
    pass