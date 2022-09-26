# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import request
from pydash import get

from lib.decorators import handle_res
from src.helpers.pool_pricing import PoolPricing
from src.services.pairs import PairService
from datetime import datetime


@handle_res(login=False)
def pairs_stats(*args, **kwargs):
    _query = request.args.to_dict()

    _page = int(get(_query, 'page', default=1))
    _limit = int(get(_query, 'limit', default=10))

    _offset = _page > 0 and (_page - 1) * _limit or 0

    _pairs = PairService.get_all_pairs(_offset, _limit)
    _pairs_list = []

    if not _pairs:
        print("go here")
        return {
            "pairs": _pairs_list,
            "skip": 0
        }

    current_date = datetime.utcnow()
    day = current_date.day
    week = current_date.isocalendar()[1]
    month = current_date.month
    year = current_date.year

    for _, _pair in enumerate(_pairs):
        _token0_info = get(_pair, 'token0')
        _token1_info = get(_pair, 'token1')

        _token0_decimals = 10 ** int(_token0_info['decimals'])
        _token1_decimals = 10 ** int(_token1_info['decimals'])

        _reserve0 = int(_pair['reserve0']) / _token0_decimals
        _reserve1 = int(_pair['reserve1']) / _token1_decimals

        _token0_usd_price = PoolPricing.get_usd_rate(PoolPricing, token=_pair['token0_address'])
        _token1_usd_price = PoolPricing.get_usd_rate(PoolPricing, token=_pair['token1_address'])

        _token1_price = _reserve1 / _reserve0
        _token0_price = _reserve0 / _reserve1

        _reserve_usd = _reserve0 * _token0_usd_price + _reserve1 * _token1_usd_price

        _one_day_data = PairService.get_one_day_data(
            factory_address=_pair['factory_address'],
            pair_address=_pair['pair_address'],
            day=day,
            month=month,
            year=year,
            token0_decimals=_token0_decimals,
            token1_decimals=_token1_decimals,
            token0_usd=_token0_usd_price,
            token1_usd=_token0_usd_price
        )

        _seven_day_data = PairService.get_seven_day_data(
            factory_address=_pair['factory_address'],
            pair_address=_pair['pair_address'],
            week=week,
            year=year,
            token0_decimals=_token0_decimals,
            token1_decimals=_token1_decimals,
            token0_usd=_token0_usd_price,
            token1_usd=_token0_usd_price
        )

        _summary_data = PairService.get_summary_data(
            factory_address=_pair['factory_address'],
            pair_address=_pair['pair_address'],
            token0_decimals=_token0_decimals,
            token1_decimals=_token1_decimals,
            token0_usd=_token0_usd_price,
            token1_usd=_token0_usd_price
        )

        _pair_data = {
            'pair_address': _pair['pair_address'],
            'reserve_usd': f'{_reserve_usd:.28f}',
            'one_day': _one_day_data,
            'seven_day': _seven_day_data,
            'summary_data': _summary_data,
            'token0': _token0_info,
            'token1': _token1_info,
            'token0_price': f'{_token0_price:.{_token0_info["decimals"]}f}',
            'token1_price': f'{_token1_price:.{_token1_info["decimals"]}f}',
            'reserve0': f'{_reserve0:.{_token0_info["decimals"]}f}',
            'reserve1': f'{_reserve1:.{_token1_info["decimals"]}f}',
        }

        _pairs_list.append(_pair_data)

    return {
        "pairs": _pairs_list,
        'skip': _offset
    }
