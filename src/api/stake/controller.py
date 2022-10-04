# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.decorators import handle_res
from src.services.staking_analytics import StakingAnalyticsService
from src.schemas.staking_apr import GetAprParams
from src.schemas.staking_total import GetTotalParams
from pydash import get


@handle_res(login=False, param_schema=GetAprParams)
def get_apr(params, *args, **kwargs):
    _type = get(params, "type")
    _env = get(params, "env")
    return {
        "APR": StakingAnalyticsService.get_apr(
            _type=_type,
            _env=_env
        ),
        "type": _type
    }


@handle_res(login=False, param_schema=GetTotalParams)
def get_total_staked(params, *args, **kwargs):
    _env = get(params, "env")
    return {
        "Total Staked": StakingAnalyticsService.get_total_staked(_env)
    }
