import json


# 读取配置文件
def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config


def get_sender_email():
    config = load_config()
    return config.get("sender_email")


def get_receiver_email():
    config = load_config()
    return config.get("receiver_email")


def get_email_authorization_code():
    config = load_config()
    return config.get("email_authorization_code")


def get_baidu_translate_api_appid():
    config = load_config()
    return config.get("baidu_translate_api_appid")


def get_baidu_translate_api_appkey():
    config = load_config()
    return config.get("baidu_translate_api_appkey")
