import  requests
import re

class Union_Port:

    def __init__(self):
        pass

    def git_url(self,issu):
        data_li = []
        html_num = requests.get(f"http://kaijiang.500.com/shtml/ssq/{issu}.shtml?")
        ls = str(html_num.content)
        reg_red = '<li class="ball_red">(.*?)</li>'
        reg_biue = '<li class="ball_blue">(.*?)</li>'
        #获取红色球
        ch = re.findall(reg_red,ls)
        #获取白色球
        ch_biue = re.findall(reg_biue,ls)
        #添加至列表
        l = [issu,ch,ch_biue]
        data_li.append(l)
        return data_li

    def __del__(self):
        pass

if __name__ == '__main__':
    d =  [[21049, ['04', '11', '13', '22', '25', '32'], ['01']]]
    # iss = 21049
    # t = Union_Port()
    # t.git_url(issu=iss)

