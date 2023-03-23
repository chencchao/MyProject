import serial
import time

class TserialS():


    # 模组串口配置，可以根据模组具体情况修改，使用的串口名字和波特率可以在程序启动参数指定
    def __init__(self,com,bu):
        # 端口与波特率要根据具体模组进行修改
        g_serial_port = com
        g_serial_baudrate = int(bu)
        g_serial_bytesize = serial.EIGHTBITS
        g_serial_parity = serial.PARITY_NONE
        g_serial_stopbits = serial.STOPBITS_ONE
        g_serial_timeout_s = 5

        # 连接串口
        self.serial_port = serial.Serial(g_serial_port, g_serial_baudrate, g_serial_bytesize, g_serial_parity,
                                         g_serial_stopbits,
                                         g_serial_timeout_s, rtscts=False)

    # 通过串口发送指令
    def into_data(self, data):
        # 输入的指令
        data_into = data
        time.sleep(15)
        datas = self.serial_port.write((data_into + '\r\n').encode('utf8'))
        return datas

    #通过串口读取信息
    def out_data(self):
            #读取串口响应信息，字节1000
            data_out=str(self.serial_port.read(200)).split(r'\r\n')   #还需要增加多个响应的情况判断语句
            # print(data_out)
            result=[]
            #输出或打印根据实际情况进行判断
            for i in range(len(data_out)):
                # 获取当前时间
                times = time.strftime("%m-%d %X", time.localtime())
                #判断跳过不必要字符串
                with open("./1.txt", 'a', encoding="utf-8") as f:
                    f.write(times + ":  " + data_out[i]+"\n")
                if data_out[i] != ""  and  data_out[i] !="b'"  and data_out[i] !="'":
                    result.append(times+":  "+data_out[i])
                else:
                    pass
            return result

    def data_dome1(self,result):
        data_file = result
        #循环写入数据
        for i in range(len(data_file)):
            pass

    def __del__(self):
        self.serial_port.close()

if __name__ == '__main__':
    data_1 = "ATRS"
    data = "connect mi"
    s=TserialS("COM3",921600)
    b = s.out_data()
    a = s.into_data(data)