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

    def home_search_old(self):
        sql = "select name, max_player, min_player, max_playtime, min_playtime from info where rating<=10 order by rating desc, rating_player desc limit 5;"
        resList = self.db_exec(sql, 1)
        self.close()
        return resList
        
    def home_search(self):
        sql = "select name, max_player, min_player, max_playtime, min_playtime from info left join (select game_id as id, sum(rating) as rating, count(rating) as rating_player from user_rating group by game_id)as ur on info.id=ur.id where info.rating<=10 and name not like \'%Expansion%\' and board_category not like \'%Expansion%\' order by case when ur.rating is NULL then (info.rating*info.rating_player+550)/(info.rating_player+100) else (info.rating*info.rating_player+ur.rating+550)/(info.rating_player+ur.rating_player+100) end desc, case when ur.rating is null then info.rating_player+100 else (info.rating_player+ur.rating_player+100) end desc limit 5;"
        resList = self.db_exec(sql, 1)
        self.close()
        return resList

    def filter_search_old(self, num_people, game_time, game_category):
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
        if game_category == 'Others':
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
        
    def filter_search(self, num_people, game_time, game_category):
        sql = "select info.name, info.board_category, info.min_player, info.max_player, info.min_playtime, info.max_playtime, case when ur.rating is NULL then info.rating else ((info.rating*info.rating_player)+(ur.rating))/(info.rating_player+ur.rating_player)end, case when ur.rating is NULL then info.rating_player else info.rating_player+ur.rating_player end from info left join (select game_id as id, sum(rating) as rating, count(rating) as rating_player from user_rating group by game_id)as ur on info.id=ur.id where "
        # players
        sql = sql + "min_player <= " + str(num_people) + " and " + "max_player >= " + str(num_people) + " "
        # game_time
        # if 'All':no play_time restriction
        if game_time == '<30 minutes':
            sql = sql + " and max_playtime<=30 "
        elif game_time == '30~60 minutes':
            sql = sql + " and (max_playtime<60 and max_playtime>=30) or (min_playtime<60 and min_playtime>=30) or (max_playtime>=60 and min_playtime<=30) "
        elif game_time == '1~2 hours':
            sql = sql + " and (max_playtime<120 and max_playtime>=60) or (min_playtime<120 and min_playtime>=60) or (max_playtime>=120 and min_playtime<=60) "
        elif game_time == '>2 hours':
            sql = sql + " and min_playtime>=120 "
        #不能有Expansion
        sql = sql + " and info.rating<=10 and name not like \'%Expansion%\' and board_category not like \'%Expansion%\' "
        # game_category
        if game_category == 'Others':
            sql = sql + " and board_category not like \'%Card Game%\' and board_category not like \'%Wargame%\' and board_category not like \'%Children\'\'s Game%\' and board_category not like \'%Dice%\' and board_category not like \'%Fantasy%\' and board_category not like \'%Abstract Strategy%\' and board_category not like \'%Miniatures%\' and board_category not like \'%Educational%\' and board_category not like \'%Party Game%\' and board_category not like \'%Science Fiction%\' and board_category not like \'%Fighting%\' and board_category not like \'%Trivia%\' and board_category not like \'%Economic%\' and board_category not like \'%Movies / TV / Radio theme%\' and board_category not like \'%Print & Play%\'"
        elif game_category == 'All':
            sql = sql
        else:
            sql = sql + " and board_category like \'%" + (
                "Children''s Game" if game_category == "Children's Game" else game_category) + "%\' "
        # 按rating, rating_player排序
        sql = sql + " order by case when ur.rating is NULL then (info.rating*info.rating_player+550)/(info.rating_player+100) else (info.rating*info.rating_player+ur.rating+550)/(info.rating_player+ur.rating_player+100) end desc, case when ur.rating is null then info.rating_player+100 else(info.rating_player+ur.rating_player+100) end desc "
        # 數量限制
        limit = 10
        sql = sql + " limit " + str(limit) + " "
        # 分號
        sql = sql + ";"
        resList = self.db_exec(sql, 1)
        self.close()
        return resList

    def name_search＿old(self, bg_name):
        sqlA = "select name, year_published, board_category, min_player, max_player, min_playtime, max_playtime, age, info.rating as info_rating, info.rating_player as info_rating_player from info,user_rating "
        sqlA = sqlA + "where name like \'%" + bg_name + "%\' and info.id = user_rating.game_id;"
        resList = self.db_exec(sqlA, 1)
        # sqlB = "select rating, rating_players from user_rating,info "
        # sqlB = sqlB + " where info.name = user_rating.rate and name = \'" + self.solve_apostrophe(bg_name) + "\' ;"
        # resListB = self.db_exec(sqlB, 1)
        newList = resList
        newList[8] = newList[8] + resListB[8]
        newList[9] = newList[9] + resListB[9]
        self.close()
        return newList
        
    def name_search(self, bg_name):
        sql = "select name, year_published, board_category, min_player, max_player, min_playtime, max_playtime, age, case when ur.rating is NULL then info.rating else ((info.rating*info.rating_player)+(ur.rating))/(info.rating_player+ur.rating_player)end, case when ur.rating is NULL then info.rating_player else info.rating_player+ur.rating_player end from info left join (select game_id as id, sum(rating) as rating, count(rating) as rating_player from user_rating group by game_id)as ur on info.id=ur.id "
        sql = sql + "where name like \'%" + bg_name + "%\' "
        sql = sql + "and info.rating<=10 and name not like \'%Expansion%\' and board_category not like \'%Expansion%\' "
        #sql = sql + "limit 10"
        sql = sql + ";"
        resList = self.db_exec(sql, 1)
        print(resList)
        self.close()
        return resList
        
    def game_info(self, bg_name):
        sql = "select name, year_published, board_category, min_player, max_player, min_playtime, max_playtime, age, info.rating as info_rating, info.rating_player as info_rating_player from info "
        sql = sql + "where name = \'" + bg_name + "\';"
        resList = self.db_exec(sql, 1)
        self.close()
        return resList
        
    def solve_apostrophe(self, string):
        newStr = ""
        for i in string:
            if i == "'":
                string = string + i + i
            else:
                string = string + i
        return newStr

# dbName = 'test.db'
# db = Sqlite3Utils(dbName)
# sql = 'select * from test'
# resList = db.db_exec(sql, 1)
# print(resList)
