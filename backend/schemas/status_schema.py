from apiflask import Schema
from apiflask.fields import String, Integer

class StatusOuSchema(Schema):
    status = String()
    messages = String()
    service = String()
    items_count = Integer()