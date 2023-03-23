#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@ModuleName:My_Proj
@software:PyCharm
@User:chenchao
@contact: 601652621@qq.com
@file:dome_04
@Date:2023/3/23 17:26 
@desc:获取电脑实时状况
"""
import datetime
import psutil
import time

#获取电脑实时状况
class computer_status:

    def __init__(self):
        pass

    def date_time(self):
        now_time = datetime.datetime.now()
        return now_time

    #监控整体的CPU情况
    def Allcpu(self):
        return  f"CPU使用情况：  {str(psutil.cpu_percent(interval=1))}%，当前时间：{self.date_time()}"

    #监控内存使用情况
    def Memory(self):
        phymem = psutil.virtual_memory()
        line = f"内存使用情况： {str(phymem.percent)}%    {str(int(phymem.used / 1024 / 1024)) + 'M'}/{str(int(phymem.total / 1024 / 1024)) + 'M'}，当前时间：{self.date_time()}"
        return line

    # 监控指定软件的内存情况
    def Single(self,exe_name):
        for proc in psutil.process_iter():
            try:
                if proc.name() == exe_name:
                    p = psutil.Process(proc.pid)
                    # print(p)
                    # print(p.memory_info())
                    proc_id = proc.pid
                    status = p.status()
                    memory_percent = round(p.memory_percent(), 2)
                    stime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.create_time()))
                    A=f'{exe_name}软件当前详情=>>>>>>当前系统时间：{self.date_time()}；进程ID：{proc_id}；进程状态：{status}；进程内存利用率：{memory_percent}；进程创建时间：{stime}\n'
                    return A
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # 进程未执行，不获取数据
                # table_name = 'finebi_memory'
                # sql = "INSERT INTO finebi_memory (proc_id,status, memory_percent, stime,strftime) VALUES ( '%s', '%s', '%s', '%s','%s' )"
                #
                # strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                # data = (0, 'kill', 0, strftime, strftime)
                pass

    #转换字节
    def bytes2human(self,n):
        # """
        # >>> bytes2human(10000)
        # '9.8 K'
        # >>> bytes2human(100001221)
        # '95.4 M'
        # """
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.2f %s' % (value, s)
        return '%.2f B' % (n)

    def poll(self,interval):
        tot_before = psutil.net_io_counters()
        pnic_before = psutil.net_io_counters(pernic=True)
        # sleep some time
        time.sleep(interval)
        tot_after = psutil.net_io_counters()
        pnic_after = psutil.net_io_counters(pernic=True)
        # get cpu state
        cpu_state = self.Allcpu()
        # get memory
        memory_state = self.Memory()

        return (tot_before, tot_after, pnic_before, pnic_after, cpu_state, memory_state)

    def ref_network(self,tot_before, tot_after, pnic_before, pnic_after, cpu_state, memory_state):
        li = []
        Summary01 = f"{cpu_state}; {memory_state}; 网络使用字节总数：sent: {self.bytes2human(tot_after.bytes_sent)}、received: {self.bytes2human(tot_after.bytes_recv)}; 网络使用总数据包数：sent: {tot_after.packets_sent}、received: {tot_after.packets_recv}\n"
        # li.append(Summary01)
        # nic_names = pnic_after.keys()
        # # nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
        # for name in nic_names:
        #     stats_before = pnic_before[name]
        #     stats_after = pnic_after[name]
        #     Summary02 = f'''
        #     {name}： bytes-sent：{self.bytes2human(stats_after.bytes_sent)}、{self.bytes2human(stats_after.bytes_sent - stats_before.bytes_sent)}；bytes-recv：{self.bytes2human(stats_after.bytes_recv)}、{self.bytes2human(stats_after.bytes_recv - stats_before.bytes_recv)}；pkts-sent：{stats_after.packets_sent}、{stats_after.packets_sent - stats_before.packets_sent}；pkts-recv：{stats_after.packets_recv}、{stats_after.packets_recv - stats_before.packets_recv}
        #     '''
        #     li.append(Summary02)
        return Summary01

if __name__ == '__main__':
    pass