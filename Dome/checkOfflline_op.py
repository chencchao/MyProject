#enccoding=utf8
#author:yt
#version 2.3
'''
V1.2版本说明：
1）增加输入文件格式为非utf8的数据读取
2）日志打印，删除前部分的目录结构
3）取消总路径打印,只显示执行文件名称
4）增加时间显示

V2.3版本说明：
1）增加输入文件格式为非utf8的数据读取
2）日志打印，删除前部分的目录结构
3）取消总路径打印,只显示执行文件名称
4）增加时间显示
5）增加日志文件写入
6）增加对于查询关键字的时间与关键字不在一行时，需要前后查询的情况，并增加日志写入

V2.3.1版本说明：
1)取消查询统计次数未0时，打印空数据的行
2）增加文件夹区分标识"=====”

'''


'''
V2.3.3版本说明：
1)增加检测项前一行无数据、后一行无数据的异常处理
2)筛选者，可按照指定文件夹内，文件名筛选
3)增加离线时间间距筛选
4)修改不显示1次离线的数据
5)加了正泰对比校验（正泰的行在auto ...上面3行才有时间戳）
6)增加文件内容含有异常中文问题修改countByFileDirAndContent、countByRootDirAndContent两个函数
'''

'''
V2.3.4版本说明：
增加文件编码格式内容非常混乱的情况，采用追行处理方式，修改countByInputData、countByFileDirAndContent函数
修改getAllTime函数，使用正则方式获取时间，支持输入list中不含时间数据的行
'''
import time,os,chardet,re
def writeLog(w_filepath,data):
    log_w = open(w_filepath, mode='a',encoding='utf8')
    log_w.write(data+'\n')

def getTimeDictByStr(timeLine= '12-03 13:38:49[PnlSwit',timeFormat = "MM-DD hh:mm:ss"):
    #timeLine= '12-03 13:38:49[PnlSwit',timeFormat = "MM-DD hh:mm:ss"
    '''根据时间记录格式取出hh、mm、ss'''
    timeDict={}
    len_timeFormat = len(timeFormat)
    h_index = timeFormat.index('h')
    m_index = timeFormat.index('m')
    s_index = timeFormat.index('s')

    timeData = timeLine[0:len_timeFormat]                #时间记录的开始位置，若不在行首，则调整0的值
    hh = timeLine[h_index]+timeLine[h_index+1]
    mm = timeLine[m_index]+timeLine[m_index+1]
    ss = timeLine[s_index]+timeLine[s_index+1]
    try:
        timeDict['hh'] = int(hh)
        timeDict['mm'] = int(mm)
        timeDict['ss'] = int(ss)
    except:
        print("请手动检查每次查询的关键数据行的格式中timeLine，timeFormat是否都正确")
    return timeDict

def getAllTime(strList = []):
    '''
        strList = [ '02:13:38:49[PnlSwit',‘test 00001 ’，' '02:13:50:49[PnlSwit23333']
        取出list中所有时间数据，支持输入list中不含时间数据的行
        使用正则方式获取时间，现在支持输入"\r12-03 13:38:49[P" 、"12-03 13:38:49[P"、"12:03 13:38:49[P"、'\r01:19 14:57:53\r\n'
    '''
    all_time = []
    for i in strList:
        x = re.finditer(r'\d+[:-]\d+.\d+[:-]\d+[:-]\d+|\r\d+[:-]\d+.\d+[:-]\d+[:-]\d+', i)     #时间日期的格式根据实际情况调整
        for match in x:
            findStrtime = match.group()
            print('=========================================',findStrtime)
            if len(findStrtime) > 6:
                all_time.append(getTimeDictByStr())

    return all_time

