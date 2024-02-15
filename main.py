# -*- encoding: utf-8 -*-
"""
PyCharm 1
2024年02月13日
by Slin
"""
import logging
import requests
import json
from pushplus import send_message
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import os

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
token = os.environ.get("TOKEN")
key = (str(username) + "0000000000000000")[:16]
logging.captureWarnings(True)
session = requests.session()


# proxies = { "http": "http://127.0.0.1:9099", "https": "http://127.0.0.1:9099", }
def encrypt(t, e):
    key = e.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(t.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return b64encode(encrypted_text).decode('utf-8')


encrypted_text = encrypt(password, key)
print("加密密码:", encrypted_text)

url0 = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
params0 = {
    "schoolID": 1,
    "password": encrypted_text,
    "username": username
}
headers0 = {"accept": "aplication/json,text/plain,*/*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; LIO-AN00 Build/HUAWEILIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1170 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/3371 MicroMessenger/7.0.12.1620(0x27000C36) Process/toolsmp NetType/4G Language/zh_CN ABI/arm64"
            }
reaponse0 = session.post(url0, params=params0, headers=headers0, verify=False)
url1 = "https://gw.wozaixiaoyuan.com/sign/mobile/receive/getMySignLogs"
res0 = session.get(url=url1, headers=headers0, verify=False).json()
type = res0["data"][0]["type"]

id = res0["data"][0]["id"]
signId = res0["data"][0]["signId"]
signTitle = res0["data"][0]["signTitle"]
signContext = res0["data"][0]["signContext"]
createName = res0["data"][0]["createName"]
params1 = {
    "id": id,
    "schoolId": 1,
    "signId": signId,

}
print(params1)
area = "{{\"id\":\"{}\",\"name\":\"西安邮电大学\"}}".format(id)
print(area)
data0 = {
    "inArea": 1,
    "areaJSON": area,
    "latitude": 34.149944390190974,
    "longitude": 108.90250108506945
}
print(data0)

text0=""

def sign():
    global text0
    url2 = "https://gw.wozaixiaoyuan.com/sign/mobile/receive/doSignByLocation"
    res1 = session.post(url2, params=params1, data=json.dumps(data0), headers=headers0, verify=False)
    return res1.text
def send():
    response_text = send_message(
        token,
        "我在校园签到推送",
        sign_info
    )







if res0["data"][0]["type"] == 1:
    a=sign()
    sign_info = (
        f"{signTitle}\n"
        f"------\n"
        f"{signContext}\n"
        f"------\n"
        f"{createName}\n"
        f"------\n"
        f"{a}\n"
    )
    send()