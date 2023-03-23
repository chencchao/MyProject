import os
from ftplib import FTP

# 环境 Python 3.7
# 根据实际环境需要修改的变量：host,username,password，localpath,ftppath

# 1.登录FTP服务器
host = "10.42.0.100"
ftp = FTP()
ftp.connect(host, 21)
useranme = ""
password = ""
ftp.login(useranme,password)

# 2.切换到FTP服务器下载文件的路径
ftppath = '/ATE/AmlogicW1551/Public/'
ftp.cwd(ftppath)
# 切换到FTP服务器的路径下

# 3.获取FTP服务器切换路径下的文件名，定义为一个filebefore列表
filebefore = ftp.nlst()
# ftp.nlst()获取FTP服务器/DOC/路径下的文件名
# 将获取到的文件名放在列表里面

# 4.切换本地存放的路径
localpath = r"C:\\Users\\chenc\\Desktop"
os.chdir(localpath)
# 切换到本地目录下

# 5.判断部分文件是否存在
fileafter = []
# 定义一个空列表，通过获取到的文件名，判断是文件是否存在。
# 如果不存在，将不存在的文件名添加到fileafter列表里。
# 判断文件
for fileone in filebefore:
    if not os.path.exists(fileone):
        fileafter.append(fileone)

# 6.下载fileafter列表里的文件
for filetwo in fileafter:
    file_handle = open(filetwo, 'wb').write
    ftp.retrbinary("RETR " +filetwo, file_handle, blocksize=2048)
ftp.quit()


