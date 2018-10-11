# Author:zylong
#新浪微博用户 ：用户token：
import requests
from sinarequestheaders import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
import time
import ymapirequest
import json


options = Options()
# options.add_argument("-headless")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
browser.get("https://weibo.com")
wait = WebDriverWait(browser,20)

def login(mobile):
    login_a_button = wait.until(
        ec.presence_of_element_located((by.CSS_SELECTOR,"#pl_login_form > div > div.info_header > a"))
    )
    login_a_button.click()

    mobile_input = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(4) > div.info_list.phone > div > input")
        )
    )
    mobile_input.send_keys(mobile)
    get_mobile_code = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(4) > div.info_list.msgInfo.clearfix > a:nth-child(2)")
        )
    )
    get_mobile_code.click()
    code_input = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(4) > div.info_list.msgInfo.clearfix > div > input")
        )
    )
    #再此等待短信验证码
    code = ymapi.getMobileCode()

    code_input.send_keys(code)

    login_click=wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#pl_login_form > div > div:nth-child(4) > div.info_list.login_btn > a > span")
        )
    )
    login_click.click()
    time.sleep(3)

    # cookies = browser.get_cookies()

    cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]

    print(cookie)

    cookiestr = ';'.join(item for item in cookie)
    with open('aa','w+') as f:
        f.write("mobile"+mobile+":"+cookiestr+"\n")
    return cookiestr


# def cookiesLogin(cookie):
#     headers["cookie"] = cookie
#     response = requests.get("https://weibo.com/",headers=headers)
#     print(response.text)

def guanzhuSGY():
    input_select_name = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#plc_top > div > div > div.gn_search_v2 > input")
        )
    )
    input_select_name.send_keys("上官_延")

    select_name = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#plc_top > div > div > div.gn_search_v2 > a")
        )
    )
    select_name.click()
    time.sleep(3)
    userButton = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#pl_feed_main > div.m-wrap > div.m-con-r > div:nth-child(1) > div > div.card-content.s-pg12 > div > div.info > div > a")
        )
    )
    userButton.click()
    time.sleep(3)
    guanzhuButton = wait.until(
        ec.presence_of_element_located(
            (by.CSS_SELECTOR,"#Pl_Official_Headerv6__1 > div.PCD_header > div > div.shadow.S_shadow > div.pf_opt > div > div:nth-child(1) > a:nth-child(1)")
        )
    )
    guanzhuButton.click()


import operator
def isExit(mobile):
    # register_button = wait.until(
    #     ec.presence_of_element_located(
    #         (by.CSS_SELECTOR,"#weibo_top_public > div > div > div.gn_position > div.gn_login > ul > li:nth-child(1) > a")
    #     )
    # )
    # register_button.click()
    # time.sleep(3)
    # mobile_input = wait.until(
    #     ec.presence_of_element_located(
    #         (by.CSS_SELECTOR,"#pl_account_regmobile > div.W_reg_form > div:nth-child(1) > div.inp > div.flag_tel.clearfix > div > input")
    #     )
    # )
    # mobile_input.send_keys(mobile)
    t = str(round(time.time()))

    response = requests.get("https://weibo.com/signup/v5/formcheck?type=mobilesea"
                            "&zone=0086&value="+mobile+"&from=&__rnd="+t,headers=headers)
    # print(response.text)
    result = json.loads(response.text)
    code = result.get("code")
    if operator.eq(code,"100000"):
        #未注册
        return True
    else:
        #已注册
        return False
        # cookies = login(mobile)

ymapi = ymapirequest.ymapi()
if __name__ == '__main__':
    # ymapi.mobile = '13635853223'
    # ymapi.getMobileCode()
    mobile = ymapi.getMObile()
    # 判断号码是否注册
    # mobile = '15071712524'
    result = isExit(mobile)
    if not result:
        login(mobile)
    #
    guanzhuSGY()


