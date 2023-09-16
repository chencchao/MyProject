import sys
import unittest
from HTMLTestRunner2 import HTMLTestRunner
import ddt
from WoniuBoss兼容测试.Set_Drive import set_driver
from WoniuBoss兼容测试.read_excel import read


drive = ''
@ddt.ddt
class Assert_ele(unittest.TestCase):
    def setUp(self):
        self.imgs = []

    @ddt.data(*read().Read_Excel())
    def test_start(self,li):
        #利用内反射找到线性脚本相对应方法
        if li[4] == 'log_in':
            global drive
            if drive != '':
                drive.quit()
            else:
                pass
            drive=set_driver(li[-3],li[-2])

        __import__(f'WoniuBoss兼容测试.script.{li[2]}')
        mod = sys.modules[f'WoniuBoss兼容测试.script.{li[2]}']
        clss = getattr(mod, li[3])
        cls = clss()
        MTD=li[4]
        mtd = getattr(cls, MTD)
        #对参数进行切片
        data = []
        if len(li[-4])>0:
            li_d=li[-4].split('\n')
            for i in li_d:
                data.append(i.split('=')[1])
            #执行对应方法得到实际结果
            r=mtd(drive,data)
        else:
            r=mtd(drive)
        #将实际的返回结果与预期结果进行断言
        ret = r[0]
        img = r[1]
        self.imgs.append(img)
        self.assertIn(li[-1], ret)





if __name__ == '__main__':
    #利用HTMLteratrunner执行，并生成报告
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Assert_ele))
    f = open(r'./report.html','wb')
    runner = HTMLTestRunner(stream=f,title=u'测试报告',description=u'执行情况')
    runner.run(suite)
    f.close()



