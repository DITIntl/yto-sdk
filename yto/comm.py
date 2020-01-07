#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime
import hashlib
import requests
from autils.datetime import DateTime

TESTURL = "http://opentestapi.yto.net.cn/service/{}/v1/wsdJFM"
URL = ""


class Comm(object):

    def __get__(self, instance, type):
        self.appkey = instance.appkey
        self.user_id = instance.user_id
        self.secret_key = instance.secret_key
        self.format = instance.format
        self.sandbox = instance.sandbox
        return self

    def _get_to_sign(self, method, time=None):
        data = {
            "user_id": self.user_id,
            "app_key": self.appkey,
            "format": self.format,
            "method": method,
            "timestamp": time if time else datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
            "v": "1.01"
        }

        return f'{self.secret_key}{"".join(f"{k}{data[k]}" for k in sorted(data.keys()))}'

    def _gen_sign(self, method, time=None):
        return hashlib.md5(self._get_to_sign(method, time=time).encode('utf-8')).hexdigest().upper()

    def post(self, method, data=None):
        """
        提交验证
        """
        url = (TESTURL if self.sandbox else URL).format(self.service)
        time = DateTime(datetime.now()).to_local_time_str()
        data.update({
            "sign": self._gen_sign(method, time=time),
            "app_key": self.appkey,
            "format": self.format,
            "method": method,
            "timestamp": time,
            "user_id": self.user_id,
            "v": "1.01"
        })
        url = f"{url}?{'&'.join(f'{k}={v}' for k,v in data.items() if v)}"
        res = requests.post(url, headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }).json()
        return res