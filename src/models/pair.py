from pymodm import fields
from lib.model import BaseMG
from lib.enums.database import DBName


class PairModel(BaseMG):
    class Meta:
        collection_name = 'pairs'
        connection_alias = DBName.POOL
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    factory_address = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default=0)
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    reserve0 = fields.CharField(blank=True, default='')
    reserve1 = fields.CharField(blank=True, default='')


class PoolHourDataModel(BaseMG):
    factory_address = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default='')
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    volume_token0 = fields.CharField(blank=True, default='')
    volume_token1 = fields.CharField(blank=True, default='')
    fee_token0 = fields.CharField(blank=True, default='')
    fee_token1 = fields.CharField(blank=True, default='')
    is_cal = fields.BooleanField(default=False)
    created_time = fields.DateTimeField(default=None)
    updated_time = fields.DateTimeField(default=None)
    updated_by = fields.CharField(blank=True, default='')

    class Meta:
        collection_name = 'hour_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.POOL


class PoolDayDataModel(BaseMG):
    day = fields.CharField(blank=True, default='')
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    factory_address = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default='')
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    volume_token0 = fields.CharField(blank=True, default='')
    volume_token1 = fields.CharField(blank=True, default='')
    fee_token0 = fields.CharField(blank=True, default='')
    fee_token1 = fields.CharField(blank=True, default='')
    created_time = fields.DateTimeField(default=None)
    updated_time = fields.DateTimeField(default=None)
    updated_by = fields.CharField(blank=True, default='')

    class Meta:
        collection_name = 'day_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.POOL


class PoolWeekDataModel(BaseMG):
    factory_address = fields.CharField(blank=True, default='')
    week = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default='')
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    volume_token0 = fields.CharField(blank=True, default='')
    volume_token1 = fields.CharField(blank=True, default='')
    fee_token0 = fields.CharField(blank=True, default='')
    fee_token1 = fields.CharField(blank=True, default='')
    created_time = fields.DateTimeField(default=None)
    updated_time = fields.DateTimeField(default=None)
    updated_by = fields.CharField(blank=True, default='')

    class Meta:
        collection_name = 'week_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.POOL


class PoolMonthDataModel(BaseMG):
    factory_address = fields.CharField(blank=True, default='')
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default='')
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    volume_token0 = fields.CharField(blank=True, default='')
    volume_token1 = fields.CharField(blank=True, default='')
    fee_token0 = fields.CharField(blank=True, default='')
    fee_token1 = fields.CharField(blank=True, default='')
    created_time = fields.DateTimeField(default=None)
    updated_time = fields.DateTimeField(default=None)
    updated_by = fields.CharField(blank=True, default='')

    class Meta:
        collection_name = 'month_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.POOL


class PoolSummaryModel(BaseMG):
    factory_address = fields.CharField(blank=True, default='')
    pair_address = fields.CharField(blank=True, default='')
    token0_address = fields.CharField(blank=True, default='')
    token1_address = fields.CharField(blank=True, default='')
    volume_token0 = fields.CharField(blank=True, default='')
    volume_token1 = fields.CharField(blank=True, default='')
    fee_token0 = fields.CharField(blank=True, default='')
    fee_token1 = fields.CharField(blank=True, default='')
    created_time = fields.DateTimeField(default=None)
    updated_time = fields.DateTimeField(default=None)
    updated_by = fields.CharField(blank=True, default='')

    class Meta:
        collection_name = 'summary_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.POOL



