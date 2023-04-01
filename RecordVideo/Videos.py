# encoding: utf-8
"""
@author: chenchao
@contact: 601652621@qq.com
@file: Videos.py
@software: PyCharm
@time: 2022/5/14 23:21
@desc: 
"""
from win32com.shell import shell,shellcon
from PIL import ImageGrab
import numpy as np
import cv2
import time
import os
from RecordVideo.ReadINI import reades

class Video:

    #获取ini文件内容
    def __init__(self):
        config = reades().config()
        self.value = config.get('videos-path', 'path')
        self.videos_name = config.get("videos-name", "name")
        self.debug = config.get("DEBUG","debug")
        self.fps = config.get("FPS","fps")
        self.start = config.get("Start","start")
        self.end = config.get("END","end")
    #获取当前时间
    def get_time(self):
        now = time.localtime()
        now_time = time.strftime("%Y%m%d%H%M%S", now)
        return now_time
    #开始录屏
    def RecVideo(self):

        fps = int(self.fps)
        start = int(self.start)  # 延时录制
        end = int(self.end)   # 自动结束时间
        curScreen = ImageGrab.grab()  # 获取屏幕对象
        height, width = curScreen.size
        #路径与文件名
        path = self.value
        name_time = path+f"{self.videos_name}_{self.get_time()}.avi"
        video = cv2.VideoWriter(f'{name_time}', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))
        imageNum = 0
        while True:
            imageNum += 1
            captureImage = ImageGrab.grab()  # 抓取屏幕
            frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)
            # 显示无图像的窗口
            cv2.imshow('capturing', np.zeros((1, 255), np.uint8))
            # 控制窗口显示位置，方便通过按键方式退
            cv2.moveWindow('capturing', height - 100, width - 100)
            if imageNum > fps * start:
                video.write(frame)
            # 退出条件
            if cv2.waitKey(50) == ord('q') or imageNum > fps*end:
                break
        video.release()
        cv2.destroyAllWindows()
    #删除视频文件
    def Delete_video(self):
        path = self.value
        debug = self.debug

        # for root, dirs, files in os.walk(path, topdown=False):
        #     fi = files
        # for i in range(1, len(fi)):
        #     for j in range(0, len(fi) - 1):
        #         if fi[j] > fi[j + 1]:
        #             fi[j], fi[j + 1] = fi[j + 1], fi[j]
        fi = os.listdir(path)
        #文件排序
        fi.sort()
        if debug == True:
            shell.SHFileOperation((0, shellcon.FO_DELETE, path + fi[0], None,
                                   shellcon.FOF_SILENT | shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION, None,
                                   None))  # 删除文件到回收站
        else:
            os.remove(path + fi[0])

if __name__ == '__main__':
    pass