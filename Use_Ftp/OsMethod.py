# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: OsMethod.py
@software: PyCharm
@time: 2022/4/21 11:35
@desc: 
"""

import os
#ftp可能用到的方法
class OS_Method:

    def __init__(self):
        pass

    # 判断本地文件或目录是否存在,Ture为存在
    def Local_Folder(self, path):
        s = os.path.exists(path)
        return s

    # 创建目录
    def Create_File(self, path):
        os.mkdir(path)
        return True

    # 创建多层目录
    def Create_Catalogue(self, path):
        os.makedirs(path)
        return True

    # 判断地址中是否为目录，Ture为目录,False不是目录
    def Judge_Catalogue(self, path):
        return os.path.isdir(path)

    # 返回本地文件详细的目录,返回列表
    def Print_Catalogue(self, path):
        return os.listdir(path)

    # 选择目录
    def put_Catalogue(self, ls, result):
        sentence = ["请选择你想进入的目录（填入序号）：", "请选择你想下载的文件（填入序号）："]

        if result == True:
            sen = sentence[1]
        else:
            sen = sentence[0]
        A = False
        while A == False:
            try:
                print(ls)
                catalogue = int(input(sen))
                if type(catalogue) == int:
                    A = True
                    return ls[catalogue]
            except (ValueError) as a:
                A = False
                print("输入类型错误，请重新选择")

    #替换替换"/"为"\"
    def file_put(self, cwd):
        cw = cwd
        cw_01 = cw[0:-1]
        cw = cw_01.replace("/", "\\")
        return cw

    #创建本地目录
    def Catalogue_case(self,path):
        if True == self.Local_Folder(path):
            return True
        else:
            self.Create_Catalogue(path)
        if True == self.Local_Folder(path):
            return True
        else:
           return False

    #判断本地目录是否创建成功
    def Catalogue_Test(self):
        pass


if __name__ == '__main__':
    pass
