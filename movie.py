from flask import Flask, render_template, request, session, abort, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SubmitField, RadioField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import validators, ValidationError
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SubmitField
from passlib.hash import sha256_crypt

import pymysql
app = Flask(__name__)
app.secret_key = 'any random string'

#databsae link here
db = pymysql.connect(host="localhost", user="newuser", password="password", database="zen_theatre")
db.connect()  
#prepare a cursor object using cursor() method
# cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS USERS")
# create table
# sql = ("CREATE TABLE IF NOT EXISTS USER (FIRST_NAME CHAR(20), LAST_NAME CHAR(20), EMAIL CHAR(100), PASSWORD CHAR(20), FEES INT, PLAN CHAR(20))")
# cursor.execute(sql)
#insert data
# sql1 = ("INSERT INTO USER (FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, FEES, PLAN) VALUES ({form.first_name.data}, {form.last_name.data}, {form.email.data}, {form.password.data}, {form.fees.data}, {form.plan.data})")
# try:
#     cursor.execute(sql1)
#     db.commit()
# except:
#     db.rollback()
# db.close()

# @app.route("/admin/<name>")
# def admin_login(name):
#     return "Welcome %s! Sir Admin" % name

# @app.route("/guest/<guest>")
# def user(guest):
#     return "Welcome %s! Sir" % guest

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('index.html', title='Home')

@app.route('/the boys.html')
def theboysPage():
    return render_template('the boys.html', title='The Boys')

@app.route('/ant man.html')
def antmanPage():
    return render_template('ant man.html', title='Ant Man')

@app.route('/avengers.html')
def avengersPage():
    return render_template('avengers.html', title='Avengers')

@app.route('/college romance.html')
def collegeromancePage():
    return render_template('college romance.html', title='College Romance')

@app.route('/eesho.html')
def eeshoPage():
    return render_template('eesho.html', title='Eesho')

@app.route('/eternals.html')
def eternalsPage():
    return render_template('eternals.html', title='Eternals')

@app.route('/john wick.html')
def johnwickPage():
    return render_template('john wick.html', title='John Wick')

@app.route('/jurassic world.html')
def jurassicworldPage():
    return render_template('jurassic world.html', title='Jurassic World')

@app.route('/kota factory.html')
def kotafactoryPage():
    return render_template('kota factory.html', title='Kota Factory')

@app.route('/money heist.html')
def moneyheistPage():
    return render_template('money heist.html', title='Money Heist')

@app.route('/moon knight.html')
def moonknightPage():
    return render_template('moon knight.html', title='Moon Knight')

@app.route('/spiderman.html')
def spidermanPage():
    return render_template('spiderman.html', title='Spiderman')

@app.route('/thor love and thunder.html')
def thorloveandthunderPage():
    return render_template('thor love and thunder.html', title='Thor Love and Thunder')

@app.route('/topgun.html')
def topgunPage():
    return render_template('topgun.html', title='Topgun')

@app.route('/uncharted.html')
def unchartedPage():
    return render_template('uncharted.html', title='Uncharted')

@app.route('/account.html')
def account():
    return render_template('account.html', title='Account')

@app.route('/aboutus')
def aboutus():
    return render_template('about us.html', title='About Us')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/insertDB', methods=["POST","GET"])
def result():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        # prepare a cursor object using cursor() method
        db.connect()
        cursor = db.cursor()
        cursor.execute("""select (max(email) + 1) FROM `userLogin`""")
        email = cursor.fetchall()
        cursor.execute("""insert into userLogin(email,password) values(%s,%s)""",(email,password)) 
        
        try:
            db.commit()
            msg = "Name is successfully inserted!"
        except Exception as e:
            db.rollback()
        db.close()
        return render_template("login.html", msg = msg)
    
# @app.route('/enter', methods=['POST', 'GET'])
# def enter():
#     error = None
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         cursor = db.cursor()
#         sql = ("SELECT email, password FROM 'userLogin' WHERE email = '"+email+"' AND password = '"+password+"'")
#         cursor.execute(sql)
#         db.commit()
#         results = cursor.fetchall()
#         for row in results:
#             email = row[0]
#             password = row[1]
#             session['email'] = email
#             return(url_for('email', guest = email))


# @app.route('/enter', methods=["POST","GET"])        
# def check():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['password']
#         # prepare a cursor object using cursor() method
#         db.connect()
#         cursor = db.cursor()
#         sql = ("SELECT email, password FROM 'userLogin' WHERE email = '"+email+"' AND password = '"+password+"'")
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for row in results:
#             email = row[0]
#             password = row[1]
#         try:
#             db.commit()
#         except Exception as e:
#             db.rollback()
#         db.close()
#         if email == ' ':
#             msg = 'Incorrect email or password'
#             return render_template("login.html",msg = msg)
#         elif email == "admin":
#             return render_template('adminpage.html')
#         else:
#             session['email'] = email
#             db.connect()
#             cursor = db.cursor()
#             sql = ("SELECT email FROM `userLogin' WHERE email = '"+session['email']+"'")
#             cursor.execute(sql)
#             results = cursor.fetchall()
#             for row in results:
#                 email = row[0]
#             session['email'] = str(email)
#             try:
#                 db.commit()
#             except Exception as e:
#                 db.rollback()
#             db.close()
#             return render_template("account.html",guest = session['email'])
        


# @app.route('/logout')
# def logout():
#     session.pop('email', None)
#     return 'Welcome Back'

# @app.route('/index')
# @app.route('/')
# def index():
#     if 'email' in session:
#         return 'Logged in as ' + session['email'] + '<br>' + "<a href = '/logout'>Click here to log out</a>"
#     else:
#         return "Welcome User! You are not logged in<br><a href= '/login'>Click here to log in</a>"

if __name__ == '__main__':
    app.debug = True
    app.run(host = "0.0.0.0", port=8000)