#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:Ai-Link
@User:chenc
@Date:2023/2/15 9:35 
"""

import re
a = '---------_20230214_134636_PASS.log--->TestTime:140.688ms'

re_TestTime = re.findall("(TestTime:.*)", a)
b=((re_TestTime[0].split(":"))[1].split("ms"))[0]

c='---------_20230214_134642_PASS.log--->TestTime:156.2452ms'

re_TestTime = re.findall("(TestTime:.*)", a)
d=((re_TestTime[0].split(":"))[1].split("ms"))[0]

print(float(b)+float(d))
