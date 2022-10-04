# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint

from .controller import *

rest_lend = Blueprint('rest_lend', __name__, url_prefix='lend')
rest_lend.add_url_rule('/stats', view_func=lend_stats)

