from ninja import Schema

class App1SchemaIn(Schema):
    title: str
    description: str

class App1SchemaOut(Schema):
    id: int