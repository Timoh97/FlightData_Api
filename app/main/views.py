from flask import render_template
from . import main
from api import api_key

import requests

# url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/direct/"

# querystring = {"destination":"LED","origin":"MOW"}

# headers = {
# 	"X-Access-Token": "undefined",
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

@main.route('/')
def index():
    return render_template("index.html")