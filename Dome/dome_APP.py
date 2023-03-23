import time
import unittest
import serial
from selenium.webdriver.common.by import By

from appium import webdriver

class MyTests():


    def __init__(self):
        # 模组串口配置，可以根据模组具体情况修改，使用的串口名字和波特率可以在程序启动参数指定
        # 端口与波特率要根据具体模组进行修改
        g_serial_port = 'COM7'
        g_serial_baudrate = 115200
        g_serial_bytesize = serial.EIGHTBITS
        g_serial_parity = serial.PARITY_NONE
        g_serial_stopbits = serial.STOPBITS_ONE
        g_serial_timeout_s = 5

        # 连接串口
        self.serial_port = serial.Serial(g_serial_port, g_serial_baudrate, g_serial_bytesize, g_serial_parity,
                                         g_serial_stopbits,
                                         g_serial_timeout_s, rtscts=False)

        #海信APP
        desired_caps= {}
        desired_caps["noReset"] = True
        desired_caps["platformName"] ="Android"
        desired_caps["platfromVersion"] = "10"
        desired_caps["deviceName"] = "EML_AL00"
        desired_caps["appPackage"] = "com.hisense.juconnect.connectlife"
        desired_caps["appActivity"] = "com.juconnect.connect_life.MainActivity"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(120)
        el1 = self.driver.find_element(by=By.ID, value="com.hisense.juconnect.connectlife:id/user_text")
        el1.click()

    def into_data(self,data):

            #输入的指令
            data_into=data
            time.sleep(15)
            datas = self.serial_port.write((data_into + '\r\n').encode('utf8'))
            return datas

    #海信，连续开机、关机
    # def HX_operation(self,num):
    #     driver=self.driver
    #     time.sleep(2)
    #     el1 = driver.find_element_by_id("com.hisense.juconnect.connectlife:id/user_text")
    #     el1.click()
    #     time.sleep(2)
    #     el2 = driver.find_element_by_accessibility_id("yup")
    #     el2.click()
    #     time.sleep(2)
    #     for i in range(int(num)):
    #         try:
    #             time.sleep(8)
    #             el3 = driver.find_element_by_accessibility_id("电源")
    #             print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #             el3.click()
    #             print(f"第 {i} 次操作")
    #         except:
    #             time.sleep(2)

    def HX_add(self):
        driver = self.driver
        data_1 = "ATRS"
        data = "ATTS=softap"
        self.into_data(data_1)
        print("发送重置网络命令")
        self.into_data(data)
        print("发送进入配网命令")

        # 获取屏幕的size
        size = driver.get_window_size()
        # 获取屏幕宽度 width
        width = size['width']
        # 获取屏幕高度 height
        height = size['height']

        time.sleep(2)
        driver = self.driver
        el2 = driver.find_element_by_accessibility_id("从这里开始\n添加电器")
        el2.click()
        el3 = driver.find_element_by_accessibility_id("空气处理")
        el3.click()
        el4 = driver.find_element_by_accessibility_id("移动空调")
        el4.click()
        el5 = driver.find_element_by_accessibility_id("下一个")
        el5.click()
        el6 = driver.find_element_by_accessibility_id("打开WIFI设置")
        el6.click()
        time.sleep(5)
        el7 = driver.find_element(by=By.XPATH,value='//android.widget.LinearLayout[@content-desc="HIS-062c43206db2,已保存 (不可上网),WLAN 信号强度满格。"]')
        el7.click()
        el8 = driver.find_element(by=By.ID,value="android:id/button1")
        el8.click()
        el9 = driver.find_element_by_accessibility_id("向上导航")
        el9.click()
        el10 = driver.find_element_by_accessibility_id("下一步")
        el10.click()
        time.sleep(10)

        # 执行滑屏操作,向下（下拉）滑动

        for i in range(5):
            try:
                x1 = width * 0.5
                y1 = height * 0.25
                y2 = height * 0.50
                driver.swipe(x1, y2, x1, y1, 500)
                time.sleep(2)
                print(f"找寻网络，滑动第{i}次")
                el11 = driver.find_element_by_accessibility_id("MEGuest_B559")
                el11.click()
                break
            except:
                continue


        el13 = driver.find_element_by_accessibility_id("连接")
        el13.click()
        print("开始连接网络")
        time.sleep(30)
        try:
            el14 = driver.find_element(by=By.XPATH,value=
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText")
            el14.click()
            time.sleep(3)
            driver.press_keycode(48)
            driver.press_keycode(66)
            time.sleep(6)
            el15 = driver.find_element_by_accessibility_id("保存")
            el15.click()
            print("设备添加成功")
        except:
            # el19 = driver.find_element_by_accessibility_id("发生了错误。请检查您的家庭无线网络证书，然后重试。").text
            print("添加失败")
            el20 = driver.find_element_by_accessibility_id("取消")
            el20.click()
            el21 = driver.find_element(by=By.XPATH,value="(//android.widget.Button[@content-desc=\"Back\"])[1]")
            el21.click()

        print("开始删除设备")
        el16 = driver.find_element_by_accessibility_id("t")
        el16.click()

        for i in range(4):
            x1 = width * 0.5
            y1 = height * 0.25
            y2 = height * 0.50
            driver.swipe(x1, y2, x1, y1, 500)
            time.sleep(2)
            print(f"删除设备，滑动第{i}次")

        el17 = driver.find_element_by_accessibility_id("设备选项")
        el17.click()
        el18 = driver.find_element_by_accessibility_id("未配对")
        el18.click()
        el19 = driver.find_element_by_accessibility_id("取消电器配对")
        el19.click()
        print("设备已删除")


    def dome(self):
        driver = self.driver
        el7 = driver.find_element_by_accessibility_id("t")
        el7.click()
        # 获取屏幕的size
        size = driver.get_window_size()
        print(size)
        # 获取屏幕宽度 width
        width = size['width']
        print(width)
        # 获取屏幕高度 height
        height = size['height']
        print(height)
        for i in range(3):
            # 执行滑屏操作,向下（下拉）滑动
            x1 = width * 0.5
            y1 = height * 0.25
            y2 = height * 0.50
            time.sleep(3)
            print("滑动前")
            driver.swipe(x1, y2, x1, y1, 500)
            print("滑动后")
        el3 = driver.find_element_by_accessibility_id("设备选项")
        el3.click()
        el4 = driver.find_element(by=By.XPATH,value=
            "//android.view.View[@content-desc=\"一般设置\n电器自定义名称\n通知\"]/android.widget.EditText")
        el4.click()
        driver.press_keycode(48)
        # time.sleep(2)
        driver.press_keycode(66)
        # el4.send_keys("123")


if __name__ == '__main__':
    s = MyTests()
    # s.dome()
    for i in range(3):
        try:
            s.HX_add()
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"第{i+1}次添加成功,{t}")
        except:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"第{i+1}次添加失败,{t}")
            continue
