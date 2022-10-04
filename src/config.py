# -*- coding: utf-8 -*-

import os
import json
from dotenv import load_dotenv
load_dotenv()


class BaseConfig(object):
    PROJECT = "vb-analytics-api"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = os.getenv("SECRET_KEY")


class DefaultConfig(BaseConfig):
    DEBUG = True

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['vi']
    BABEL_DEFAULT_LOCALE = 'en'

    # DB
    POOL_DEX_MONGO_URI = os.getenv('POOL_DEX_MONGO_URI')
    ANALYTIC_MONGO_URI = os.getenv('ANALYTIC_MONGO_URI')

    # Redis Cluster
    REDIS_CLUSTER = json.loads(os.getenv('REDIS_CLUSTER'))

    # Sentry SDK
    SENTRY_DSN = os.getenv('SENTRY_DSN')
    # Blockchain RPC
    RPC_URI = os.getenv('RPC_URI')

    # Celery
    CELERY_TRACK_STARTED = "True"

    CELERY_ENABLE_UTC = True

    CELERY_IMPORTS = ['src.workers']

    # Scheduled Jobs Config
    SCHEDULED_INTERVAL = os.getenv('SCHEDULED_INTERVAL') or 1800

    # Vechain Call to Pool
    CONTRACT_LENDING_POOL = os.getenv('CONTRACT_LENDING_POOL')
    VECHAIN_RPC = os.getenv('VECHAIN_RPC')
    KEYSTORE_PASSWORD = os.getenv('KEYSTORE_PASSWORD')
    CALLER = os.getenv('CALLER')
    POOL_DEX_FACTORY_CONTRACT = os.getenv('POOL_DEX_FACTORY_CONTRACT')
    VEUSD_ADDRESS = os.getenv('VEUSD_ADDRESS')
    VVET_ADDRESS = os.getenv('VVET_ADDRESS')
    VB_ADDRESS = os.getenv('VB_ADDRESS')
    VTHO_ADDRESS = os.getenv('VTHO_ADDRESS')
    WHITELIST = [
        os.getenv('VVET_ADDRESS'),  # VVET
        os.getenv('VEUSD_ADDRESS'),  # VEUSD
        os.getenv('VB_ADDRESS'),  # VB
        os.getenv('VTHO_ADDRESS'),  # VTHO
    ]
    ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"
    BIG_DECIMAL_1E18 = 10 ** 18
    BIG_DECIMAL_1E6 = 10 ** 6
    BIG_DECIMAL_ONE = 1
    BIG_DECIMAL_ZERO = 0

    # RabitMQ
    RABBIT_HOST = os.getenv('RABBIT_HOST')
    RABBIT_USER = os.getenv('RABBIT_USER')
    RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')
    RABBIT_PORT = os.getenv('RABBIT_PORT')
    RABBIT_VHOST = os.getenv('RABBIT_VHOST')

    # Implementation environment
    ENV = os.getenv('ENV') or 'dev'

    ASSET_VET = os.getenv('ASSET_VET').lower()
    ASSET_VTHO = os.getenv('ASSET_VTHO').lower()
    ASSET_VEUSD = os.getenv('ASSET_VEUSD').lower()
    ASSET_VB = os.getenv('ASSET_VB').lower()
    LIST_ASSETS = [ASSET_VET, ASSET_VEUSD, ASSET_VB, ASSET_VTHO]
    ASSETS_NAME = {
        ASSET_VET: "vet",
        ASSET_VTHO: "vtho",
        ASSET_VEUSD: "veusd",
        ASSET_VB: "vb"
    }

