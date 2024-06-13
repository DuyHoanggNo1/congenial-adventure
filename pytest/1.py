import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
sdt = '0399962319'
headers = {
    'Host': 'api.ahamove.com',
    'User-Agent': 'Android/25 AhaMove_User/300106 asus/ASUS_Z01QD',
    'Accepts-Version': '2',
    'Authorization': 'Bearer null',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Content-Length': '101',
    # 'Accept-Encoding': 'gzip, deflate',
}

params = {
    'lang': 'vi',
}

json_data = {
    'country_code': 'VN',
    'firebase_sms_auth': False,
    'mobile': sdt,
    'resend': True,
    'type': 'android',
}

response = requests.post(
    'https://api.ahamove.com/api/v3/public/user/login',
    params=params,
    headers=headers,
    json=json_data,
    verify=False,
)

print(response.text)