def getTimeByIntervalTime(allTime = [],allowed = 2):
    '''
        allTime =[{'hh': 13, 'mm': 38, 'ss': 49}, {'hh': 14, 'mm': 38, 'ss': 59}, {'hh': 14, 'mm': 48, 'ss': 59}]
        allowed = 2 :若差距2min，则代表数据出现连上后再次失联
    '''
    _data = []
    _return = []
    if len(allTime) >1:
        _data.append(allTime[0])
        for i in range(len(allTime)-1):
            tmp = None
            if allTime[i]['hh'] < allTime[i+1]['hh']:
                _data.append(allTime[i+1])
            if allTime[i]['hh'] == allTime[i+1]['hh']:
                if allTime[i+1]['mm'] - allTime[i]['mm'] > allowed:
                    _data.append(allTime[i + 1])

                if allTime[i + 1]['mm'] - allTime[i]['mm'] == allowed and  allTime[i+1]['ss'] -  allTime[i]['ss'] > 0:
                    _data.append(allTime[i + 1])
    if len(allTime) == 1:
        _data.append(allTime[0])

    for timeDict in _data:
        if len(str(timeDict['hh'])) == 1 :
            hh = '0'+str(timeDict['hh'])
        else:
            hh = str(timeDict['hh'])
        if len(str(timeDict['mm'])) == 1:
            mm = '0' + str(timeDict['mm'])
        else:
            mm = str(timeDict['mm'])
        if len(str(timeDict['ss'])) == 1:
            ss = '0'+str(timeDict['ss'])
        else:
            ss = str(timeDict['ss'])
        _return.append(hh+':'+mm+':'+ss)
    return (_return)


class DealTime():
    def GetTimeByformat(self,format="%Y-%m-%d %H:%M:%S"):
        t =time.time()
        x = time.localtime(t)
        str_time = time.strftime(format,x)
        return str_time

