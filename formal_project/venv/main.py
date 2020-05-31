# 正式使用時，記得把debug模式改成False
ifDebugMode = True

# flask使用
from flask import Flask, render_template, request

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


# 路由：篩選搜尋選擇頁面
@app.route('/filter')
def index():
    return render_template('search_filters.html')


# 依篩選條件搜尋(Column: name, board_category, players(加工), playtime(加工), rating, rating_player)
# query得到的八欄，加工後六欄
@app.route('/search_filter', methods=['POST'])
def search_filter():
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
    # print(nameBeSearched)
    # print(type(nameBeSearched))
    return "great"


# 路由：感謝、引用
@app.route('/source')
def credit():
    return render_template('credit.html')


# run(這一段要放在程式最後面，不然可能頁面出不來)
if __name__ == '__main__':
    # app.run(port=(random.randint(20000, 30000)), host="127.0.0.1", debug=ifDebugMode)  # port在20000~30000隨機選一個
    app.run(port=30003, host="0.0.0.0", debug=ifDebugMode)  # port在20000~30000隨機選一個
