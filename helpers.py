from functools import wraps
import requests
from flask import render_template, redirect, session

# Geolocation
def get_location(ip_address):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip_address))
        js_data = response.json()
        country = js_data["country"]
        city = js_data["city"]
        location_details = {"country": country ,"city": city}
        return location_details
    except:
        location_details = {"country": "unknown" ,"city": "unknown"}
        return location_details
    
# Error display
def error_message(message):
    return render_template("error.html", message=message)
    
# Login required decorator
def login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function