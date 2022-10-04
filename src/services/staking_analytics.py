# -*- coding: utf-8 -*-

""""
    Copyright (C) 2022 ESOL LABS - All Rights Reserved.

    You may use, distribute and modify this code under the
    terms of the XYZ license, which unfortunately won't be
    written for another century.

    You should have received a copy of the XYZ license with
    this file. If not, please write to: , or visit :
"""

# File: consumer_liquidation_checking.py
# Created at May 17th, 2022
# Author: taipa

from src.config import DefaultConfig
from src.constants import AppConstants
from lib.util import dt_utcnow
from src.exceptions.stake import StakeAnalyticsEx
from src.models.staking_total import StakingTotalModel
from src.models.staking_apr import StakingAPRModel
from pydash import get
import datetime
from datetime import timezone
from src.helpers.stake import get_list_staking_contract
from src.extensions import redis_cluster


class StakingAnalyticsService(object):
    @staticmethod
    def get_apr(_type: str, _env: str):
        if _type not in AppConstants.ANALYTICS_STAKING_APR_TYPES:
            raise StakeAnalyticsEx("Invalid type of apr query")
        print(_env)
        if _type == "24h":
            _start_time = datetime.datetime(
                                    dt_utcnow().year,
                                    dt_utcnow().month,
                                    dt_utcnow().day,
                                    0,
                                    0,
                                    0
                                )
            _end_time = datetime.datetime(
                                    dt_utcnow().year,
                                    dt_utcnow().month,
                                    dt_utcnow().day,
                                    23,
                                    59,
                                    59
                                )
            _list_query = StakingAPRModel.get_list(
                filter={
                    "$and": [
                        {
                            "created_time": {
                                '$gt': _start_time
                            },
                            "env": _env
                        },
                        {
                            "created_time": {
                                '$lt': _end_time
                            },
                            "env": _env
                        }
                    ]
                }
            )
            _list_query = list(_list_query)
            _list_apr = [get(x, "apr") for x in _list_query]
        else:
            _prev_7d = (dt_utcnow() - datetime.timedelta(days=7)).replace(tzinfo=timezone.utc)
            _start_time = datetime.datetime(
                                    _prev_7d.year,
                                    _prev_7d.month,
                                    _prev_7d.day,
                                    0,
                                    0,
                                    0
                                )
            _end_time = datetime.datetime(
                                    dt_utcnow().year,
                                    dt_utcnow().month,
                                    dt_utcnow().day,
                                    23,
                                    59,
                                    59
                                )
            _list_query = StakingAPRModel.get_list(
                filter={
                    "$and": [
                        {
                            "created_time": {
                                '$gt': _start_time
                            },
                            "env": _env
                        },
                        {
                            "created_time": {
                                '$lt': _end_time
                            },
                            "env": _env
                        }
                    ]
                }
            )
            _list_query = list(_list_query)
            _list_apr = [get(x, "apr") for x in _list_query]
        if len(_list_apr) > 0:
            return sum(_list_apr) / len(_list_apr)
        return 0

    @staticmethod
    def get_total_staked(_env: str):
        _total_list = []
        print(get_list_staking_contract(_env))
        for _staking_contract_name in get_list_staking_contract(_env):
            print(_staking_contract_name)
            _staking_contract_address = redis_cluster.hget(
                name=f"vb.env_{_env}",
                key=_staking_contract_name
            )
            print(_staking_contract_address)
            if not _staking_contract_address:
                raise StakeAnalyticsEx("No staking contract address found in cluster !")

            _get_total = StakingTotalModel.get_latest_total_staked(
                filter={
                    "env": _env,
                    "staking_contract": _staking_contract_address
                }
            )
            print(_get_total)
            if _get_total:
                _total_list.append(get(_get_total, "total"))
        return sum(_total_list)
