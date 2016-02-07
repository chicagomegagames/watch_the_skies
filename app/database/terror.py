from . import BaseModel, Database, Game, User
from peewee import ForeignKeyField, IntegerField, CharField

class Terror(BaseModel):
  delta = IntegerField()
  reason = CharField()
  user = ForeignKeyField(User, related_name = "added_terror")
  game = ForeignKeyField(Game, related_name = "terror_changes")

  class Meta:
    database = Database

  def save(self, **kwargs):
    try:
      self.game
    except Exception as e:
      self.game = self.user.game
    super().save(**kwargs)

  def __repr__(self):
      return str(self.id) + " " + str(self.delta)

  def __str__(self):
      return self.__repr__()
