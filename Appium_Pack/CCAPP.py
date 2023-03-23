import time
from appium import webdriver

class TApp():

    def __init__(self,data):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", data)  # 连接Appium
        self.driver.implicitly_wait(120)

    #模拟键盘输入
    def KeyInput(self,code):
        driver = self.driver
        driver.press_keycode(code)

    #手机滑动动作,向下滑动
    def DownSlide(self):
        driver = self.driver
        # 获取屏幕的size
        size = driver.get_window_size()
        # 获取屏幕宽度 width
        width = size['width']
        # 获取屏幕高度 height
        height = size['height']
        print(width,height)
        # 执行滑屏操作,向下（下拉）滑动
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.50
        time.sleep(3)
        driver.swipe(x1, y2, x1, y1, 500)


    #手机滑动动作,向上滑动
    def UpSlide(self):
        driver = self.driver
        # 获取屏幕的size
        size = driver.get_window_size()
        # 获取屏幕宽度 width
        width = size['width']
        # 获取屏幕高度 height
        height = size['height']
        # 执行滑屏操作,向下（下拉）滑动
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.50
        time.sleep(3)
        driver.swipe(x1, y1, x1, y2, 500)

    # def __del__(self):
    #     self.driver.close()


if __name__ == '__main__':
    pass


