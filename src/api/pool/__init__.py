# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint

from .controller import *

rest_pool = Blueprint('rest_pool', __name__, url_prefix='pool')
rest_pool.add_url_rule('/pairs_stats', view_func=pairs_stats)
