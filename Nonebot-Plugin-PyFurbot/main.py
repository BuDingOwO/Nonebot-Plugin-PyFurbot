import requests
import time
from .sign import getsign
from .Config import Config

authkey = Config.Token
api_url = "https://api.tail.icu/"
qq = Config.QQ


def gettime():
    t = time.time()
    t = str(round(t * 1000) / 1000)
    return t


# 来只毛模块
def GetFursuitRand():
    timestamp = gettime()
    api_path = "api/v2/getFursuitRand"
    params = {"qq": qq, "timestamp": timestamp, "sign": getsign(api_path, timestamp, authkey)}
    response = requests.get(api_url + api_path, params).json()
    return response


# 来只 {毛毛名字} 模块
def GetFursuitByName(name: str):
    timestamp = gettime()
    api_path = "api/v2/getFursuitByName"
    params = {"qq": qq, "timestamp": timestamp, "sign": getsign(api_path, timestamp, authkey), "name": name}
    response = requests.get(api_url + api_path, params).json()
    return response


# 找毛图模块
def GetFurByIdCommand(fid: str):
    timestamp = gettime()
    api_path = "api/v2/getFursuitByID"
    params = {"qq": qq, "timestamp": timestamp, "sign": getsign(api_path, timestamp, authkey), "fid": fid}
    response = requests.get(api_url + api_path, params).json()
    return response

# 每日鉴毛


