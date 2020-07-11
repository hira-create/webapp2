import pathlib
import os
import sys
from flask import Flask, render_template
from flask import jsonify
from modules import test_module
from flask import request

app = Flask(__name__)

BASE_DIR = pathlib.Path(__file__).parent
#----------------------------------------------------
# GET メソッドのWEB API
@app.route("/get_number/<key>", methods=["GET"])
def sum_number(key):
    numbers: int = test_module.sum_number(int(key))
    return jsonify(numbers)

@app.route("/number")
def number():
    return render_template("button.html")
#----------------------------------------------------

# 入力スタート
@app.route('/')
def index():
    return render_template('index.html')

# POST GET(test)
@app.route('/output/',methods = ['POST', 'GET'])
def output():
    if request.method == 'GET':
        result  = request.args.get('url_get_text', '')
        url_text=result
        send_type="GET通信"
    elif request.method == 'POST':
        result  = request.form
        url_text=str(result["url_post_text"])
        send_type="POST通信"
    return render_template("output.html",url_text=url_text,send_type=send_type)

# ルーティング
@app.route('/good')
def good():
    name = "Good"
    return name



@app.route("/test_render")
def t_render():
    page_title = "test render title"
    disc = "TESTTESTETETEE"
    return render_template("test.html",
                           title=page_title,
                           disc=disc)

@app.route("/hirai")
def hira():
    hy = "hirai"
    return hy

@app.route("/login") #ログイン
def login():
    return render_template("login.html")

@app.route("/login_manager", methods=["POST"])  #POST
def login_manager():
    return "ようこそ、" + request.form["username"] + "さん"

if __name__ == "__main__":
    app.run(debug=True, port=8080, threaded=True)
