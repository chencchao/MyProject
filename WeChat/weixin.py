from Appium_Pack import CCAPP
import time


class Ten(CCAPP.TApp):
    # 微信
    date_huawei = {"noReset": True,
                   "platformName": "Android",
                   "platfromVersion": "10",
                   "deviceName": "EML_AL00",
                   "appPackage": "com.tencent.mm",
                   "appActivity": "com.tencent.mm.ui.LauncherUI"
                   }

    def __init__(self):
        super(Ten,self).__init__(data=self.date_huawei)


    def IntoHaier(self):
        driver = self.driver
        # self.DownSlide()
        el1 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.View")
        el1.click()   #进入海享租
        el2 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与海享租的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.TextView")
        el2.click()   #点击管理平台
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
        el3.click()   #点击验机中心
        time.sleep(30)
        el4 = driver.find_elements_by_link_text("登录").click()


if __name__ == '__main__':
    s = Ten()
    s.IntoHaier()