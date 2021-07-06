import time
from selenium import webdriver




class Union_web:

    def __init__(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()


    def wbe_di(self):
        di = {}
        for i in range(2):
            li = []
            lang = 21049 - i
            self.driver.get(f"http://kaijiang.500.com/shtml/ssq/{lang}.shtml?0_ala_baidu")
            time.sleep(5)
            for i in range(7):
                nu=i+1
                s=self.driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div[2]/div[1]/div[2]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/ul/li[{nu}]").text
                li.append(s)
            di[f"{lang}"]=li
            time.sleep(12)
        self.driver.quit()
        return di

    #数据库写入数据


    # def wbe_in_data(self):
    #     sql = UnionLotto.OperationMySql.MyData()
    #     in_di = self.wbe_di()
    #     for i in in_di:
    #             stawrite_in  =f"INSERT INTO unionlotto_information(number,one,two,three,four,five,six,seven)VALUES({int(i)},{int(in_di[i][0])},{int(in_di[i][1])},{int(in_di[i][2])},{int(in_di[i][3])},{int(in_di[i][4])},{int(in_di[i][5])},{int(in_di[i][6])});"
    #             sql.execute(statement=stawrite_in)


    def __del__(self):
        pass


if __name__ == '__main__':
    pass