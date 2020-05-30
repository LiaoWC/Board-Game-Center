class sqlite3Utils:
    def __init__(self, dbName):
        import sqlite3
        self.connection = sqlite3.connect(dbName)

    def db_exec(self, sql, operation_type=0):  # 0為返回查詢列表，1為返回邏輯值的操作
        try:
            result = self.connection.execute(sql)
            if operation_type == 0:
                return True
            else:
                return result.fetchall()
        except ValueError as e:
            print(e)

    def close(self):
        self.connection.commit()
        self.connection.close()

    def home_search(self):
        sql = "select name, max_player, min_player, max_playtime, min_playtime from info where rating<=10 order by rating desc, rating_player desc limit 5;"
        resList = self.db_exec(sql, 1)
        self.close()
        return resList


# dbName = 'test.db'
# db = Sqlite3Utils(dbName)
# sql = 'select * from test'
# resList = db.db_exec(sql, 1)
# print(resList)



