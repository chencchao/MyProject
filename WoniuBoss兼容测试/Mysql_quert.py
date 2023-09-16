import pymysql

class mysql_connet:
    con = pymysql.connect('192.168.6.237', 'root', '123456', 'woniuboss3.5')
    cur = con.cursor()
    def mysql_query(self,sql):
        a = self.cur.execute(sql)
        r = self.cur.fetchone()
        self.con.commit()
        return a, r
    def mysql_execute(self,sql):
        a = self.cur.execute(sql)
        self.con.commit()
        return a
    def mysql_query_all(self,sql):
        self.cur.execute(sql)
        r = self.cur.fetchall()
        self.con.commit()
        return r
    # def __del__(self):
    #     self.cur.close()
    #     self.con.close()