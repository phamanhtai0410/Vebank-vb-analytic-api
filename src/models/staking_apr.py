from pymodm import fields
from lib.model import BaseMG
from lib.enums.database import DBName


class StakingAPRModel(BaseMG):
    class Meta:
        collection_name = 'staking_apr'
        connection_alias = DBName.ANALYTIC
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    env = fields.CharField(blank=True, default='')
    staking_contract = fields.CharField(blank=True, default='')
    apr = fields.FloatField(blank=True, default=0)



