#!/usr/bin/python3
# @Time    : 2020-01-06
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm


class Query(Comm):

    service = "newtwork_service_query"

    def get_station_info(self, Code):
        """
        根据网点ID获取该网点的详细服务信息
        param Code: 网点编号。调用根据市ID查询下属网点接口成功后，会返回Station_Code字段，该字段值就是网点编号，例如：999999(总公司)。
        """
        data = {
            "param": [{"Code": Code}]
        }
        return self.post("yto.BaseData.StationInfo", data=data)
