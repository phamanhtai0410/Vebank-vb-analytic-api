# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint

from .controller import *

rest_stake = Blueprint('rest_stake', __name__, url_prefix='stake')
# rest_root.add_url_rule('/common/health_check', view_func=health_check)

