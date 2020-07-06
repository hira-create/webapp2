import pathlib
import os
from flask import Flask, render_template
from flask import jsonify
from modules import test_module

app = Flask(__name__)

BASE_DIR = pathlib.Path(__file__).parent


# GET メソッドのWEB API
@app.route("/get_candy/<key>", methods=["GET"])
def get_many_candy(key):
    candies: list = test_module.get_two_candy(int(key))
    return jsonify(candies)


@app.route("/candy")
def candy():
    candies: list = test_module.get_two_candy(2)
    return render_template("candy.html",
                           candies=candies
                           )


if __name__ == "__main__":
    print(BASE_DIR)
    app.run(debug=True, port=8080)
