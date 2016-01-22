from tests.test_helper import *
from datetime import date

from app.database import Game, Country, DiplomaticRelationship

class CountryTest(TestBase):
  def test_defaults(self):
    game = GameFactory()
    game.save()

    Country.initialize_defaults(game)

    expect(len(Country.select())).to(equal(8))

  def test_successor_state(self):
    game = GameFactory()
    game.save()

    starting_country = Country.create(
      game = game,
      name = "Sealand",
    )

    successor_state = Country.create(
      game = game,
      name = "Government of Sealand in Exile",
      successor_to = starting_country,
    )

    expect(starting_country.succeeded_by).to(equal(successor_state))

  def test_create_diplomatic_relationships(self):
    game = GameFactory()
    game.save()

    sealand = Country.create(
      game = game,
      name = "Sealand",
    )
    conch_republic = Country.create(
      game = game,
      name = "Conch Republic",
    )

    sealand.set_relationship(
      user = User.create(
        game = game,
        name = "Nobody",
        email = "foo@bar.com",
      ),
      country = conch_republic,
      relationship_type = DiplomaticRelationship.ALLIANCE,
    )

    expect(conch_republic.relationship_with(sealand)).to(equal(DiplomaticRelationship.ALLIANCE))
