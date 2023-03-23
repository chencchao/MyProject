# -*- coding: gbk -*-
"""
@author: chenchao
@contact: 601652621@qq.com
@file: FtpMethod.py
@software: PyCharm
@time: 2022/4/19 15:33
@desc: ��¼ftp
"""
import time
from ftplib import FTP
import OsMethod
import os

#ftp��ʹ��
class Ftp_Method:

    def __init__(self):
        self.ftp = FTP()
        self.ftp.set_debuglevel(0)
        self.Method = OsMethod.OS_Method()

    # ��¼ftp
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

    #�л�Զ��Ŀ¼
    def  Switch_To_directory(self,Ftppath):
        ftp = self.ftp
        ftp.cwd(Ftppath)
        fileslist = ftp.nlst()
        filesname = ftp.dir()
        path = "192.168.110.112/����/"
        filemlsd01 ,filemlsd02= ftp.mlsd(path=path,facts=".")

        return fileslist,filesname,filemlsd01,filemlsd02#�л���Զ��Ŀ¼

    #�����ļ�,��鱾��Ŀ¼���籾����Ŀ¼�ʹ���Ŀ¼�����о�ֱ�������ļ�
    def Download(self,host,username,passed,port,cwd,path):
        fileafter = []
        ftp = self.ftp
        #�л�Զ��Ŀ¼
        filebefore, filesname,filemlsd01,filemlsd02= self.Switch_To_directory(cwd)
        #�滻"/"Ϊ"\"
        st = self.Method.file_put(cwd)
        #ƴ�ճ�ָ��·��
        localpath = path+st
        # ���Զ�̱���Ŀ���ޣ����ޣ��½�Ŀ¼
        self.Method.Catalogue_case(localpath)
        # �ı䵱ǰ����Ŀ¼��ָ��·��
        os.chdir(localpath)
        #�жϱ����ļ��Ƿ���ڣ��粻���ڼ�������б���
        for fileone in filebefore:
            s = self.Method.Local_Folder(fileone)
            if s == True:
                print(f"{fileone}���ļ��Ѵ���")
            if s == False:
                fileafter.append(fileone)
        #ѭ�������б�����ļ�
        for filetwo in fileafter:
            file_handle = open(filetwo, 'wb').write
            ftp.retrbinary("RETR " + filetwo, file_handle, blocksize=2048)

    #�ϴ��ļ�
    def Update_file(self,host,username,passed,port,cwd):
        ftp = self.ftp
        ftp.cwd(cwd)
        filebefore = ftp.nlst()
        print(filebefore)
        localpath = r"D:\chenchao\��������\aaa\΢��ͼƬ_20201123094924.jpg"
        localpath_name = localpath.split("\\")[-1]
        cmd = "STOR " + os.path.basename(localpath)
        fb = open(localpath, 'rb')
        ftp.storbinary(cmd,fb,blocksize=8192)
        if localpath_name in ftp.nlst():
            print("�ϴ��ɹ�")

    #Զ�̴���Ŀ¼
    def Establish_catalogue(self,host,username,passed,port,cwd):
        ftp = self.ftp
        ftp.cwd(cwd)
        localpath = r"D:\chenchao\��������\aaa"
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
            print("���Ŀ¼�ɹ�")
        else:
            print("���Ŀ¼ʧ��")

    #�ϴ�Ŀ¼���ļ�
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
    path=r"C:\Users\chenc\Desktop\��ʱ"
    host = "192.168.110.112"
    port = 21
    username = "chenchao"
    passed = "5566"
    cwd = "/����/"
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


