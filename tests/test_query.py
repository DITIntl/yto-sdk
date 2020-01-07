#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from yto.api import YTO


class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.yto = YTO("sF1Jzn", "YTOTEST", "1QLlIZ", sandbox=True)

    def test_get_station_info(self):
        res = self.yto.query.get_station_info("775003")
        self.assertTrue(res["Station_Code"], res)

    def test_get_trace_route(self):
        res = self.yto.query.get_package_route("1111111111")
        self.assertEqual(res[0]["Waybill_No"], "1111111111", res)

    def test_get_charge_price(self):
        res = self.yto.query.get_charge_price(
            "甘肃省", "金昌市", "湖南省", "湘西土家族苗族自治州", 0.5)
        self.assertEqual(res, 18, res)

    def test_get_city_by_state(self):
        res = self.yto.query.get_city_by_state("2330102")
        self.assertGreater(len(res), 0, res)


if __name__ == "__main__":
    unittest.main()
