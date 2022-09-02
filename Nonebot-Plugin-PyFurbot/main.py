import requests
import time
from .utils import BuildSign
from .config import Config
from nonebot import get_driver

# global_config = get_driver().config
# config = Config.parse_obj(global_config)

authkey = Config.Token
api_url = "https://api.tail.icu/"
qq = Config.ID


# =============
# 获取时间
def gettime():
    t = time.time()
    t = str(round(t * 1000) / 1000)
    return t


# 来只毛模块
def GetFursuitRand():
    timestamp = gettime()
    api_path = "api/v2/getFursuitRand"
    params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey)}
    response = requests.get(api_url + api_path, params).json()
    print("\n" + str(params) + "\n")
    return response


# 来只 {毛毛名字} 模块
def GetFursuitByName(name: str):
    timestamp = gettime()
    api_path = "api/v2/getFursuitByName"
    params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey), "name": name}
    response = requests.get(api_url + api_path, params).json()
    return response


# 找毛图模块
def GetFurByIdCommand(fid: str):
    timestamp = gettime()
    api_path = "api/v2/getFursuitByID"
    params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey), "fid": fid}
    response = requests.get(api_url + api_path, params).json()
    return response


# 每日鉴毛
def GetDailyFurCommand(type: str, key: int or str):
    if type == "random":
        timestamp = gettime()
        api_path = "api/v2/DailyFursuit/Rand"
        params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey)}
        response = requests.get(api_url + api_path, params).json()
        return response
    if type == "id":
        timestamp = gettime()
        api_path = "api/v2/DailyFursuit/Id"
        params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey), "id": key}
        response = requests.get(api_url + api_path, params).json()
        return response
    if type == "name":
        timestamp = gettime()
        api_path = "api/v2/DailyFursuit/Name"
        params = {"qq": qq, "timestamp": timestamp, "sign": BuildSign(api_path, timestamp, authkey), "name": key}
        response = requests.get(api_url + api_path, params).json()
        return response
    else:
        return {"code": 501, "msg": "参数不合法"}

