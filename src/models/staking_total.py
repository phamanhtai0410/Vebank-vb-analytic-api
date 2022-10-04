from pymodm import fields
from lib.model import BaseMG
from lib.enums.database import DBName


class StakingTotalModel(BaseMG):
    class Meta:
        collection_name = 'staking_total'
        connection_alias = DBName.ANALYTIC
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    env = fields.CharField(blank=True, default='')
    staking_contract = fields.CharField(blank=True, default='')
    total = fields.FloatField(blank=True, default=0)

    @classmethod
    def get_latest_total_staked(cls, filter={}):
        _query_res = list(cls.aggregate(
            pipelines=[
                {
                    "$match": filter
                },
                {
                    "$sort": {
                        "created_time": -1
                    }
                },
                {
                    "$limit": 1
                }
            ]
        ))
        print("__Get latest : ", len(_query_res), _query_res)
        if len(_query_res) > 0:
            print("1")
            return _query_res[0]
        return None


