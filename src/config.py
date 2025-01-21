import json


# 读取配置文件
def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config


# 获取 sender_email 参数
def get_sender_email():
    config = load_config()
    return config.get("sender_email")


# 获取 receiver_email 参数
def get_receiver_email():
    config = load_config()
    return config.get("receiver_email")


# 获取 email_authorization_code 参数
def get_email_authorization_code():
    config = load_config()
    return config.get("email_authorization_code")


# 获取 baidu_translate_api_appid 参数
def get_baidu_translate_api_appid():
    config = load_config()
    return config.get("baidu_translate_api_appid")


# 获取 baidu_translate_api_appkey 参数
def get_baidu_translate_api_appkey():
    config = load_config()
    return config.get("baidu_translate_api_appkey")
