#读出用例.xlsx中的数据

import xlrd

class read:
    def __init__(self):
        book = xlrd.open_workbook(r'.\data\兼容测试用例.xlsx')
        self.sheet = book.sheets()[0]
        self.li_data = []
        for i in range(1, self.sheet.nrows):
            self.li_data.append(self.sheet.row_values(i))


    def Read_Excel(self):
        sheet = self.sheet
        return self.li_data


