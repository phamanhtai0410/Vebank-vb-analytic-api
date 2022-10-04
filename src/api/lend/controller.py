# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import datetime as dt

from flask import request
from pydash import get
from lib.decorators import handle_res
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from src.services.lend import LendService
from src.config import DefaultConfig


@handle_res(login=False)
def lend_stats(*args, **kwargs):
    _query = request.args.to_dict()

    _page = int(get(_query, 'page', default=1))
    _limit = int(get(_query, 'limit', default=10))

    _offset = _page > 0 and (_page - 1) * _limit or 0

    _assets = DefaultConfig.LIST_ASSETS
    _assets_list = []

    current_date = datetime.utcnow()
    day = current_date.day
    week_ago = datetime.now() - timedelta(days=7)
    today_date = datetime.today()
    one_month_ago = today_date - relativedelta(months=1)
    print("one_month_ago ", one_month_ago)
    month = one_month_ago.date()
    year = current_date.year
    _res = []
    for _asset in _assets:
        _one_day_data = LendService.get_one_day_data(
            asset=_asset,
        )
        _one_week_data = LendService.get_summary_data(
            asset=_asset,
            from_day=week_ago
        )
        _one_month = LendService.get_summary_data(
            asset=_asset,
            from_day=one_month_ago
        )
        _summary = LendService.get_summary_data(
            asset=_asset,
            from_day=one_month_ago,
            get_all=True
        )
        _asset_data = {
            "asset": _asset,
            "asset_name": DefaultConfig.ASSETS_NAME[_asset],
            "one_day": _one_day_data,
            "seven_day": _one_week_data,
            "one_month": _one_month,
            "summary": _summary
        }
        _res.append(_asset_data)
       
    return {
        "lending": _res,
        "liquidate": [{"asset": "0x033bbc923a9378600c6b52fa9aada608c4cc7ece", "amount": "23232222", "created_time": "2022-10-04 08:05:08"}],
    }