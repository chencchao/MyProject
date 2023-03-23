# -*- codeing = utf-8 -*-
# @Time：2022/9/29 20:17
# @Author：CHENCHAO
# @File：ExcelRead.py
# @Software：PyCharm

import xlrd

class Excelread:

    def __int__(self):
        pass

    def __del__(self):
        pass

    def OpenExcel(self,path,sheetName="Sheet1"):
        data = xlrd.open_workbook(path)
        #获取sheet名字
        sheet_name = data.sheet_names()
        if sheetName in sheet_name:
            #通过名称获取sheet
            table = data.sheet_by_name(sheet_name=sheetName)
            #行数
            nrows = table.nrows
            #列数
            ncols = table.ncols
            return  table,nrows,ncols
        else:
            print('设定的sheet不存在')

    #遍历读取每行数据
    def readrow(self,path,sheetName):
        table,nrows, ncols =self.OpenExcel(path,sheetName)
        for i in range(nrows):
            s = table.row_values(i, start_colx=0, end_colx=None)
            print(s)

    # 遍历读取每列数据
    def readcol(self,path,sheetName):
        table, nrows, ncols = self.OpenExcel(path, sheetName)
        for i in range(ncols):
            s = table.col_values(i, start_rowx=0, end_rowx=None)
            print(s)

    # 获取指定行数数据
    def readrow_row(self,path,sheetName):
        table, nrows, ncols = self.OpenExcel(path, sheetName)
        s = table.row_values(rowx=2)
        print(s)



if __name__ == '__main__':
    path = r'E:\Windows\Desktop\临时\新建文件夹\20220829_LH PLC_测试报告 - 终版.xlsx'
    sheet_name = '服务器功能测试'
    s = Excelread()
    # s.readcol(path,sheet_name)
    # s.readrow_row(path,sheet_name)