from factory_peewee import PeeweeModelFactory
import factory

from app.database import Game, Database
from datetime import date

class GameFactory(PeeweeModelFactory):
  class Meta:
    model = Game
    database = Database

  id = factory.Sequence(lambda n: n)
  location = "Chicago"
  date = date.today()
  turn = 0
