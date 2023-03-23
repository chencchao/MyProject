import time
#不加yield 时只会一个一个打印，加上yield时会同时打印



def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()
