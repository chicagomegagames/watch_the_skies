from peewee import CharField, DateField, IntegerField
from . import BaseModel, Database

class Game(BaseModel):
  location = CharField()
  date = DateField()
  turn = IntegerField()

  class Meta:
    database = Database
