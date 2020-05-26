from flask import  Flask,render_template
from flask import request,session, redirect, url_for
import random
app=Flask(__name__)

app.secret_key='any random string'    #这里我们直接给定一个密钥


@app.route('/')
def index():
    msg=""
    return render_template("index.html",data=msg)  #加入变量传递

@app.route('/news')   #增加一个news页面
def newspage():
    import dbutil
    db = dbutil.dbUtils('newsDB.db')
    sql = 'select * from news'
    newslist = db.db_action(sql,1)
    db.close()
    return render_template("news.html",data=newslist)


@app.route('/productpage')  #增加一个product页面
def productpage():
    return render_template("productpage.html")

@app.route('/account')
def accountpage():
    return render_template("login.html")

@app.route('/login')
def loginpage():
    return render_template("login.html")


@app.route('/loginProcess',methods=['POST','GET'])
def loginProcesspage():
    if request.method=='POST':
        nm=request.form['nm']     #获取姓名文本框的输入值
        pwd=request.form['pwd']   #获取密码框的输入值
        if nm=='cao' and pwd=='123':
            session['username']=nm             #使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('index'))  #重定向跳转到首页
        else:
            return 'the username or userpwd does not match!'

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('index'))


@app.route('/search')
def search():
    return render_template("search.html")


if __name__=="__main__":
    app.run(port=(random.randint(20000,30001)),host="0.0.0.0",debug=True)
    # app.run( host="0.0.0.0", debug=True)