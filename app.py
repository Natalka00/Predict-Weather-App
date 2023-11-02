from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import os
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import get_location, error_message

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


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

        # Error: Empty fields
        if len(username) < 1 or len(password) < 1 or len(confirmation) < 1:
            return error_message("Fields cannot be empty.")
        
        # Error: Existing username
        db_connection = sqlite3.connect('database.db')
        db_cursor = db_connection.cursor()
        check_username = db_cursor.execute("SELECT username FROM users WHERE username = ?;", username)
        if len(check_username.fetchone()) > 0:
            db_connection.close()
            return error_message("Username already exists.")
        
        # Error: Too short password
        if len(password) < 8:
            return error_message("Password must be at least 8 characters long.")

        # Error: No digit in password
        elif not any(character.isdigit() for character in password):
            return error_message("Password must contain at least one digit.")

        # Error: No uppercase letter
        elif not any(character.isupper() for character in password):
            return error_message("Password must contain at least one uppercase letter.")

        # Error: No lowercase letter
        elif not any(character.islower() for character in password):
            return error_message("Password must contain at least one lowercase letter.")
        
        # TODO: Add special characters handling
        
        # Error: Confirmation unsuccessful
        elif password != confirmation:
            return error_message("Password confirmation unsuccessful")
        
        else:
            hash = generate_password_hash(password, method="pbkdf2", salt_length=16)

        
    else:
        return render_template("register.html")
    
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")