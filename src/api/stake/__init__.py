# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint
from .controller import *

rest_stake = Blueprint('rest_stake', __name__, url_prefix='stake')
rest_stake.add_url_rule('/apr', view_func=get_apr, methods=['GET'])
rest_stake.add_url_rule('/total_staked', view_func=get_total_staked, methods=['GET'])

