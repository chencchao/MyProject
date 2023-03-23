# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: Production_Token.py
@software: PyCharm
@time: 2022/6/10 14:31
@desc: 
"""
import uuid
name = "test_name"
namespace = "test_namespace"
for j in range(2):
    for i in range(500):
        c= str(uuid.uuid1()).replace("-",'')
        l =f"0moEvJJYqIhaXEJs1srf5kRpm+AAABBB{c},eIlb5JHMz8rHJ9P8dDxgBbLcdKBe9kUJTZiMW41AO9TfibzGorqZ5nu8hc6kVHQs,QJbkb5fTCUb6NKaA,0000"
        with open(f"C:\\Users\\ichenchao\\Desktop\\{j}.txt","a",encoding="utf-8") as f:
            f.write(l+"\n")

