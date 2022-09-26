from pydash import get

from src.config import DefaultConfig
from src.services.pairs import PairService


class PoolPricing(object):
    """
        Base VB price using VB/VET * VET.
    """

    @staticmethod
    def get_vb_price(cls):
        # vet_rate = cls.get_vet_rate(cls, token=DefaultConfig.VB_ADDRESS)
        # vet_price = cls.get_vet_price(cls)
        # return vet_rate * vet_price

        pair_address = PairService.get_pair_address(DefaultConfig.VB_ADDRESS, DefaultConfig.VEUSD_ADDRESS)

        if pair_address == DefaultConfig.ADDRESS_ZERO:
            vet_rate = cls.get_vet_rate(cls, token=DefaultConfig.VB_ADDRESS)
            vet_price = cls.get_vet_price(cls)
            return vet_rate * vet_price

        _pair_info = PairService.get_pair_info_by_address(pair_address=pair_address)
        token0 = _pair_info['token0_address']
        reserve0 = int(_pair_info['reserve0'])
        reserve1 = int(_pair_info['reserve1'])

        if token0 == DefaultConfig.VB_ADDRESS:
            if reserve0 == DefaultConfig.BIG_DECIMAL_ZERO:
                return DefaultConfig.BIG_DECIMAL_ZERO
            return (reserve1 / DefaultConfig.BIG_DECIMAL_1E6) / (reserve0 / DefaultConfig.BIG_DECIMAL_1E18)

        if reserve1 == DefaultConfig.BIG_DECIMAL_ZERO:
            return DefaultConfig.BIG_DECIMAL_ZERO
        return (reserve0 / DefaultConfig.BIG_DECIMAL_1E6) / (reserve1 / DefaultConfig.BIG_DECIMAL_1E18)

    """
        Bundle tracks the price of VET, it is used to convert from VET price to USD price.
        Exchange subgraph only keeps 1 bundle; it is updated during factory sync() event.

        This is different from get_vet_rate which calculates VET price for token, as it only
        calculates price in USD for VET.

        VET price is calculated by getting weighted average of stable-coin pairs.
    """

    @staticmethod
    def get_vet_price(cls):
        pair_address = PairService.get_pair_address(DefaultConfig.VVET_ADDRESS, DefaultConfig.VEUSD_ADDRESS)
        price = cls._get_vet_price(pair_address)
        # weight = cls._get_vet_reserve(pair_address)
        #
        # if weight == DefaultConfig.BIG_DECIMAL_ZERO:
        #     return DefaultConfig.BIG_DECIMAL_ZERO
        return price

    @staticmethod
    def _get_vet_price(pair_address):
        if pair_address == DefaultConfig.ADDRESS_ZERO or pair_address is None:
            return DefaultConfig.BIG_DECIMAL_ZERO

        _pair_info = PairService.get_pair_info_by_address(pair_address=pair_address)
        token0 = _pair_info['token0_address']
        reserve0 = int(_pair_info['reserve0'])
        reserve1 = int(_pair_info['reserve1'])

        if token0 == DefaultConfig.VVET_ADDRESS:
            if reserve0 == DefaultConfig.BIG_DECIMAL_ZERO:
                return DefaultConfig.BIG_DECIMAL_ZERO
            return (reserve1 / DefaultConfig.BIG_DECIMAL_1E6) / (reserve0 / DefaultConfig.BIG_DECIMAL_1E18)

        if reserve1 == DefaultConfig.BIG_DECIMAL_ZERO:
            return DefaultConfig.BIG_DECIMAL_ZERO
        return (reserve0 / DefaultConfig.BIG_DECIMAL_1E6) / (reserve1 / DefaultConfig.BIG_DECIMAL_1E18)

    @staticmethod
    def _get_vet_reserve(pair_address):
        if pair_address == DefaultConfig.ADDRESS_ZERO or pair_address is None:
            return DefaultConfig.BIG_DECIMAL_ZERO

        _pair_info = PairService.get_pair_info_by_address(pair_address=pair_address)
        token0 = _pair_info['token0_address']
        reserve0 = int(_pair_info['reserve0'])
        reserve1 = int(_pair_info['reserve1'])

        if token0 == DefaultConfig.VVET_ADDRESS:
            return reserve0 / DefaultConfig.BIG_DECIMAL_1E18
        return reserve1 / DefaultConfig.BIG_DECIMAL_1E18

    """
        @param token: address of token

        Get price of token in VET.
    """

    @staticmethod
    def get_vet_rate(cls, token):
        if token == DefaultConfig.VVET_ADDRESS:
            return DefaultConfig.BIG_DECIMAL_ONE

        for whitelist_token in DefaultConfig.WHITELIST:
            _pair_info = PairService.get_pair_info_by_token(token0_address=token, token1_address=whitelist_token)
            _pair_address = get(_pair_info, 'pair_address', DefaultConfig.ADDRESS_ZERO)

            if _pair_address != DefaultConfig.ADDRESS_ZERO:
                token0 = _pair_info['token0_address']
                token1 = _pair_info['token1_address']

                if token1 == DefaultConfig.VEUSD_ADDRESS or token0 == DefaultConfig.VEUSD_ADDRESS:
                    if token1 == DefaultConfig.VEUSD_ADDRESS:
                        reserve0 = int(_pair_info['reserve0']) / DefaultConfig.BIG_DECIMAL_1E18
                        reserve1 = int(_pair_info['reserve1']) / DefaultConfig.BIG_DECIMAL_1E6
                    else:
                        reserve0 = int(_pair_info['reserve0']) / DefaultConfig.BIG_DECIMAL_1E6
                        reserve1 = int(_pair_info['reserve1']) / DefaultConfig.BIG_DECIMAL_1E18
                else:
                    reserve0 = int(_pair_info['reserve0'])
                    reserve1 = int(_pair_info['reserve1'])

                if reserve0 != DefaultConfig.BIG_DECIMAL_ZERO:
                    token1_price = reserve1 / reserve0
                else:
                    token1_price = DefaultConfig.BIG_DECIMAL_ZERO

                if reserve1 != DefaultConfig.BIG_DECIMAL_ZERO:
                    token0_price = reserve0 / reserve1
                else:
                    token0_price = DefaultConfig.BIG_DECIMAL_ZERO

                if token0 == token:
                    return token1_price * cls.get_vet_rate(cls, token=token1)

                if token1 == token:
                    return token0_price * cls.get_vet_rate(cls, token=token0)

        return DefaultConfig.BIG_DECIMAL_ZERO

    """
        @param token: address of token
    """

    @staticmethod
    def get_usd_rate(cls, token):
        if token == DefaultConfig.VEUSD_ADDRESS:
            return DefaultConfig.BIG_DECIMAL_ONE

        if token == DefaultConfig.VB_ADDRESS:
            return cls.get_vb_price(cls)

        if token == DefaultConfig.VVET_ADDRESS:
            return cls.get_vet_price(cls)

        vet_rate = cls.get_vet_rate(cls, token=token)
        vet_price = cls.get_vet_price(cls)

        return vet_rate * vet_price
