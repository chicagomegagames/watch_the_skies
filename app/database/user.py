from . import BaseModel, Game, Database
from peewee import ForeignKeyField, CharField

class User(BaseModel):
  game = ForeignKeyField(Game)
  name = CharField()
  email = CharField()
  position = CharField(null=True)

  class Meta:
    database = Database
