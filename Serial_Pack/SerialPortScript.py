#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:Ai-Link
@User:chenc
@Date:2023/3/17 22:12 
"""
import datetime
import serial
import threading

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QGuiApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt

import sys

class SerialPort():
    # 模组串口配置，可以根据模组具体情况修改，使用的串口名字和波特率可以在程序启动参数指定
    def __init__(self, COM, Bu):
        super().__init__()
        # 端口与波特率要根据具体模组进行修改
        g_serial_port = COM  # COM口
        g_serial_baudrate = int(Bu)  # 波特率
        g_serial_bytesize = serial.EIGHTBITS  # 字节大小
        g_serial_parity = serial.PARITY_NONE  # 校验位
        g_serial_stopbits = serial.STOPBITS_ONE  # 停止位
        g_serial_timeout_s = 100  # 读超时设置
        # 连接串口
        try:
            self.serial_port = serial.Serial(g_serial_port, g_serial_baudrate, g_serial_bytesize, g_serial_parity,
                                         g_serial_stopbits,
                                         g_serial_timeout_s, rtscts=False)
        except:
            print( '拒接访问')

    #循环串口接收消息
    def PortReception(self,end="cc"):
        port = self.serial_port
        Condition = False
        while Condition==False:
            da=port.readline().splitlines()
            dat = (str(da[0])[2:-1])
            print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} 接收：{dat}')
            if dat != end:
                pass
            elif dat == end:
                print('-----接收到结束语句，断开串口-----')
                Condition=True

    #单次接收数据
    def portre(self):
        port = self.serial_port
        da = port.readline().splitlines()
        dat = (str(da[0])[2:-1])
        return (f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} 接收：{dat}')

    #单次串口发送消息
    def comser(self,Data=''):
        data = Data
        serial_port = self.serial_port
        serial_port.write((data+ '\r\n').encode('utf8'))
        return (f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} 发送：{data}')

    #循环串口发送消息
    def SendMessage(self,date,end='cc'):
        Condition = False
        while Condition == False:
            self.comser(Data=date)
            if date != end:
                pass
            elif date == end:
                Condition = True

    # 关闭串口
    def __del__(self):
        self.serial_port.close()

# class ui_port(QMainWindow):
#
#     def __init__(self):
#         super(ui_port,self).__init__()
#         uic.loadUi('ui_port.ui',self)
#
#         com='COM4'
#         bu=115200
#         self.a=SerialPort(COM=com,Bu=bu)
#         self.pButton01.clicked.connect(self.lineEdit_01)
#
#
#     def lineEdit_01(self):
#         data=self.lineEdit01.text()
#         t1 = threading.Thread(target=self.a.portre)
#         t2 = threading.Thread(target=self.a.comser,kwargs={"Data":data})
#         t2.setDaemon(True)
#         comser_data_g1 =t1.start()
#         comser_data_g2 = t2.start()
#         self.textEdit01.append(comser_data_g1)
#         self.textEdit01.append(comser_data_g2)
#
#     # def textEdit_01(self):
#     #
#     #
#     #     self.textEdit01.append(comser_data_g)
#

# def shw():
#     QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
#     app = QApplication(sys.argv)
#     my = ui_port()
#     my.show()
#     sys.exit(app.exec())

if __name__ == '__main__':
    # shw()

    com='COM4'
    bu=115200
    a=SerialPort(COM=com,Bu=bu)
    t1=threading.Thread(target=a.PortReception)
    t1.start()
    t2=threading.Thread(target=a.SendMessage)
    t2.setDaemon(True)
    t2.start()
    t2.join()

