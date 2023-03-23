# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: Start_up.py
@software: PyCharm
@time: 2022/5/12 17:10
@desc: 
"""

from RecordVideo.ReadINI import reades
from RecordVideo.Videos import Video
from RecordVideo.Windows_Event import WindowsEvent


class StartUp:

    def __init__(self):
        config = reades().config()
        self.vi = Video()
        self.WE = WindowsEvent()



    def start(self):
        vi = self.vi
        WE = self.WE
        vi.RecVideo()

if __name__ == '__main__':
    a= StartUp()

