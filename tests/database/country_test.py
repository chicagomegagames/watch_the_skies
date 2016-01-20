from tests.test_helper import *
from datetime import date

from app.database import Game, Country, DiplomaticRelationship

class CountryTest(unittest.TestCase):
  def setUp(self):
    self.game = Game.create(
      location = "Chicago",
      date = date.today(),
      turn = 0,
    )

  def test_defaults(self):
    starting_number_of_countries = len(Country.select())

    Country.initialize_defaults(self.game)

    expect(len(Country.select())).to(equal(8 + starting_number_of_countries))

  def test_successor_state(self):
    starting_country = Country.create(
      game = self.game,
      name = "Sealand",
    )

    successor_state = Country.create(
      game = self.game,
      name = "Government of Sealand in Exile",
      successor_to = starting_country,
    )

    expect(starting_country.succeeded_by).to(equal(successor_state))

  def test_create_diplomatic_relationships(self):
    sealand = Country.create(
      game = self.game,
      name = "Sealand",
    )
    conch_republic = Country.create(
      game = self.game,
      name = "Conch Republic",
    )

    sealand.set_relationship(
      user = User.create(
        game = self.game,
        name = "Nobody",
        email = "foo@bar.com",
      ),
      country = conch_republic,
      relationship_type = DiplomaticRelationship.ALLIANCE,
    )

    expect(conch_republic.relationship_with(sealand)).to(equal(DiplomaticRelationship.ALLIANCE))
