# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.decorators import handle_res


@handle_res(login=False)
def pairs_stats(*args, **kwargs):
    return {
        "pairs": [
            {
                'oneDay': {
                    'volumeUSD': "2810580993.791174114520619173768077",
                    'reserveUSD': "31023353.36008123235725155568138271",
                },
                'sevenDay': {
                    'volumeUSD': "2776995100.196437474783662082033321",
                    'reserveUSD': "36688948.85153882279813469895922276",
                },
                'pair_address': "0xf4003f4efbe8691b60249e6afbd307abe7758adb",
                'reserveUSD': "29495193.68317102671905268661396854",
                'reserveVET': "1289218.680561543339889136",
                'volumeUSD': "2820505046.165927794817905859269533",
                'token0': {
                    'address': "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
                    'name': "Wrapped VET",
                    'symbol': "WVET"
                },
                'token1': {
                    'address': "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e",
                    'name': "USD Coin",
                    'symbol': "USDC",
                },
                'reserve0': "644609.340280771669944568",
                'reserve1': "14750515.648759",
                'token0Price': "0.0437008004079507798936395093311878",
                'token1Price': "22.88287607240400313159677567269168",
            }
        ],
        'skip': 0
    }
