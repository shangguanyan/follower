# Author:zylong
import requests
from setting import *

def getYMToken():
    login_ym_url = YM_LOGIN_URL.format(**YM_USER)
    response = requests.get(login_ym_url)
    if response.status_code == 200:
        content = response.text
        token = content.split("|")[1]
        return token

def getJMToken():
    login_ym_url = YM_LOGIN_URL.format(**YM_USER)
    response = requests.get(login_ym_url)
    print(response)
    if response.status_code == 200:
        content = response.text
        print(content)
        return content

if __name__ == '__main__':
    token = getJMToken()