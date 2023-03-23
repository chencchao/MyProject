# -*- coding: gbk -*-
"""
@author: chenchao
@contact: 601652621@qq.com
@file: FtpMethod.py
@software: PyCharm
@time: 2022/4/19 15:33
@desc: 登录ftp
"""
import time
from ftplib import FTP
import OsMethod
import os

#ftp的使用
class Ftp_Method:

    def __init__(self):
        self.ftp = FTP()
        self.ftp.set_debuglevel(0)
        self.Method = OsMethod.OS_Method()

    # 登录ftp
    def login_ftp(self,host,username,passed,port=21):
        ftp_log = self.ftp
        ftp_log.connect(host,port,timeout=60)
        ftp_log.login(username,passed)
        ftp_log.encoding = "gbk"
        # print(ftp_log.dir())
        return ftp_log.getwelcome()

    def Document_Judgment(self,host,username,passed,port,cwd):
        li = {}
        ftp = self.ftp
        ftp.dir()
        ls = ftp.nlst()
        # print(ls)
        for filesname in ls:
            # print(filesname)
            try:
                ftp.cwd(filesname)
                li[filesname]=True
            except:
                li[filesname]=False
            else:
                ftp.cwd('..')
        return li

    #切换远程目录
    def  Switch_To_directory(self,Ftppath):
        ftp = self.ftp
        ftp.cwd(Ftppath)
        fileslist = ftp.nlst()
        filesname = ftp.dir()
        path = "192.168.110.112/资料/"
        filemlsd01 ,filemlsd02= ftp.mlsd(path=path,facts=".")

        return fileslist,filesname,filemlsd01,filemlsd02#切换至远程目录

    #下载文件,检查本地目录、如本地无目录就创建目录，如有就直接下载文件
    def Download(self,host,username,passed,port,cwd,path):
        fileafter = []
        ftp = self.ftp
        #切换远程目录
        filebefore, filesname,filemlsd01,filemlsd02= self.Switch_To_directory(cwd)
        #替换"/"为"\"
        st = self.Method.file_put(cwd)
        #拼凑出指令路径
        localpath = path+st
        # 检测远程本地目有无，如无，新建目录
        self.Method.Catalogue_case(localpath)
        # 改变当前本地目录到指令路径
        os.chdir(localpath)
        #判断本地文件是否存在，如不存在即添加至列表里
        for fileone in filebefore:
            s = self.Method.Local_Folder(fileone)
            if s == True:
                print(f"{fileone}，文件已存在")
            if s == False:
                fileafter.append(fileone)
        #循环下载列表里的文件
        for filetwo in fileafter:
            file_handle = open(filetwo, 'wb').write
            ftp.retrbinary("RETR " + filetwo, file_handle, blocksize=2048)

    #上传文件
    def Update_file(self,host,username,passed,port,cwd):
        ftp = self.ftp
        ftp.cwd(cwd)
        filebefore = ftp.nlst()
        print(filebefore)
        localpath = r"D:\chenchao\个人资料\aaa\微信图片_20201123094924.jpg"
        localpath_name = localpath.split("\\")[-1]
        cmd = "STOR " + os.path.basename(localpath)
        fb = open(localpath, 'rb')
        ftp.storbinary(cmd,fb,blocksize=8192)
        if localpath_name in ftp.nlst():
            print("上传成功")

    #远程创建目录
    def Establish_catalogue(self,host,username,passed,port,cwd):
        ftp = self.ftp
        ftp.cwd(cwd)
        localpath = r"D:\chenchao\个人资料\aaa"
        localpath_name = localpath.split("\\")[-1]
        path_cwd = cwd+localpath_name
        filebefore = ftp.nlst()
        if localpath_name in filebefore:
            pass
        else:
            try:
                ftp.mkd(localpath_name)
            except (UnicodeDecodeError):
                pass
        filebefore = ftp.nlst()
        if localpath_name in filebefore:
            print("添加目录成功")
        else:
            print("添加目录失败")

    #上传目录中文件
    def Update_catalogue(self,host,username,passed,port,cwd):
        ftp = self.login_ftp(host, username, passed)
        pass

    def start(self,Ftppath):
        ftp = self.ftp
        ftp.cwd(Ftppath)
        fileslist = ftp.nlst()
        # filesname = ftp.mlsd(path="")
        print(fileslist)

    def __del__(self):
        self.ftp.quit()

if __name__ == '__main__':
    path=r"C:\Users\chenc\Desktop\临时"
    host = "192.168.110.112"
    port = 21
    username = "chenchao"
    passed = "5566"
    cwd = "/资料/"
    s = Ftp_Method()
    s.login_ftp(host,username,passed)
    l ,ll,lll,llll= s.Switch_To_directory(cwd)
    # print(l)
    # print(ll)
    print(lll)
    print(llll)
    # print(next(lll))
    # for i in lll:
    #     print(i)


