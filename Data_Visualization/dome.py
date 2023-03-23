import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif']=['SimHei']  # 汉字字体


# #简单的折线图
# def broken():
#     a = [4, 5, 9, 14, 25, 27, 7]
#     fig, ax = plt.subplots()
#     ax.plot(a)
#     plt.show()

#修改签文字和线条粗细
# def linewidth():
#
#     a = [4, 5, 9, 14, 25, 27, 7]
#     i = [1, 2, 3, 4, 5, 6, 7]
#     # 使用内置样式
#     plt.style.use("seaborn")
#
#     fig, ax = plt.subplots()
#
#     ax.plot(i,a,linewidth=3)
#     ax.set_title("平方数",fontsize = 24)
#     ax.set_xlabel("值",fontsize = 14)
#     ax.set_ylabel("值的平方",fontsize = 14)
#
#     #设置刻度标记的大小
#     ax.tick_params(axis= "both",labelsize =14)
#     plt.show()

def scatte():

    plt.style.use("seaborn")
    fig , ax = plt.subplots()
    ax.scatter(2, 4,s=200)
    ax.set_title("平方数", fontsize=24)
    ax.set_xlabel("值", fontsize=14)
    ax.set_ylabel("值的平方", fontsize=14)

    ax.tick_params(axis="both", which = "major",labelsize=14)

    plt.show()


if __name__ == '__main__':
    scatte()