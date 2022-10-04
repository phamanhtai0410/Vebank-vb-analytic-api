from pymodm import fields
from lib.enums.database import DBName
from lib.model import BaseMG


class LendingHourDataModel(BaseMG):
    pool_address = fields.CharField(blank=True, default='')
    asset = fields.CharField(blank=True, default='')
    unbacked = fields.CharField(blank=True, default='')
    accrued_to_treasury = fields.CharField(blank=True, default='')
    total_aToken = fields.CharField(blank=True, default='')
    total_stable_debt = fields.CharField(blank=True, default='')
    total_variable_debt = fields.CharField(blank=True, default='')
    liquidity_rate = fields.CharField(blank=True, default='')
    variable_borrow_rate = fields.CharField(blank=True, default='')
    stable_borrow_rate = fields.CharField(blank=True, default='')
    average_stable_borrow_rate = fields.CharField(blank=True, default='')
    variable_borrow_index = fields.CharField(blank=True, default='')
    last_update_time = fields.CharField(blank=True, default='')
    is_cal = fields.BooleanField(default=False)
    
    class Meta:
        collection_name = 'lend_hour_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.ANALYTIC


class LendingDayDataModel(BaseMG):
    day = fields.CharField(blank=True, default='')
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pool_address = fields.CharField(blank=True, default='')
    asset = fields.CharField(blank=True, default='')


    class Meta:
        collection_name = 'lend_day_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.ANALYTIC


class LendingWeekDataModel(BaseMG):
    week = fields.CharField(blank=True, default='')
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pool_address = fields.CharField(blank=True, default='')
    asset = fields.CharField(blank=True, default='')


    class Meta:
        collection_name = 'lend_week_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.ANALYTIC


class LendingMonthDataModel(BaseMG):
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pool_address = fields.CharField(blank=True, default='')
    asset = fields.CharField(blank=True, default='')


    class Meta:
        collection_name = 'lend_month_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.ANALYTIC


class LendingSummaryModel(BaseMG):
    month = fields.CharField(blank=True, default='')
    year = fields.CharField(blank=True, default='')
    pool_address = fields.CharField(blank=True, default='')
    asset = fields.CharField(blank=True, default='')


    class Meta:
        collection_name = 'lend_month_data'
        final = True
        ignore_unknown_fields = True
        connection_alias = DBName.ANALYTIC
