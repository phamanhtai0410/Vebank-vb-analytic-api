from marshmallow import INCLUDE, fields, Schema


class GetTotalParams(Schema):
    class Meta:
        unknown = INCLUDE
        ordered = True
        ignore_unknown_fields = True

    env = fields.Str(required=True)

