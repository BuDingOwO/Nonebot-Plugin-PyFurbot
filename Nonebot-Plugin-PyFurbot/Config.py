import json
import os


class Config:
    try:
        os.path.getsize("config.json")
    except:
        open("config.json", mode="w")
    with open(file="config.json", mode="r+", encoding="utf-8") as config:
        default = {"QQ": "", "Token": ""}
        default = json.dumps(default, indent=4, separators=(',', ': '))
        if os.path.getsize("config.json") == 0:
            config.write(default)
        else:
            config_json = json.loads(config.read())
            QQ = config_json['QQ']
            Token = config_json['Token']
