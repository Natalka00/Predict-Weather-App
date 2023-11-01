from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import os
import sqlite3
from helpers import get_location, error_message

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3.connect('database.db')

@app.route("/")
def index():
    ip_address = request.remote_addr
    location = get_location(ip_address)
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if len(username) < 1 or len(password) < 1 or len(confirmation) < 1:
            return error_message("Fields cannot be empty")
        
    else:
        return render_template("register.html")