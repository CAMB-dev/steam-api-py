import requests
from requests import Response

communityUrl = 'https://steamcommunity.com/'
steamApiUrl = 'http://api.steampowered.com/{0}/{1}/{2}/'
storeUrl = 'https://store.steampowered.com/'
def getCommunity(resource:str,params:dict={},headers:dict={}) -> Response:
    return requests.get(communityUrl+resource,params=params,headers=headers)

def getStore(resource:str,params:dict={},headers:dict={}) -> Response:
    return requests.get(storeUrl+resource,params=params,headers=headers)

def getSteamApi(interface:str,method:str,version:str,params:dict={},headers:dict={}) -> Response:
    return requests.get(steamApiUrl.format(interface,method,version),params=params,headers=headers)