import hashlib


def sign(key: str):
    key = bytes(key, encoding='utf-8')
    key = hashlib.md5(key)
    key = key.digest().hex()
    return key


def getsign(api_path: str, timestamp: str, authkey: str):
    keysign = api_path + "-" + timestamp + "-" + authkey
    keysign = sign(keysign)
    return keysign
