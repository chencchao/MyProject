import os
import subprocess
import configparser
import time
import requests
from urllib import parse
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class wifi_dome:

    def __int__(self):
        pass
    def GetSSID(self,Name):
        cmd = 'netsh wlan show interfaces'
        subp = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        ret = subp.stdout.read()
        ret = str(ret,"gbk")
        index = ret.find("SSID")
        if index > 0:
            if Name in ret:
                time.sleep(2)
                print("The specified wifi is connected")
                return True
            else:
                time.sleep(2)
                print("Connected to other wifi")
                return False
        else:
            time.sleep(2)
            print("Not connected")
            return False

    def SwitchToWifi(self,Name):
        wifi_name = Name
        cmd = f"netsh wlan connect name={wifi_name}"
        os.system(cmd)

    def readini(self):
        path = r"config.ini"
        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8-sig")
        Name = config.get("WIFI", "Name")
        Type = config.get("RequestType","Type")
        return Name,Type

    def InterfaceRequest(self):
        urls = "http://10.42.251.1:8008/portal.cgi"
        urls_1="http://10.42.251.1:8008/user_quota_push_notification.cgi"
        header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                  "User-Agent": "PostmanRuntime/7.29.2",
                  "Accept": "*/*",
                  "Accept-Encoding": "gzip, deflate, br",
                  "Connection": "Close",
                  "Host":"10.42.251.1:8008",
                  }
        body_data = {
            "Token":"dulpwTu0fVdtDvbss0qyvfPS3FQF2zcQ1rhiDxnHDHIFbwXFP/udjCWEv9NCtu0tb9/Wix/MTMMVajNJkKQwZiHFVjDFwO+V5nqcHa3MCO4C+EpNXhff9pi8YVNZIEWBRmRUR+9IuMDon3TUWkCdZd4+8e3yjLQQ4g8QF6jJmLQ=",
            "username": "20376303",
            "password": "Cc123456.",
            "submit": "submit",
            "uplcyid":"2",
        }
        payload = parse.urlencode(body_data)
        re = requests.post(url=urls,json=payload,headers=header)
        re.encoding = re.apparent_encoding
        print(re.text)
        ta = {
            "username": "20376303",
            "submit": "submit",
        }
        payl =parse.urlencode(ta)
        a = requests.post(url=urls_1,json=payl,headers=header)
        a.encoding = a.apparent_encoding
        print(a.text)
        print("接口请求结束")

    #界面登录
    def faceRequest(self):
        print("")
        opt = ChromeOptions()  # 创建Chrome参数对象
        opt.headless = True    # 把Chrome设置成可视化无界面模式
        browser = Chrome(options=opt)   # 创建Chrome无界面对象
        browser.get('http://10.42.251.1:8008/portal/local/index.html?uplcyid=2&weburl=')
        time.sleep(2)
        browser.maximize_window()
        browser.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys("20376303")
        time.sleep(1)
        browser.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys("Cc123456.")
        time.sleep(1)
        browser.find_element(by=By.XPATH,value='//*[@id="local_index"]/div/div[3]/div/div[3]/button').click()
        time.sleep(1)
        browser.close()
        print("无界面请求结束")

    def main(self):
        print("start---------")
        Name,Type = self.readini()
        a = 0
        while True:
            a +=1
            if self.GetSSID(Name) == True:
                if Type == "1":
                    print("开始无界面请求")
                    self.faceRequest()
                elif Type == "2":
                    print("开始接口请求")
                    self.InterfaceRequest()
                break
            else:
                self.SwitchToWifi(Name)
                time.sleep(10)
                # if a == 5:
                #     os.system("shutdown -r")
        print("end---------")

if __name__ == '__main__':
    s = wifi_dome()
    s.main()
