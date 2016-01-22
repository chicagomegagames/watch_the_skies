from tests.test_helper import *
from datetime import date

from app.database import Game

class gametest(TestBase):
  def test_game(self):
    game = Game.create(
      location="Chicago",
      date=date.today(),
      turn=0,
    )

    expect(game.location).to(equal("Chicago"))
