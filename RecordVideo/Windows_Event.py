# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: Windows_Event.py
@software: PyCharm
@time: 2022/5/14 23:25
@desc: 
"""
import os
import mmap
import contextlib
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom
import shutil
from RecordVideo.ReadINI import reades

class WindowsEvent:

    def __init__(self):
        config = reades().config()
        self.WinOld = config.get("windows-path", "windows_original_path")
        self.WinNew = config.get("windows-path", "windows_copy_path")

    def windows_evtx(self):
        # 解析Windows事件日志
        with open(self.WinNew, 'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as buf:
                content = []
                fh = FileHeader(buf, 0)
                leveldict = {'1': '关键', '2': '错误', '3': '警告', '4': '消息'}
                for xml, record in evtx_file_xml_view(fh):
                    domtree = minidom.parseString(xml)
                    provider = domtree.getElementsByTagName('Provider')[0].getAttribute('Name')
                    eventid = domtree.getElementsByTagName('EventID')[0].childNodes[0].data
                    eventtime = domtree.getElementsByTagName('TimeCreated')[0].getAttribute('SystemTime')[:-7]
                    eventtype = leveldict[str(domtree.getElementsByTagName('Level')[0].childNodes[0].data)]
                    computer = domtree.getElementsByTagName('Computer')[0].childNodes[0].data
                    try:
                        processid = domtree.getElementsByTagName('Execution')[0].getAttribute('ProcessID')
                    except:
                        processid = ''
                    try:
                        evendatas = domtree.getElementsByTagName('Data')
                        evendata = ''
                        for i in evendatas:
                            evendata += i.childNodes[0].data + '  '
                    except Exception as e:
                        evendata = ''
                    d = dict(zip(['Provider', 'Evenid', 'Eventtime', 'Eventype', 'Processid', 'Computer', 'Evendata'],
                                 [provider, eventid, eventtime, eventtype, processid, computer, evendata]))
                    content.append(d)
            f.close()
            return content

    def windows_op_evtx(self):
        for file in os.listdir(self.WinOld):
            # 遍历原文件夹中的文件
            full_file_name = os.path.join(self.WinOld, file)  # 把文件的完整路径得到
            print("要被复制的全文件路径全名:", full_file_name)
            if os.path.isfile(full_file_name):  # 用于判断某一对象(需提供绝对路径)是否为文件
                shutil.copy(full_file_name, self.WinNew)  # shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹


if __name__ == '__main__':
    pass