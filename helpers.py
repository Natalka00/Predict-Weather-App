import requests

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
    