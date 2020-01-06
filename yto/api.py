#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .query import Query


class YTO(object):

    def __init__(self, appkey, user_id, secret_key, format="JSON", sandbox=False):
        """
        初始化API接口
        param appkey: 分配给应用的app_key
        param user_id: 用户在开放平台注册时填写的客户标识
        param secret_key: 由开放平台分配给用户的Secret_Key，生成签名时使用
        """
        self.appkey = appkey
        self.user_id = user_id
        self.secret_key = secret_key
        self.format = format
        self.sandbox = sandbox

    comm = Comm()
    query = Query()
