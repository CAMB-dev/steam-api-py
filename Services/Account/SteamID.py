err_msg = {
    'success':-1,
    'errmsg':'Invalid Parameter'
},400
def GetSteamCommunityID(s:str) -> int:
    try:
        if int(s) <= 76561197960265728:
            return -1
        else:
            return int(s)
    except:
        steamid = s.split(':')
        if steamid[0] == '[U':
            if int(s[5:-1])%2==0:
                a = 0
                b = int(s[5:-1]) // 2
            else:
                a = 1
                b = (int(s[5:-1]) - 1) // 2
        else:
            a = int(steamid[1])
            b = int(steamid[2])
    return ((b * 2) + a) + 76561197960265728

def GetSteamID(sid:int) -> str:
    y = sid - 76561197960265728
    x = y % 2 
    return "STEAM_0:{}:{}".format(x, (y - x) // 2)

def GetSteamID32WithSymbol(s:str) -> str:
    steamid = s.split(':')
    a = int(steamid[1])
    b = int(steamid[2])
    return '[U:1:{0}]'.format(str(b*2+a))

def GetSteamID32(s:str) -> int:
    steamid = s.split(':')
    a = int(steamid[1])
    b = int(steamid[2])
    return b*2+a

def SteamIDConvert(s:str) -> dict:
    SteamId = None
    SteamId32 = None
    SteamCommunityID = None
    if s[:5] == 'STEAM':
        try:
            SteamCommunityID = GetSteamCommunityID(s)
            SteamId = s
            SteamId32 = GetSteamID32(s)
        except:
            return err_msg
    elif s[:5] == '[U:1:':
        try:
            SteamCommunityID = GetSteamCommunityID(s)
            SteamId = GetSteamID(SteamCommunityID)
            SteamId32 = s
        except:
            return err_msg
    else:
        try:
            if int(s) <= 76561197960265728:
                return err_msg
            SteamCommunityID = int(s)
            SteamId = GetSteamID(int(s))
            SteamId32 = GetSteamID32(SteamId)
            SteamId32WithSymbol = GetSteamID32WithSymbol(SteamId)
        except:
            return err_msg
    
    return {
        'success' : 0,
        'SteamID' : SteamId,
        'SteamID32' : SteamId32,
        'SteamID32WithSymbol' : SteamId32WithSymbol,
        'SteamCommunityID' : SteamCommunityID
    },200