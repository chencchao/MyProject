import UnionLotto.OperationMySql
import UnionLotto.RequestPort
import time
import random

# data_li = [[21049, ['04', '11', '13', '22', '25', '32'], ['01']]]

port = UnionLotto.RequestPort.Union_Port()
sql = UnionLotto.OperationMySql.MyData()
inquire = 'select * from mydata.unionlotto_information'
s = sql.execute(statement=inquire)
lss = []
for i in s:
    lss.append(i[0])
lss_max = int(max(lss))
iss = 21063
iss_con = iss-lss_max
print(iss)
data_li =[]
if iss_con == 0:
    pass
else:
    for j in range(iss):
        data_li=(port.git_url(issu=iss-j))
        for i in data_li:
            number_red = i[0]
            one_red = i[1][0]
            two_red = i[1][1]
            three_red = i[1][2]
            four_red = i[1][3]
            five_red = i[1][4]
            six_red = i[1][5]
            seven_blue = i[2][0]
            stawrite_in = f"INSERT INTO unionlotto_information(number,one,two,three,four,five,six,seven)VALUES({number_red},{one_red},{two_red},{three_red},{four_red},{five_red},{six_red},{seven_blue});"
            sql.execute(statement=stawrite_in)
            print(f"{i[0]}+加入数据库成功")
        ti = random.randint(10,50)
        print(ti)
        time.sleep(ti)




