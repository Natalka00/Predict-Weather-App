from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import os
import sqlite3
import helpers

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = sqlite3.connect('database.db')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # TODO: Get form data
        return
    else:
        return render_template("register.html")