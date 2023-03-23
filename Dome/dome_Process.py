from multiprocessing import Process
import os
import time

#os.getpid()   获取当前进程ID

def run_proc(name):
    time.sleep(10)
    print(f'Run child process {name} {os.getpid()}')


def hello_world():
    # time.sleep(5)
    time.sleep(20)
    print('hello world!')
    print('Run child process (%s)...' % (os.getpid()))


if __name__ == '__main__':
    print(f'父进程开始    {os.getpid()}')
    p1 = Process(target=run_proc, args=('test',))
    p2 = Process(target=hello_world)
    p3 = Process(target=hello_world)
    print('子进程开始')
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    print('子进程结束')