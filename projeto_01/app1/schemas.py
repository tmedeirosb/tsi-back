from ninja import Schema, ModelSchema
from app1.models import Agenda

class App1SchemaIn(Schema):
    title: str
    description: str

class App1SchemaOut(Schema):
    id: int

class AgendaSchemaIn(ModelSchema):
    class Config:
        model = Agenda
        model_fields = ["nome", "telefone"]

class AgendaSchemaOut(ModelSchema):
    class Config:
        model = Agenda
        model_fields = ["nome", "telefone"]

