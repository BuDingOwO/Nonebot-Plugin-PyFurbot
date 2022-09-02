import hashlib


def Sign(key: str):
    key = bytes(key, encoding='utf-8')
    key = hashlib.md5(key)
    key = key.digest().hex()
    return key


def BuildSign(api_path: str, timestamp: str, authkey: str):
    keysign = api_path + "-" + timestamp + "-" + authkey
    keysign = Sign(keysign)
    return keysign


def IsNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
