# -*- encoding: utf-8 -*-
"""
PyCharm 1
2024年02月13日
by Slin
"""
import logging
import requests
import json
logging.captureWarnings(True)
session = requests.session()

username='19854062326'
password='5211314666'
schoolid=1
key = (username + "0000000000000000")[:16]
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
#proxies = { "http": "http://127.0.0.1:9099", "https": "http://127.0.0.1:9099", }
def encrypt(t, e):
    key = e.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(t.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return b64encode(encrypted_text).decode('utf-8')

encrypted_text = encrypt(password, key)
print("加密密码:", encrypted_text)

url0="https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
params0={
    "schoolID":schoolid,
    "password":encrypted_text,
    "username":username
}
data0={}
headers0={"accept":"aplication/json,text/plain,*/*",
          "user-agent":"Mozilla/5.0 (Linux; Android 10; LIO-AN00 Build/HUAWEILIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1170 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/3371 MicroMessenger/7.0.12.1620(0x27000C36) Process/toolsmp NetType/4G Language/zh_CN ABI/arm64"
          }
reaponse0=session.post(url0,params=params0,headers=headers0,verify=False)
url1="https://gw.wozaixiaoyuan.com/sign/mobile/receive/getMySignLogs"
res0=session.get(url=url1,headers=headers0,verify=False).json()
type=res0["data"][0]["type"]
a=res0["data"][0]
id=res0["data"][0]["id"]
signId=res0["data"][0]["signId"]
signTitle=res0["data"][0]["signTitle"]
signContext=res0["data"][0]["signContext"]
params1={
    "id": id,
    "schoolId":schoolid,
    "signId":signId,

}
print(params1)
data0={
    "inArea": 1,
    "areaJSON":"{\"id\":\"664212671557669112\",\"name\":\"西安邮电大学\"}",
    "latitude": 34.149944390190974,
    "longitude": 108.90250108506945
}
print(data0)
url2="https://gw.wozaixiaoyuan.com/sign/mobile/receive/doSignByLocation"
res1=session.post(url2,params=params1,data=json.dumps(data0),headers=headers0,verify=False)
print(res1.text)
