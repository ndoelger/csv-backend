
from marshmallow import Schema, fields

class CSVSchema(Schema):
    title = fields.Str(required=True)
    id = fields.Str(required=True)
    json = fields.Str(required=True)

class CSVUpdateSchema(Schema):
    title = fields.Str()
    json = fields.Str()

