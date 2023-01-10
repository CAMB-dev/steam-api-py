from Utils import Web
from .SteamID import *
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup as bs
import json
err_msg = {
    'success':-1,
    'errmsg':'Internal Server Error'
},500

def GetBasicInfo(id:str) -> dict:
    scid = GetSteamCommunityID(id)
    if scid is -1:
        return err_msg
    resp = Web.getCommunity('/profiles/{0}'.format(str(scid)),params={'xml':'1'})
    if resp.status_code == 200:
        tree = ET.fromstring(resp.text)
        return {
            'steamID64':tree.find('steamID64').text,
            'name':tree.find('steamID').text,
            'onlineState':tree.find('onlineState').text,
            'avatarHash':tree.find('avatarIcon').text.split('/')[-1].split('.')[0],
            'customURL':tree.find('customURL').text,
            'memberSince':tree.find('memberSince').text,
            'summary':tree.find('summary').text
        },200
    else:
        return err_msg

def GetGameList(id:str) -> dict:
    scid = GetSteamCommunityID(id)
    if scid is -1:
        return err_msg
    resp = Web.getCommunity('/profiles/{0}/games/'.format(str(scid)),params={'tab':'all'})
    if resp.status_code == 200:
        soup = bs(resp.text,'html.parser')
        return json.loads(
            soup.find('script',attrs={'language':'javascript'})
            .text
            .replace('\n','')
            .replace('\t','')
            .replace('\r','')
            .replace('var rgGames = ','')
            .split(';var')[0]
        )
    else:
        return err_msg

def GetWishlist(id:str) -> dict:
    scid = GetSteamCommunityID(id)
    if scid is -1:
        return err_msg
    resp = Web.getStore('wishlist/profiles/{0}/wishlistdata'.format(scid))
    if resp.status_code == 200:
        return list(set(json.loads(resp.text).keys()))
    else:
        return err_msg

def GetGameStat(id:str) -> dict:
    scid = GetSteamCommunityID(id)
    if scid is -1:
        return err_msg
    sid32 = GetSteamID32(GetSteamID(scid))
    resp = Web.getCommunity('miniprofile/{0}/json'.format(str(sid32)))
    if resp.status_code == 200:
        try:
            return json.loads(resp.text)['in_game']
        except:
            return {}
    else:
        return err_msg
