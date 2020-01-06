#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from yto.api import YTO


class TestComm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yto = YTO("ABCDEF", "yto_user", "123456", format="XML")

    def test_to_sign(self):
        res = self.yto.comm._get_to_sign(
            "yto.Marketing.WaybillTrace", time="2016-6-1 13:14:35")
        self.assertEqual(
            res, "123456app_keyABCDEFformatXMLmethodyto.Marketing.WaybillTracetimestamp2016-6-1 13:14:35user_idyto_userv1.01", res)

    def test_sign(self):
        res = self.yto.comm._gen_sign("yto.Marketing.WaybillTrace","2016-6-1 13:14:35")
        self.assertEqual(res, "B78455F451153FA1284B186D5C4E31DF", res)


if __name__ == "__main__":
    unittest.main()
