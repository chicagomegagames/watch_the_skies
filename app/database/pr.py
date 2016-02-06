from . import BaseModel, Database, User, Country
from peewee import IntegerField, CharField, ForeignKeyField

class PR(BaseModel):
  delta = IntegerField()
  reason = CharField()
  country = ForeignKeyField(Country, related_name = "pr_changes")
  user = ForeignKeyField(User, related_name = "added_pr")

  class Meta:
    database = Database
