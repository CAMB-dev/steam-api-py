from flask import Flask
from flask import render_template
from Services.Account.SteamID import *
from Services.Account.Account import *

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/steamid/<id>')
def convertSteamID(id:str):
    return SteamIDConvert(id)

@app.route('/user/<id>/basicInfo')
def getBasicInfo(id:str):
    return GetBasicInfo(id)

@app.route('/user/<id>/gameList')
def getGameList(id:str):
    return GetGameList(id)

@app.route('/user/<id>/wishlist')
def getWishlist(id:str):
    return GetWishlist(id)

@app.route('/user/<id>/gameStat')
def getGameStat(id:str):
    return GetGameStat(id)