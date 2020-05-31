class Sqlite3Utils:
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

    def filter_search(self, num_people, game_time, game_category):
        sql = "select name, board_category, min_player, max_player, min_playtime, max_playtime, rating, rating_player from info where "
        # players
        sql = sql + "min_player <= " + str(num_people) + " and " + "max_player >= " + str(num_people) + " "
        # game_time
        # if 'All':no play_time restriction
        if game_time == '<30 minutes':
            sql = sql + " and (max_playtime<=30 & max_playtime>=0)|(min_playtime<=30 & min_playtime>=0)|(max_playtime>=30 & min_playtime<=0) "
        elif game_time == '30~60 minutes':
            sql = sql + " and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30) "
        elif game_time == '1~2 hours':
            sql = sql + " and (max_playtime<=120 & max_playtime>=60)|(min_playtime<=120 & min_playtime>=90)|(max_playtime>=120 & min_playtime<=90) "
        elif game_time == '>2 hours':
            sql = sql + " and (max_playtime>=120)|(min_playtime>=120) "
        # game_category
        if game_category == 'All':
            sql = sql + " and board_category not like \'%Card Game%\' and board_category not like \'%Wargame%\' and board_category not like \'%Children\'\'s Game%\' and board_category not like \'%Dice%\' and board_category not like \'%Fantasy%\' and board_category not like \'%Abstract Strategy%\' and board_category not like \'%Miniatures%\' and board_category not like \'%Educational%\' and board_category not like \'%Party Game%\' and board_category not like \'%Science Fiction%\' and board_category not like \'%Fighting%\' and board_category not like \'%Trivia%\' and board_category not like \'%Economic%\' and board_category not like \'%Movies / TV / Radio theme%\' and board_category not like \'%Print & Play%\'"
        else:
            sql = sql + " and board_category like \'%" + (
                "Children''s Game" if game_category == "Children's Game" else game_category) + "%\' "
        # 按rating, rating_player排序
        sql = sql + " order by rating desc, rating_player desc "
        # 數量限制
        limit = 10
        sql = sql + " limit " + str(limit) + " "
        # 分號
        sql = sql + ";"
        print(sql)
        resList = self.db_exec(sql, 1)
        self.close()
        return resList

# dbName = 'test.db'
# db = Sqlite3Utils(dbName)
# sql = 'select * from test'
# resList = db.db_exec(sql, 1)
# print(resList)
