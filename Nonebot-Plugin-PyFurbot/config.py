import json
import os


class Config:
    ID = 0
    Token = ""
    TITLE = ""
    TITLE2 = ""
    Down = ""
    Filed = ""

    try:
        os.path.getsize("data/PyFurbot/config.json")
    except:
        os.mkdir("data/PyFurbot")
        open("data/PyFurbot/config.json", mode="w")
    finally:
        with open(file="data/PyFurbot/config.json", mode="r+", encoding="utf-8") as config:
            default = {"ID": 0, "Token": "", "TITLE": "---ヾ(≧▽≦*)o---", "TITLE2": "今天你吸毛了嘛（＾∀＾●）ﾉｼ",
                       "Down": "---ヾ(≧▽≦*)o---", "Filed": "该毛毛不存在或者未收录进绒狸毛毛数据库哟(●'◡'●)"}
            default = json.dumps(default, indent=4, separators=(',', ': '))
            if os.path.getsize("data/PyFurbot/config.json") == 0:
                config.write(default)
            else:
                config_json = json.loads(config.read())
                ID = config_json.get('ID')
                Token = config_json.get('Token')
                TITLE = config_json.get('TITLE')
                TITLE2 = config_json.get('TITLE2')
                Down = config_json.get('Down')
                Filed = config_json.get('Filed')

    class config:
        extra = "ignore"
