
from marshmallow import Schema, fields

class CSVSchema(Schema):
    title = fields.Str(required=True)
    user_id = fields.Str(required=True)
    json = fields.Str(required=True)

class CSVUpdateSchema(Schema):
    old_title = fields.Str()
    new_title = fields.Str()
    new_json = fields.Str()
    user_id = fields.Str(required=True)

