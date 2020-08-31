# -*- coding: utf-8 -*-


# 正式使用時，記得把debug模式改成False
ifDebugMode = True

# flask使用
from flask import Flask, render_template, request, redirect, session

# http的exception用
from werkzeug.exceptions import HTTPException

# 亂數使用
import random

# sqlite3資料庫預備
import Sqlite3Utils

dbFileName = 'table.db'  # 檔名

# 其它自訂涵數預備
import other_functions
from draw_dynamic import draw_dynamic

# 初始創建與執行(這一段要放在程式最後面，不然可能頁面出不來)
app = Flask(__name__)
app.secret_key = '33_db_project'  # 密鑰


# 路由：首頁
@app.route('/home')
@app.route('/')
def home():
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.home_search()
    print(resList)
    newList = other_functions.home_top_rating_list(resList)
    return render_template('home.html', bgList=newList)


# 路由：感謝、引用
@app.route('/source')
def credit():
    return render_template('source.html')


# 路由：篩選搜尋選擇頁面
@app.route('/search_filters')
def search_filters():
    return render_template('search_filters.html')


# 依篩選條件搜尋(Column: name, board_category, players(加工), playtime(加工), rating, rating_player)
# query得到的八欄，加工後六欄
@app.route('/search_filter_result', methods=['POST'])
def search_filter_result():
    num_people = request.form['numPeople']
    game_time = request.form['gameTime']
    game_category = request.form['gameCategory']
    # print(num_people, game_time, game_category)
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.filter_search(num_people, game_time, game_category)
    newList = other_functions.filter_search_list(resList)
    return render_template('search_filter_result.html', bgList=newList)


# 依名稱搜尋
@app.route('/search_name', methods=['POST'])
def search_name():
    nameBeSearched = request.form['searchName']  # nameBeSearched 是使用者輸入的字
    return redirect('directly_search_name/' + nameBeSearched)


# 直接搜尋名字
@app.route('/directly_search_name/<path:bg_name>')
def directly_search_name(bg_name):
    # name, year_published, board_category, min_player, max_player, min_playtime, max_playtime, age, rating, rating_player
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.name_search(bg_name)
    # print(resList)
    print(bg_name)
    newList = other_functions.name_search_list(resList)
    return render_template('search_name_result.html', bgList=newList)


@app.route('/game_info/<path:bg_name>')
def game_info(bg_name):
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.game_info(bg_name)
    print("rres:", resList)
    if len(resList) == 0:
        error_str = "This game \"" + bg_name + "\" does not exist in the database."
        return render_template('exception/exception.html', e=error_str, status404=0)
    newList = other_functions.name_search_list(resList)
    # print("resList: " ,resList)
    info = newList[0]
    return render_template('game_info.html', bg_name=bg_name, bg_info=info)


@app.route('/statistics')
def statistics():
    return render_template('statistics_home.html')


@app.route('/statistics/category_to_time')
def category_to_time():
    return render_template("statistics/category_to_time.html")


@app.route('/statistics/circulation_to_publishedyear')
def circulation_to_publishedyear():
    return render_template("statistics/circulation_to_publishedyear.html")


@app.route('/statistics/category_to_rating')
def category_to_rating():
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.category_to_rating_query()
    rand_num = random.randint(0, 9999999999999999999999999)
    draw_dynamic(resList, rand_num)
    return render_template("statistics/category_to_rating.html", flip=rand_num)


def if_string_is_int(str_):
    try:
        str_int = int(str_)
        if 10 >= str_int >= 1:
            return True
        else:
            return False
    except:
        return False


# 按了評分星星後
@app.route('/rate/<path:bgname>/<rating>')
def rate(bgname, rating):
    bgname = str(bgname)
    if not if_string_is_int(rating):
        return render_template('exception/exception.html',
                               e="The rating-score must be in integer and range from 1 to 10.", status404=0)
    rating = int(rating)
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    sqlA = "SELECT game_id FROM info,user_rating WHERE info.id = user_rating.game_id and info.name = \"" + bgname + "\";"
    id_list = (db.db_exec(sqlA, 1))
    if len(id_list) == 0:
        error_str = "This game \"" + bgname + "\" does not exist in the database."
        return render_template('exception/exception.html', e=error_str, status404=0)
    game_id = id_list[0][0]
    print("game_id: ", game_id)
    sqlB = "INSERT INTO user_rating(game_id,rating) values(" + str(game_id) + "," + str(rating) + ")"
    if not db.db_exec(sqlB, 0):
        return "Rate unsuccessfully."
    db.close()
    redirect_link = '/game_info/' + str(bgname)
    return redirect(redirect_link)


@app.errorhandler(404)
def exception_handling_404(e):
    return render_template('exception/exception.html', e=e, status404=1)


@app.errorhandler(HTTPException)
def exception_handling_http_general(e):
    return render_template('exception/exception.html', e=e, status404=0)


# run(這一段要放在程式最後面，不然可能頁面出不來)
if __name__ == '__main__':
    # app.run(port=(random.randint(20000, 30000)), host="127.0.0.1", debug=ifDebugMode)  # port在20000~30000隨機選一個
    # app.run(port=30003, host="0.0.0.0", debug=ifDebugMode)  # port在20000~30000隨機選一個
    app.run(port=80, host='0.0.0.0', debug=ifDebugMode)
