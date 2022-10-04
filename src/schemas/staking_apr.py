from marshmallow import INCLUDE, fields, Schema


class GetAprParams(Schema):
    class Meta:
        unknown = INCLUDE
        ordered = True
        ignore_unknown_fields = True

    type = fields.Str(required=True)
    env = fields.Str(required=True)
