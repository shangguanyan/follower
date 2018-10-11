# Author:zylong
from setting import *
import requests
import time,re
class ymapi():
    token = YM_TOKEN
    itemid = "35"
    action = ""
    url = "http://api.fxhyd.cn/UserInterface.aspx?action={action}&token={token}"
    # mobile = '15071712524'
    mobile = ""
    code_content = ""

    def getMObile(self):
        self.action = "getmobile"
        mobile_url = self.url.format(action=self.action,token=self.token)+"&itemid="+self.itemid
        response = requests.get(mobile_url)
        if response.status_code == 200:
            mobile = response.text.split("|")[1]
            self.mobile = mobile
            return mobile

    def getMobileCode(self):
        time.sleep(3)
        self.action = "getsms"
        code_url = self.url.format(action=self.action,token=self.token)+\
                   "&itemid="+self.itemid+"&mobile="+self.mobile+"&release=1"
        response = requests.get(code_url)
        response.encoding="utf-8"
        status_code = response.status_code
        content = response.text
        if status_code == 200 and "success" in content:
            # code_content = content.split("!")[1]
            # code = 'success|【微博】验证码：945943。此验证码只用于校验身份以登录微博，10分钟内有效。'
            # mobilet_code = re.findall('\d+', code)[0]
            print(content)
            return re.findall('\d+', content)[0]
        else:
            time.sleep(2)
            return self.getMobileCode()


# if __name__ == '__main__':
#     code = 'success|【微博】验证码：945943。此验证码只用于校验身份以登录微博，10分钟内有效。'
#
#     print(re.findall("\d+",code)[0])