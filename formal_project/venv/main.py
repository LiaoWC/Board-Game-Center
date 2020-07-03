# 正式使用時，記得把debug模式改成False
ifDebugMode = True

# flask使用
from flask import Flask, render_template, request, redirect

# 亂數使用
import random

# sqlite3資料庫預備
import Sqlite3Utils

dbFileName = 'table.db'  # 檔名

# 其它自訂涵數預備
import other_functions

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
@app.route('/directly_search_name/<string:bg_name>')
def directly_search_name(bg_name):
    # name, year_published, board_category, min_player, max_player, min_playtime, max_playtime, age, rating, rating_player
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.name_search(bg_name)
    # print(resList)
    newList = other_functions.name_search_list(resList)
    return render_template('search_name_result.html', bgList=newList)


@app.route('/game_info/<string:bg_name>')
def game_info(bg_name):
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    resList = db.game_info(bg_name)
    newList = other_functions.name_search_list(resList)
    info = newList[0]
    return render_template('game_info.html', bg_name=bg_name, bg_info=info)


@app.route('/rate/<string:bg_name>')
def rate(bg_name):
    db = Sqlite3Utils.Sqlite3Utils(dbFileName)
    # sql = "INSERT INTO user_rating(game_id,rating) VALUES("+");"


# test
@app.route('/test')
def test():
    return render_template('test.html')


# run(這一段要放在程式最後面，不然可能頁面出不來)
if __name__ == '__main__':
    # app.run(port=(random.randint(20000, 30000)), host="127.0.0.1", debug=ifDebugMode)  # port在20000~30000隨機選一個
    # app.run(port=30003, host="0.0.0.0", debug=ifDebugMode)  # port在20000~30000隨機選一個
    app.run(port=80, host='0.0.0.0', debug=ifDebugMode)
