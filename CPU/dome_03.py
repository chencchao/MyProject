#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:My_Proj
@software:PyCharm
@User:chenchao
@contact: 601652621@qq.com
@file:dome_03
@Date:2023/3/23 17:23 
@desc: 获取电脑基础信息
"""
import wmi
import uuid

#获取电脑基本信息
class computer_Basic_information:

    def __init__(self):
        self.c = wmi.WMI()

    #获取电脑信息
    def get_computer_CSName_Caption_OSArchitecture(self):
        for i in self.c.Win32_OperatingSystem():
            return f"电脑操作系统：{i.Caption}，系统类型：{i.OSArchitecture}，设备名称：{i.CSName}\n"

    #获取磁盘Caption
    def get_disk_Caption(self):
        for i in self.c.win32_DiskDrive():
            return f"磁盘名称：{i.Caption}\n"

    #获取网卡物理地址
    def get_net_mac(self):
        node = uuid.getnode()
        macHex = uuid.UUID(int=node).hex[-12:]
        mac = []
        for i in range(len(macHex))[::2]:
            mac.append(macHex[i:i + 2])
        mac = ':'.join(mac)
        return f"网卡物理地址：{mac}\n"


if __name__ == '__main__':
    pass
    # a=computer_Basic_information()
    # print(a.get_computer_CSName_Caption_OSArchitecture())
    # print(a.get_net_mac())
    # print(a.get_disk_Caption())