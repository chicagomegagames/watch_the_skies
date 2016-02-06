from tests.test_helper import *

class PRTest(TestBase):
  def test_pr(self):
    game = GameFactory()
    user = User.create(game = game, name = "Nobody", email = "foo@bar.com")
    country = Country.create(game = game, name = "Sealand")

    PR.create(country = country, user = user, delta = 5, reason = "People like Sealand!")

    expect(country.current_pr()).to(equal(5))

  def test_multiple_pr(self):
    game = GameFactory()
    user = User.create(game = game, name = "Nobody", email = "foo@bar.com")
    country = Country.create(game = game, name = "Sealand")

    PR.create(country = country, user = user, delta = 5, reason = "People like Sealand!")
    PR.create(country = country, user = user, delta = -3, reason = "Sealand fucked up")

    expect(country.current_pr()).to(equal(2))
