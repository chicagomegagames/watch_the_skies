from peewee import CharField, DateField, IntegerField
from . import BaseModel, Database

class Game(BaseModel):
  location = CharField()
  date = DateField()
  turn = IntegerField()

  class Meta:
    database = Database

  def terror(self):
    terror_count = 0
    for terror_change in self.terror_changes:
      terror_count += terror_change.delta
    return terror_count
