from decimal import Decimal

from src.config import DefaultConfig
from src.models.pair import PairModel, PoolDayDataModel, PoolMonthDataModel, PoolSummaryModel, PoolWeekDataModel


class PairService(object):

    @staticmethod
    def get_pair_info_by_address(pair_address):
        _pair = PairModel.db().find_one(filter={
            'pair_address': pair_address
        })

        return _pair

    @staticmethod
    def get_pair_address(token0_address, token1_address):
        _pair = PairModel.db().find_one(filter={
            'factory_address': DefaultConfig.POOL_DEX_FACTORY_CONTRACT,
            '$or': [
                {
                    'token0_address': token0_address,
                    'token1_address': token1_address
                },
                {
                    'token0_address': token1_address,
                    'token1_address': token0_address
                }
            ]
        })
        if _pair is None:
            return DefaultConfig.ADDRESS_ZERO

        return _pair['pair_address']

    @staticmethod
    def get_pair_info_by_token(token0_address, token1_address):
        _pair = PairModel.db().find_one(filter={
            'factory_address': DefaultConfig.POOL_DEX_FACTORY_CONTRACT,
            '$or': [
                {
                    'token0_address': token0_address,
                    'token1_address': token1_address
                },
                {
                    'token0_address': token1_address,
                    'token1_address': token0_address
                }
            ]
        })

        return _pair

    @staticmethod
    def get_all_pairs(offset, limit):
        _pairs = PairModel.db().aggregate([
            {
                "$match": {
                    'factory_address': DefaultConfig.POOL_DEX_FACTORY_CONTRACT
                }
            },
            {
                "$sort": {
                    "priority": -1
                }
            },
            {
                '$skip': offset
            },
            {
                '$limit': limit
            }
        ])

        if _pairs is None:
            return []

        return _pairs
    
    @staticmethod
    def get_one_day_data(
            factory_address,
            pair_address,
            day,
            month,
            year,
            token0_decimals,
            token1_decimals,
            token0_usd,
            token1_usd
    ):
        _day_data = PoolDayDataModel.db().find_one({
            'day': day,
            'month': month,
            'year': year,
            'factory_address': factory_address,
            'pair_address': pair_address,
        })

        if _day_data is None:
            return {
                'volume_one_day': '0',
                'fee_one_day': '0'
            }

        token0_volume_usd = Decimal(_day_data['volume_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_volume_usd = Decimal(_day_data['volume_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        token0_fee_usd = Decimal(_day_data['fee_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_fee_usd = Decimal(_day_data['fee_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        total_volume_usd = token0_volume_usd + token1_volume_usd
        total_fee_usd = token0_fee_usd + token1_fee_usd

        return {
            'volume_one_day': f'{total_volume_usd:.28f}',
            'fee_one_day': f'{total_fee_usd:.28f}'
        }

    @staticmethod
    def get_seven_day_data(
            factory_address,
            pair_address,
            week,
            year,
            token0_decimals,
            token1_decimals,
            token0_usd,
            token1_usd
    ):
        _week_data = PoolWeekDataModel.db().find_one({
            'week': week,
            'year': year,
            'factory_address': factory_address,
            'pair_address': pair_address,
        })

        if _week_data is None:
            return {
                'volume_seven_day': '0',
                'fee_seven_day': '0'
            }

        token0_volume_usd = Decimal(_week_data['volume_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_volume_usd = Decimal(_week_data['volume_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        token0_fee_usd = Decimal(_week_data['fee_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_fee_usd = Decimal(_week_data['fee_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        total_volume_usd = token0_volume_usd + token1_volume_usd
        total_fee_usd = token0_fee_usd + token1_fee_usd

        return {
            'volume_seven_day': f'{total_volume_usd:.28f}',
            'fee_seven_day': f'{total_fee_usd:.28f}'
        }

    @staticmethod
    def get_summary_data(
            factory_address,
            pair_address,
            token0_decimals,
            token1_decimals,
            token0_usd,
            token1_usd
    ):
        _summary_data = PoolWeekDataModel.db().find_one({
            'factory_address': factory_address,
            'pair_address': pair_address,
        })

        if _summary_data is None:
            return {
                'total_volume': '0',
                'total_fee': '0'
            }

        token0_volume_usd = Decimal(_summary_data['volume_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_volume_usd = Decimal(_summary_data['volume_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        token0_fee_usd = Decimal(_summary_data['fee_token0']) / Decimal(token0_decimals) * Decimal(token0_usd)
        token1_fee_usd = Decimal(_summary_data['fee_token1']) / Decimal(token1_decimals) * Decimal(token1_usd)

        total_volume_usd = token0_volume_usd + token1_volume_usd
        total_fee_usd = token0_fee_usd + token1_fee_usd

        return {
            'total_volume': f'{total_volume_usd:.28f}',
            'total_fee': f'{total_fee_usd:.28f}'
        }
