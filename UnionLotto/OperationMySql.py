import pymysql


class MyData:

    def __init__(self):
        try:
            # 连接数据库
            self.data_con = pymysql.connect(host='localhost', port=3306, user='root', password='12345678', database='mydata',charset='utf8')
        except:
            print("数据库连接失败")

    def execute(self,statement):
        data_con = self.data_con
        # #创建游标
        my_data = data_con.cursor()
        # #传入查询语句
        my_data.execute(statement)
        # #提交执行
        data_con.commit()
        # #执行成功就遍历结果的每行数据，以元组返回
        get_data = my_data.fetchall()
        return get_data

    def __del__(self):
        # 关闭数据库连接
        self.data_con.close()



if __name__ == '__main__':
    #写入语句
    stawrite_in  = "INSERT INTO unionlotto_information(number,one,two,three,four,five,six,seven)VALUES(21062,12,13,14,15,16,16,14);"
    inquire = 'select * from mydata.unionlotto_information'
    s = MyData()
    # 查询语句
    l = s.execute(statement=inquire)
    print(l)