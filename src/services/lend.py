from decimal import Decimal
from datetime import datetime
from src.config import DefaultConfig
from src.models.lend import *


class LendService(object):
    @staticmethod
    def get_one_day_data(
        asset
    ):
        _day_data = LendingHourDataModel.db().find_one({
                "asset": asset
            }, sort=[('_id', -1)]
        )
        
        if _day_data is None:
            return {
                "total_aToken": "0",
                "total_debt_token": "0"
            }

        return {
            "total_aToken": _day_data["total_aToken"],
            "total_debt_token": _day_data["total_debt"],
            "created_time": _day_data["created_time"].strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def get_summary_data(asset, from_day, get_all=False):
        res = []
        if get_all:
            _query_data = LendingDayDataModel.db().find({
                "asset": asset
        }, sort=[('created_time', 1)])
        else:
            _query_data = LendingDayDataModel.db().find({
                "asset": asset,
                "created_time": {"$gt": from_day},
            }, sort=[('created_time', 1)])
        for _day in _query_data:
            _res_data = {
                "total_aToken": _day["total_aToken"],
                "total_debt_token": _day["total_debt"],
                "created_time": _day["created_time"].strftime("%Y-%m-%d %H:%M:%S")
            }
            if _query_data is None:
                return _res_data
    
            res.append(_res_data)
        return res

    