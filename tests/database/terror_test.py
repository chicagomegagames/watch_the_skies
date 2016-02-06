from tests.test_helper import *

class TerrorTest(TestBase):
  def test_terror(self):
    game = GameFactory()
    game.save()

    user = User.create(
      game = game,
      name = "Nobody",
      email = "foo@bar.com",
    )

    Terror.create(user = user, delta = 10, reason = "OMG LIEK ALIENS!")

    expect(game.terror()).to(equal(10))

  def test_multiple_terror(self):
    game = GameFactory()
    game.save()

    user = User.create(
      game = game,
      name = "Nobody",
      email = "foo@bar.com",
    )

    Terror.create(user = user, delta = 10, reason = "OMG LIEK ALIENS!")
    Terror.create(user = user, delta = 15, reason = "war in the US")
    Terror.create(user = user, delta = -20, reason = "that's some good peacekeeping")

    expect(game.terror()).to(equal(5))
