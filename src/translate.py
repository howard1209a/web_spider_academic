import requests
import random
from hashlib import md5
import config

baidu_translate_api_appid = config.get_baidu_translate_api_appid()
baidu_translate_api_appkey = config.get_baidu_translate_api_appkey()

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'en'
to_lang = 'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def baidu_api(query):
    salt = random.randint(32768, 65536)
    sign = make_md5(baidu_translate_api_appid + query + str(salt) + baidu_translate_api_appkey)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': baidu_translate_api_appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt,
               'sign': sign}

    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    return result["trans_result"][0]['dst']