class CheckOffline(DealTime):
    def __init__(self):
        self.log = None

    def countByInputData(self,content,selectdata):
        count = 0
        _return = {}
        _list = []
        for line,row_data in enumerate(content):
            try:
                if selectdata in row_data:
                    try:
                        # print(row_data)   #若要打印改行数据，可取消注释
                        # print(content[line - 5])   #若涉及时间在查询数据前一行，则取消注释
                        # print(content[line + 1])     #若涉及时间在查询数据后一行，则取消注释

                        _list.append(content[line - 5])   #若涉及时间在查询数据前一行，则取消注释?
                        _list.append(row_data)   #添加查询的的行
                        # _list.append(content[line + 1])
                    except:
                        print("****************最后一行为空***********************")
                    count = count+1

            except:
                    # print("【此行数据为NoneType】：",row_data)
                    pass
        print(_list)
        _return["count"] = count

        offlineTime = getTimeByIntervalTime(allTime=getAllTime(_list), allowed=2)
        _return["data"] = offlineTime
        return (_return)

    def countByFileDirAndContent(self,filepath=None, selectdata=None):
        '''做输出数据显示处理，以及文件格式读取'''
        DealCountAndData = {}
        try:
            file = open(file=filepath, mode='r', encoding='utf8')
            content = file.readlines()
        except:
            # try:
            #     file = open(file=filepath, mode='r')
            #     content = file.readlines()
            # except UnicodeDecodeError:
            #2.3.1版本修改
            #2.3.2版本增加每一行的加密方式验证
            file = open(file=filepath, mode='rb')
            content = file.readlines()
            print(filepath,'：文件编码有问题,转码后的文件还请核实是否影响查询内容，开始转码............')
            # return ('file UnicodeDecodeError')
            tmp_content = []
            for i, line in enumerate(content):
                try:
                    decode_line = line.decode('utf8')
                    # print('************', decode_line)
                    tmp_content.append(decode_line)
                except Exception as UnicodeDecodeError:
                    try:
                        decode_line = line.decode('gbk')
                        # print('************', decode_line)
                        tmp_content.append(decode_line)
                    except:
                        try:
                            decode_line = chardet.detect(line)['encoding']
                            # print('---------非gbk与utf8编码：', line.decode(decode_line))
                            tmp_content.append(decode_line)
                        except:
                            print('************************文件中有异常无法解码的字符，请手动检测****************************')
                            return ('file UnicodeDecodeError')
            content = tmp_content
        _return = self.countByInputData(content=content, selectdata=selectdata)
        count = _return["count"]
        data = _return["data"]

        fileName = filepath.split('\\')[-1]
        count_str = fileName + "统计的数量为：" + str(count)
        DealCountAndData['count_str'] = count_str
        DealCountAndData["data"] = data

        return DealCountAndData

    def countByRootDirAndContent(self,root_dir=None, selectData='offline',logPath = None,checkFileName=None):
        '''只支持根目录:子目录:文件的结构'''
        self.log = str(self.GetTimeByformat()+"开始查询%s下%s在各文件出现的次数" % (root_dir, selectData))
        print(self.log)
        writeLog(logPath,self.log)
        os.chdir(root_dir)
        currentRootDir = os.getcwd()
        # print(currentRootDir)   #总目录路径
        chdirs = os.listdir()
        self.log = self.GetTimeByformat()+"该文件夹下的一级子目录有："+ str(chdirs)    # 子目录
        print(self.log)
        writeLog(logPath, self.log)
        self.log = "合计文件夹数量为："+str(len(chdirs))
        print(self.log)
        writeLog(logPath, self.log)
        # writeLog(logPath,self.log)
        for dir in chdirs:
            chdir = os.path.join(root_dir, dir)
            os.chdir(chdir)
            print("=="*40)
            writeLog(logPath, "=="*40)
            self.log = self.GetTimeByformat()+"开始查询统计文件夹为："+ str(dir)   # 打印当前目录文件名称
            print(self.log)
            writeLog(logPath, self.log)
            os.getcwd()  # 进入子目录
            for files in os.walk(chdir):
                all_files = files[-1]
                # self.log = self.GetTimeByformat()+"该文件夹下的文件有："+ str(all_files)   # 获取子目录下的所有文件名称
                # print(self.log)
                writeLog(logPath, self.log)
                for fileName in all_files:
                    if checkFileName == fileName:
                        file_path = os.path.join(chdir, fileName)
                #         # 后续增加'''校验目录是否存在'''
                        _return = self.countByFileDirAndContent(file_path, selectdata=selectData)
                        if _return =='file UnicodeDecodeError':                            #2.3.1版本修改
                            break;
                        else:
                            count_str = _return['count_str']
                            data = _return['data']
                            if "统计的数量为：0" in count_str:
                                print(count_str)
                                writeLog(logPath, count_str)
                            else:
                                print(count_str)
                                print(data)
                                writeLog(logPath,count_str)
                                writeLog(logPath,str(data))
                    if checkFileName == None:
                    #查询所有文件
                        file_path = os.path.join(chdir, fileName)
                        #         # 后续增加'''校验目录是否存在'''
                        _return = self.countByFileDirAndContent(file_path, selectdata=selectData)
                        if _return == 'file UnicodeDecodeError':                      #2.3.1版本修改
                            break;
                        else:
                            count_str = _return['count_str']
                            data = _return['data']
                            if "统计的数量为：0" in count_str:
                                print(count_str)
                                writeLog(logPath, count_str)
                            else:
                                print(count_str)
                                print(data)
                                writeLog(logPath, count_str)
                                writeLog(logPath, str(data))

# checkDir ='F:/ZT-衰减挂机'
# logPath ='F:/衰减.log'

checkDir ='D:/0-软件测试/811204808-R-WIFI模组WF-H861-RTP1/1.0.0.104/log//长稳挂机日志/第二轮'
logPath ='D:/0-软件测试/811204808-R-WIFI模组WF-H861-RTP1/1.0.0.104/log/1.log'

