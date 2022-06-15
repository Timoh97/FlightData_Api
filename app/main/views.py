from doctest import script_from_examples
from flask import render_template
from . import main
from ..api import api_key


import json

# url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/direct/"

# querystring = {"destination":"LED","origin":"MOW"}

# headers = {
# 	"X-Access-Token": "undefined",
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)





import http.client

conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': "airport-info.p.rapidapi.com"
    }

code='ABV'
code1='/airport?iata'
code3=f'{code1}={code}'
conn.request("GET", code3 , headers=headers)

res = conn.getresponse()
data = res.read()

name=data.decode("utf-8")
conv = json.loads(name)

@main.route('/')
def index():
    airport={'airport':conv}
    airport=airport['airport']
    return render_template("index.html",airport=airport)