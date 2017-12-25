# -*- coding: utf-8 -*-
import requests

class SMS:
    def __init__(self, l, p):
        self.login = l
        self.psw = p
        self.url = "http://smsc.ru/"

    def doRequest(self, rqData, url):
        rqData["login"] = self.login
        rqData["psw"] = self.psw
        r = requests.get(self.url + url, params=rqData)
        return r.text

    def sendSMS(self, phone, message,sender=''):
        rqData = {"phones": phone, "mes": message, "charset": "utf-8"}
        if sender != "":
            rqData['sender'] = sender
        return self.doRequest(rqData, "sys/send.php")

