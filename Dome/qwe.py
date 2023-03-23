# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: qwe.py
@software: PyCharm
@time: 2022/6/25 21:51
@desc: 
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

wb = webdriver.Chrome(r'D:\Python\Python310\chromedriver.exe')
wb.get('https://www.gaokao.cn/school/search')
wb.maximize_window()
try:
    wb.find_element(by=By.ID,value="headsearch").click()
    wb.find_element(by=By.ID,value="headsearch").send_keys("厦门大学")
    wb.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/button').click()
    wb.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div/ul/li[1]/div[1]/p[1]/span[1]').click()
    s = wb.window_handles
    wb.switch_to.window(s[1])
    time.sleep(5)
    wb.quit()
    # wb.close()
except:
    time.sleep(5)
    wb.quit()

