# 导入依赖库
import psutil,time
import re,string

# 打印系统全部进程的PID列表
# print(psutil.pids())

# 根据进程名获取进程PID
def get_pid(name):
    process_list = list(psutil.process_iter())
    # print(process_list)
    regex = "pid=(\d+),\sname=\'" + name + "\'"
    # print(regex)
    pid = 0
    for line in process_list:
        process_info = str(line)
        ini_regex = re.compile(regex)
        result = ini_regex.search(process_info)
        if result != None:
            pid = result.group(1)
            # print(pid)
            # print(result.group())
            return int(pid)

# 根据进程PID获取进程对象
def get_process_obj_by_id(pid):
    p ="0"
    try:
        p = psutil.Process(pid)
    except Exception as e:
        print(e)
    return p

# 获取Taskmgr的PID
pid = get_pid('msedge.exe')

# 根据Taskmgr的PID获取Taskmgr进程对象
process_obj=get_process_obj_by_id(pid)
num=0
while True:
    num+=1
    # 获取Taskmgr的CPU实时利用率，interval为间隔时间
    per = process_obj.cpu_percent(interval=1)
    put = f'''
    -----------------------------------msedge.exe CPU占用情况-------------------------------
    CPU占用率:{per}
    '''
    # print(put)
