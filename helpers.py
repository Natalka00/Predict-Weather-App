from flask import Flask
from flask import request
import requests

# Geolocation
def get_location(ip_adress):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip_adress))
        js_data = response.json()
        country = js_data["country"]
        city = js_data["city"]
        location_details = {"country": country ,"city": city}
        return location_details
    except:
        return "Unknown"