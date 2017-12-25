# -*- coding: utf-8 -*-
import requests
import hashlib
import re

class SMS:
    def __init__(self, l, p):
        self.login = l
        self.psw = p
        self.url = "http://smsc.ru/"

    def doRequest(self, rqData, url):
        rqData["login"] = self.login
        psw = self.psw
        m = hashlib.md5()
        m.update(psw.encode('utf-8'))
        rqData["psw"] = m.hexdigest()
        r = requests.get(self.url + url, params=rqData)
        return r.text

    def sendSMS(self, phone, message,sender=''):
        if re.match(r'7[0-9]{10}', phone) and len(phone)==11:
            rqData = {"phones": phone, "mes": message, "charset": "utf-8"}
            if sender != "":
                rqData['sender'] = sender
            return self.doRequest(rqData, "sys/send.php")
        else:
            return "Wrong type Number"

    def balance(self):
        rqData = {}
        return self.doRequest(rqData, "sys/balance.php")

