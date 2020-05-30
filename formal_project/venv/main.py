# 正式使用時，記得把debug模式改成False
ifDebugMode = True

# flask使用
from flask import Flask, render_template,request

# 亂數使用
import random

# sqlite3資料庫預備
import sqlite3Utils
dbFileName = 'table.db' # 檔名

# 初始創建與執行(這一段要放在程式最後面，不然可能頁面出不來)
app = Flask(__name__)
app.secret_key = '33_db_project'  # 密鑰



# 路由：首頁
@app.route('/home')
@app.route('/')
def home():
    db = sqlite3Utils.sqlite3Utils(dbFileName)
    resList = db.home_search()
    return render_template('home.html',bgList=resList)

# 路由：篩選搜尋
@app.route('/filter')
def index():
    return render_template('search_filters.html')


# 依名稱搜尋
@app.route('/search_name', methods=['POST'])
def search_name():
    nameBeSearched = request.form['searchName'] # nameBeSearched 是使用者輸入的字
    print(nameBeSearched)
    return "great"

# 依篩選條件搜尋
@app.route('/search_filter', methods=['POST'])
def search_filter():
    numPeople = request.form['numPeople']
    gameTime = request.form['gameTime']
    gameCategory = request.form['gameCategory']
    print(numPeople,gameTime,gameCategory)
    return "grea"

# 路由：感謝、引用
@app.route('/credit')
def credit():
    return render_template('credit.html')


# run(這一段要放在程式最後面，不然可能頁面出不來)
if __name__ == '__main__':
    # app.run(port=(random.randint(20000, 30000)), host="127.0.0.1", debug=ifDebugMode)  # port在20000~30000隨機選一個
    app.run(port=30003, host="0.0.0.0", debug=ifDebugMode)  # port在20000~30000隨機選一個
