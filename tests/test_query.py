#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from yto.api import YTO


class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yto = YTO("sF1Jzn", "YTOTEST", "1QLlIZ",sandbox=True)

    def test_get_station_info(self):
        res = self.yto.query.get_station_info("775003")
        print(res)


if __name__ == "__main__":
    unittest.main()
