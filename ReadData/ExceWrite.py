# -*- codeing = utf-8 -*-
# @Time：2022/9/29 20:58
# @Author：CHENCHAO
# @File：ExceWrite.py
# @Software：PyCharm

import xlwt
import xlsxwriter
import datetime

class Excelwrite:

    def __int__(self):
        pass

    def __del__(self):
        pass

    def writeXls(self):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet("Sheet1")
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.height = 20 * 11  # 字体大小，11为字号，20为衡量单位
        font.bold = True  # 黑体
        font.underline = False  # 下划线
        font.italic = True  # 斜体
        style.font = font  # 设定样式
        worksheet.write(0,0,"test")
        workbook.save(r"E:\Windows\Desktop\cc.xls")

    def writeExcel(self,data,filename):
        workbook = xlsxwriter.Workbook(filename)   #创建表格文件
        worksheet1=workbook.add_worksheet("Shee1") #创建子表
        worksheet1.activate()                      #激活表
        title = ["第一列","第二列","第三列"]          #设置表头
        worksheet1.write_row("A1",title)           #从A1单元格开始写入表头
        i= 2
        for j in range(len(data)):
            indata = [1,2,3]
            row = "A"+str(i)
            worksheet1.write_row(row,indata)
            i +=1
        workbook.close()


if __name__ == '__main__':
    data = [1,2,3]
    s = Excelwrite()
    # s.writeXls()
    # s.writeExcel(data,filename=r"E:\Windows\Desktop\CC.xlsx")