#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm


class Query(Comm):

    def get_station_info(self, Code):
        """
        根据网点ID获取该网点的详细服务信息
        param Code: 网点编号。调用根据市ID查询下属网点接口成功后，会返回Station_Code字段，该字段值就是网点编号，例如：999999(总公司)。
        """
        data = {
            "param": [{"Code": Code}]
        }
        self.service = "newtwork_service_query"
        return self.post("yto.BaseData.StationInfo", data=data)

    def get_package_route(self, Number):
        """
        获取快递物流信息
        """
        data = {
            "param": [{"Number": Number}]
        }
        self.service = "waybill_query"
        return self.post("yto.Marketing.WaybillTrace", data=data)

    def get_charge_price(self, from_state, from_city, dest_state, dest_city, weight, length=0, width=0, height=0):
        """
        获取运单价格查询
        param from_state: 发件省份
        param from_city: 发件城市
        param dest_state: 到达省份
        param dest_state: 到达城市
        param weight: 重量
        param length: 长度
        param width: 宽度
        param height: 高
        return ：运费
        """
        data = {
            "param": [{
                "StartProvince": from_state,
                "StartCity": from_city,
                "EndProvince": dest_state,
                "EndCity": dest_city,
                "GoodsWeight": weight,
                "GoodsLength": length,
                "GoodsWidth": width,
                "GoodsHeight": height
            }]
        }
        self.service = "charge_query"
        return self.post("yto.Marketing.TransportPrice", data=data)

    def get_city_by_state(self, code):
        """
        根据省ID查询市接口
        param code: 省ID
        2110101-北京市;
        2310101-上海市;
        2120101-天津市;
        2500101-重庆市;
        2330102-浙江省;
        2320102-江苏省;
        2340102-安徽省;
        2440103-广东省;
        2350102-福建省;
        2140121-江西省;
        2370102-山东省;
        2130102-河北省;
        2410102-河南省;
        2420102-湖北省;
        2430482-湖南省;
        2140121-山西省;
        2610102-陕西省;
        2210102-辽宁省;
        2220102-吉林省;
        2230102-黑龙江省;
        2450102-广西壮族自治区;
        2510104-四川省;
        2520102-贵州省;
        2460105-海南省;
        2530102-云南省;
        2630102-青海省;
        2620421-甘肃省;
        2640104-宁夏回族自治区;
        2150102-内蒙古自治区;
        2650102-新疆维吾尔自治区;
        2540102-西藏自治区;
        8a8142c3324990c7013266ba4f9e5030-港澳。
        """
        self.service = "subcity_query"
        data = {
            "param": [{
                "Code": code
            }]
        }
        return self.post("yto.BaseData.ProvinceOfCity", data=data)

    def get_network_by_city(self, code):
        """
        根据市ID查询下属网点接口
        param code: 市ID。
        调用根据省ID查询市接口成功后，会返回Id字段，该字段值就是市ID
        """
        self.service = "subnetwork_query"
        data = {
            "param": [{
                "Code": code
            }]
        }
        return self.post("yto.BaseData.CityOfStation", data=data)
