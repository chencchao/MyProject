import time
from selenium.webdriver.common.by import By
from appium import webdriver

class Thua():
    """
          获取appPackage和appActivity ：           adb logcat | findStr -i displayed

    """

    # 智慧生活APP 0826
    date_huawei = {"noReset": True,
                   "platformName": "Android",
                   "platfromVersion": "10",
                   "deviceName": "EML_AL00",
                   "appPackage": "com.huawei.smarthome",
                   "appActivity": "com.huawei.smarthome.login.LauncherActivity"
                   }

    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.date_huawei)  # 连接Appium
        self.driver.implicitly_wait(120)


    def socket_operation_01(self):
        driver = self.driver
        el1 = driver.find_element(by=By.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView")
        el2 = driver.find_element(by=By.XPATH,
                                  value=f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView")
        el3 = driver.find_element(by=By.XPATH, value='(//android.widget.ImageView[@content-desc="关闭"])[1]')
        return el1,el2,el3


    #华为，控制正泰插座
    def huawei(self):
        driver = self.driver
        try:
            for i in range(2):

                el5 = driver.find_element(by=By.XPATH, value=
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[3]")
                el6 = driver.find_element(by=By.XPATH, value=
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[3]")
                el7 = driver.find_element(by=By.XPATH, value=
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[3]")

                # 这是向上滑动手机屏幕，通过循环加等待时间可得出下一步执行操作的时间
                for j in range(4):
                    self.UpSlide()
                    time.sleep(30)

                el5.click()
                el6.click()
                el7.click()

                time.sleep(5)
                el2 = driver.find_element(by=By.XPATH,
                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView")
                el3 = driver.find_element(by=By.XPATH,
                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView")
                el4 = driver.find_element(by=By.XPATH,
                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView")
                print(f"当前执行第{i + 1}次，各插座执行后状态为：{el2.text};{el3.text};{el4.text}")

        except:
            print("本页未找到")

    #手机向上滑动
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

    def __del__(self):
        pass

if __name__ == '__main__':
    s = Thua()
    s.huawei()