# checkDir = 'D:/AI-Link/Case-Data/811204808-R-WIFI模组WF-H861-RTP1/v1.0.0.104/log/长稳挂机日志/非衰减组'
# logPath = 'D:/AI-Link/Case-Data/811204808-R-WIFI模组WF-H861-RTP1/v1.0.0.104/log/1.log'

# checkDir ='E:/RTS1-未衰减'
# logPath ='E:/RTS1未衰减.log'

# selectData = '[hilink_notify_devstatus(),83] status=0'
selectData ='去掉云端状态 hilink_notify_devstatus== 0'            #去掉云端状态 hilink_notify_devstatus== 0        #119固件,在离线前4行打印，上线行在
# selectData = "hilink_notify_devstatus== 1"
# selectData = 'auto'

checkOffline = CheckOffline()

testCheck_offline = checkOffline.countByRootDirAndContent(root_dir= checkDir,selectData = selectData,logPath = logPath,checkFileName="24.log")
print(testCheck_offline)

# content = ['12-22 10:360312-22 10:3603\r\n', '12-22 10:4015\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:40151 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4015IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8383135 \n', '\r\rboot reas12-22 10:4015on: 0 \n', '\r12-22 10:4015\rDONT PG EFUSE Under MP \n', '\r\rSystem_Init2\n', '\r\r#wifissid_: ssid,CHNT_Socket_Test,pwd,chint1984xyz\r\n', '\rinterface 0 is initialized\n', '\rinter12-22 10:4015face 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\n', '\r\rRTL8195A[Driver]: The driver is for MP\n', '\r\r\n', '\rLDO Mode,12-22 10:4015 BD_Info: 0 \n', '\r12-22 10:4015\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4016\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(67), Available heap 0xca7012-22 10:4058\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:40581 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4058\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4058IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8386568 \n', '\r\rboot reason: 0 \n', '\r12-22 10:4058\rDONT PG EFUSE Under MP \n', '\r\rSystem_Init2\n', '\r\r#wifissid_: ssid,CHNT_Socket_Test,pwd,chint1984xyz\r\n', '\rinterface 0 is initialized\n', '\rinter12-22 10:4058face 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\n', '\r\rRTL8195A[Driver]: The driver is for MP\n', '\r\r\n', '\rLDO Mode,12-22 10:4058 BD_Info: 0 \n', '\r\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4058\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(67), Available heap 0xca7012-22 10:4453\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:44531 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4453\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:1312-22 10:4453:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', 'ISO-8859-1', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:44531 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4453\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4453IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8386568 \n', '\r\rboot reas12-22 10:4453on: 0 \n', '\r12-22 10:4453\rDONT PG EFUSE Under MP \n', '\r\rSystem_Init2\n', '\r\r#wifissid_: ssid,CHNT_Socket_Test,pwd,chint1984xyz\r\n', '\rinterface 0 is initialized\n', '\rinter12-22 10:4453face 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\n', '\r\rRTL8195A[Driver]: The driver is for MP\n', '\r\r\n', '\rLDO Mode,12-22 10:4453 BD_Info: 0 \n', '\r\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4453\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(67), Available heap 0xca7012-22 10:4657\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', 'ISO-8859-1', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', 'ISO-8859-1', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', 'ISO-8859-1', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG1 ENTER\n', '\r\rCHIPID[0000012-22 10:46570ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4657\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4657IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8383135 \n', '\r\rboot reason: 0 \n', '\r12-22 10:4658\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:46581 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4658\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4658IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8383135 \n', '\r\rboot reas12-22 10:4658on: 0 \n', '\r12-22 10:4658\rDONT PG EFUSE Under MP \n', '\r\rSystem_Init2\n', '\r\r#wifissid_: ssid,CHNT_Socket_Test,pwd,chint1984xyz\r\n', '\rinterface 0 is initialized\n', '\rinter12-22 10:4658face 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\n', '\r\rRTL8195A[Driver]: The driver is for MP\n', '\r\r\n', '\rLDO Mode,12-22 10:4658 BD_Info: 0 \n', '\r\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4658\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(67), Available heap 0xca7012-22 10:4708\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:47081 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4708\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[ffffffff]\n', '\r\rOTA1 USE\n', '\r\rIMG2 DATA[0x8053eac:5072:0x10005000]\n', '\r\rIMG2 S12-22 10:4708IGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x804ff75]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8383135 \n', '\r\rboot reas12-22 10:4708on: 0 \n', '\r12-22 10:4708\rDONT PG EFUSE Under MP \n', '\r\rSystem_Init2\n', '\r\r#wifissid_: ssid,CHNT_Socket_Test,pwd,chint1984xyz\r\n', '\rinterface 0 is initialized\n', '\rinter12-22 10:4708face 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\n', '\r\rRTL8195A[Driver]: The driver is for MP\n', '\r\r\n', '\rLDO Mode,12-22 10:4708 BD_Info: 0 \n', '\r12-22 10:4708\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4708\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(67), Available heap 0xca7012-22 10:4736ATSC\r\n', '\r[ATSC]: _AT_SYSTEM_Switch to OTA2 app!!\r\n', '\r\rBitIdx: 0 \n', '\r\rcurrrent is OTA1, select OTA2 \n', '\r12-22 10:4736\r<RTL8195A>\rROM:[V0.1]\n', '\r\rFLASHRATE:4\n', '\r\rBOOT TYPE:0 XTAL:40000000\n', '\r\rIMG1 DATA[1168:10002000]\n', '\r\rIMG1 ENTRY[8000541:100021ef]\n', '\r\rIMG12-22 10:47361 ENTER\n', '\r\rCHIPID[000000ff]\n', '\r\rread_mode idx:0, flash_speed idx:0\n', '\r12-22 10:4736\rcalibration_result:[1:5:11][9:d] \n', '\r\rcalibration_result:[2:13:7][1:d] \n', '\r\rcalibration_result:[3:3:3][1:3] \n', '\r\rcalibration_ok:[2:13:7] \n', '\r\rFLASH CALIB[NEW OK]\n', '\r\rOTA2 ADDR[8100000]\n', '\r\rOTAx SELE[fffffffe]\n', '\r\rOTA2 USE\n', '\r\rOTA2 SIGN[35393138:31313738]\n', '\r\rIMG2 DATA[0x81a95d0:7604:0x10005000]\n', '\r\rIMG2 SIGN[RTKWin(10005008)]\n', '\r\rIMG2 ENTRY[0x10005000:0x81001b9]\n', '\r\r===== Enter Image 2 ====\n', '\r\rSystem_Init1\n', '\r\rOSC8M: 8386568 \n', '\r\rboot reason: 5 \n', '\r12-22 10:4736\rSystem_Init2\n', '\r\r# sample_TaskCreat stack size 5k byte!\r\n', '\r\r\r\n', '\rLiteOS Release Date: 2019/07/05-10:08:41\r\n', '\r\rLiteOS Version: LiteOSV12-22 10:4736200R001C10B335SP1\r\n', '\rinterface 0 is initialized\n', '\rinterface 1 is initialized\n', '\r\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\r\n', '12-22 10:4736\rLDO Mode, BD_Info: 0 \n', '\r12-22 10:4736\n', '\r\rStart LOG SERVICE MODE\n', '\r\r\n', '\r\r# 12-22 10:4736hilink sdk build time Jul 10 2019 22:47:29\r\n', '\rhilink sdk version v9.0.10.323[date:2019-07-10 22:47:29 compiler:arm-none-eabi-gcc]12-22 10:4736\r\n', '\r12-22 10:4736\rCreate Task "rtw_recv_tasklet"\n', '\r\rCreate Task "rtw_xmit_tasklet"\n', '\r\rCreate Task "rtw_interrupt_thread"\n', '\r\rCreate Task "cmd_thread"12-22 10:4736\n', '\r\n', '\r\rWIFI initialized\n', '\r\n', '\r\rinit_thread(74), Available heap 0x11ae4\r\n', '\r\r\n', '\r 保留wifi状态做指示灯 hilink_notify_devstatus== 5\r\n', '\r12-22 10:4736\n', '\r\rLwIP_DHCP: dhcp stop.\n', '\r\rDeinitializing WIFI ...\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r12-22 10:4736\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelete Task "cmd_thread"\n', '\r\rDelete Task "rtw_interrupt_thread"\n', '\r\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelet12-22 10:4736e Task "rtw_recv_tasklet"\n', '\r\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelete Task "rtw_xmit_tasklet"\n', '\r\n', '\r\rWIFI deinitialized\n', '\r\rInitializing WI12-22 10:4736FI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r12-22 10:4737\rCreate Task "rtw_recv_tasklet"\n', '\r\rCreate Task "rtw_xmit_tasklet"\n', '\r\rCreate Task "rtw_interrupt_thread"\n', '\r\rCreate Task "cmd_thread"12-22 10:4737\n', '\r\n', '\r\rWIFI initialized\n', '\r\rCreate Task "LateResumeThread"\n', '\r12-22 10:4737clr wdt\r\n', '\r指示灯开关 backlight == on\r\n', 'ISO-8859-1', '\r电量校准参数偏差系数 = 0.000000\r\n', None, '\r功率校准参数偏差系数  = 0.000000\r\n', '\r\r\n', '\r\r12-22 10:4737\n', 'ISO-8859-1', '\r\r\n', '\r12-22 10:4737\r\n', '\r=============hilink ver infor===================\r\n', '\r\t\tfirmwareVer 1.0.0.116\r\n', '\r\t\tsoftwareVer 1.0.0\r\n', '\r\t\thardwareVer 1.0.0\r\n', '\r\t\t产12-22 10:4737品名称 正泰智能插座(hilink)\r\n', '\r\t\t最大功率 2500W\r\n', '\r\r\n', '\r=============hilink ver infor===================\r\n', '\r12-22 10:4737\r\n', '\r======== Wifi Module Information ========\r\n', '\r\r\n', '\r  Firmware Version:1.0.0.116\r\n', '\r  Release Date:2019/08/19-16:01:27\r\n', '\r  MAC: 54:12-22 10:4737f1:5f:a8:9b:7b\r\n', '\r\r\n', '\r======== Wifi Module Information ========\r\n', '\r12-22 10:4737\r\n', '\r\r\n', '\r\r\n', '\r=============hilink ver infor===================\r\n', '\r\t\tfirmwareVer 1.0.0.116\r\n', '\r\t\tsoftwareVer 1.0.0\r\n', '\r\t\thardwareVer 1.0.0\r\n', '\r\t\t产品名称 正泰智能插座(hilink)\r\n', '\r\t\t最大功率 2500W\r\n', '\r\r\n', '\r=============hilink ver infor===================\r\n', '\r12-22 10:4737\r\n', '\r======== Wifi Module Information ========\r\n', '\r\r\n', '\r  Firmware Version:1.0.0.116\r\n', '\r  Release Date:2019/08/19-16:01:27\r\n', '\r  MAC: 54:12-22 10:4737f1:5f:a8:9b:7b\r\n', '\r\r\n', '\r======== Wifi Module Information ========\r\n', '\r12-22 10:4737厂测wifi ssid: CHNT_Socket_Test,pwd:chint1984xyz\r\n', '\r\r\n', '\r\r\n', '\r在正泰加工厂-工厂校准测试模式\r\n', '\r\r\n', '\r$$key test:3000ms##\r\n', '\r12-22 10:4738\r\n', '\r\r\n', '\r在正泰加工厂-按键退出闪灯模式\r\n', '\r\r\n', '\r\r\n', '\r\r\n', '\r上电必须是按键必须是弹起的 ,以便检测按键是不是好的\r\n', '\r\r\n', '\r12-22 10:4745set sta cb not reg\r\n', '\r12-22 10:4748\n', '\r\rLwIP_DHCP: dhcp stop.\n', '\r\rDeinitializing WIFI ...\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r12-22 10:4748\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelete Task "cmd_thread"\n', '\r\rDelete Task "rtw_interrupt_thread"\n', '\r\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelet12-22 10:4748e Task "rtw_recv_tasklet"\n', '\r\r\n', '\r\rRTKTHREAD exit Swt_Task\n', '\r\rDelete Task "rtw_xmit_tasklet"\n', '\r\n', '\r\rWIFI deinitialized12-22 10:4748\n', '\r\rInitializing WIFI ...\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r\r\n', '\rLDO Mode, BD_Info: 0 \n', '\r12-22 10:4749\rCreate Task "rtw_recv_tasklet"\n', '\r\rCreate Task "rtw_xmit_tasklet"\n', '\r\rCreate Task "rtw_interrupt_thread"\n', '\r\rCreate Task "cmd_thread"\n', '\r12-22 10:4749\n', '\r\rWIFI initialized\n', '\r12-22 10:4749\r\n', '\r\r\n', '\r 保留wifi状态做指示灯 hilink_notify_devstatus== 7\r\n', '\r12-22 10:4750\rmemcpy_s ret:34\r\n', '\r12-22 10:4753\rwlan1: 1 DL RSVD page success! DLBcnCount:01, poll:00000001\n', '\r12-22 10:4754\r\n', '\r\r\n', '\r 保留wifi状态做指示灯 hilink_notify_devstatus== 8\r\n', '\r12-22 10:4754\r\n', '\r\r\n', '\r去掉云端状态 hilink_notify_devstatus== 9\r\n', '\r12-22 10:4755set rtc time for first time [1608605275]\r\n', '\rtime sync for first time, current utc time is:\r\n', '\r   2020-12-22 2:47:55\r\n', '\r12-22 10:4755\r\n', '\r\r\n', '\r 补丁云端在线 肯定连接wifi了 hilink_notify_devstatus\r\n', '\r\r\n', '\r\r\n', '\r去掉云端状态 hilink_notify_devstatus== 1\r\n', '\r\r\n', '\r 设备上线\r\n', '\r12-22 10:4755boot reason (1)\r\n', '\r12-22 10:4755\r\n', '\r\r\n', '\rstart process GET cmd: ID - switch\r\n', '\r\r\n', '\r hilink get_char::: {"on":0}\r\n', '\r12-22 10:4755set dia [1]\r\n', '\r12-22 10:4755\r\n', '\r\r\n', '\rstart process GET cmd: ID - power\r\n', '\r\r\n', '\r hilink get_char::: {"current":0}\r\n', '\r\r try post queue write failed, ret = [0x200061612-22 10:4755],task:tcpip_thread \n', '\r12-22 10:4755\r\n', '\r\r\n', '\rstart process GET cmd: ID - consumption\r\n', '\r\r\n', '\r hilink get_char::: {"consumption":0}\r\n', '\r12-22 10:4755set dia [1]\r\n', '\r12-22 10:4755\r\n', '\r\r\n', '\rstart process \r try post queue write failed, ret = [0x2000616],task:tcpip_thread \n', '\rGET cmd: ID - faultDetection\r\n', '\r\r\n', '\r hilink get_char::: {"code":0,"status":0}\r\n', '\r12-22 10:4756\r\n', '\r\r\n', '\rstart process GET cmd: ID - memorySwitch\r\n', '\r\r\n', '\r hilink get_char::: {"status":0}\r\n', '\r12-22 10:4756\r\n', '\r\r\n', '\rstart process GET cmd: ID - timerInfo\r\n', '\r\r\n', '\r hilink get_char::: {"num":0,"timerI\r try post queue write failed, ret = [0x20012-22 10:47560616],task:tcpip_thread \n', '\rnfo":[]}\r\n', '\r12-22 10:4756\r try post queue write failed, ret = [0x2000616],task:tcpip_thread \n', '\r\r\n', '\r\r\n', '\rstart process GET cmd: ID - backlight\r\n', '\r\r\n', '\r hilink ge12-22 10:4756t_char::: {"on":1}\r\n', '\r12-22 10:4756\r try post queue write failed, ret = [0x2000616],task:tcpip_thread \n', '\r12-22 10:4756\r try post queue write failed, ret = [0x2000616],task:tcpip_thread \n', '\r12-22 10:4809set dia [1]\r\n', '\r12-22 10:4817start handle PUT cmd: ID-switch, payload-{"on":1}\r\n', '\rtimer or delay 打开继电器 \r\n', '\r\r\n', '\r\r\n', '\rstart process GET cmd: ID - switch\r\n', '\r\r\n', '\r 12-22 10:4817hilink get_char::: {"on":1}\r\n', '\r12-22 10:4817\r\n', '\r\r\n', '\rstart process GET cmd: ID - switch\r\n', '\r\r\n', '\r hilink get_char::: {"on":1}\r\n', '\r12-22 11:1347\r\n', '\r\r\n', '\r去掉云端状态 hilink_notify_devstatus== 0\r\n', '\r\r\n', '\r 设备离线\r\n', '\r12-22 11:1503\r\n', '\r\r\n', '\r 补丁云端在线 肯定连接wifi了 hilink_notify_devstatus\r\n', '\r\r\n', '\r\r\n', '\r去掉云端状态 hilink_notify_devstatus== 1\r\n', '\r\r\n', '\r 设备上线\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - switch\r\n', '\r\r\n', '\r hilink get_char::: {"on":1}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - power\r\n', '\r\r\n', '\r hilink get_char::: {"current":0}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - consumption\r\n', '\r\r\n', '\r hilink get_char::: {"consumption":0}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - faultDetection\r\n', '\r\r\n', '\r hilink get_char::: {"code":0,"status":0}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - memorySwitch\r\n', '\r\r\n', '\r hilink get_char::: {"status":0}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - timerInfo\r\n', '\r\r\n', '\r hilink get_char::: {"num":0,"timerInfo":[]}\r\n', '\r12-22 11:1504\r\n', '\r\r\n', '\rstart process GET cmd: ID - backlight\r\n', '\r\r\n', '\r hilink get_char::: {"on":1}\r\n', '\r12-22 11:4826set rtc time for first time [1608608907]\r\n', '\r12-22 12:4829set rtc time for first time [1608612510]\r\n', '\r12-22 13:4833set rtc time for first time [1608616113]\r\n', '\r12-22 14:3501ota check task created, flag [0]\r\n', '\r12-22 14:3502\n', '\r[HTTPC] Use ciphersuite TLS-RSA-WITH-AES-128-GCM-SHA256\n', '\r12-22 14:3502no new version checked\r\n', '\rota check task exit\r\n', '\r12-22 14:4837set rtc time for first time [1608619717]\r\n', '\r12-22 15:4841set rtc time for first time [1608623322]\r\n', '\r12-22 16:4845set rtc time for first time [1608626926]\r\n', '\r12-22 17:284212-22 17:2842\r\n', '12-22 17:28:4512-22 17:28:45\r\n', '12-22 17:48:49set rtc time for first time [1608630530]\r\n', '\r12-22 18:48:53set rtc time for first time [1608634134]\r\n', '\r12-22 19:48:57set rtc time for first time [1608637738]\r\n', '\r12-22 20:49:01set rtc time for first time [1608641342]\r\n', '\r12-22 21:49:05set rtc time for first time [1608644947]\r\n', '\r12-22 22:49:09set rtc time for first time [1608648550]\r\n', '\r12-22 23:49:13set rtc time for first time [1608652155]\r\n', '\r']
# # content = ['test','离线']
# checkOffline = CheckOffline()



