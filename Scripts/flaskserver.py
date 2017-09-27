'''
Basic Flask micro http server.
'''
from flask import Flask, redirect, render_template, request, session, url_for 

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"]=="":
        return render_template("fail.html")
    return render_template("success.html2")