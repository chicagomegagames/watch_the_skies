from tests.test_helper import *

class TestDiplomaticRelationship(TestBase):
  def test_creates_audit_log(self):
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

    relationship = DiplomaticRelationship(
      country1 = sealand,
      country2 = conch_republic,
      relationship_type = DiplomaticRelationship.ALLIANCE,
    )
    relationship.save(
      user = User.create(
        game = game,
        name = "Nobody",
        email = "foo@bar.com",
      )
    )

    expect(len(relationship.audits())).to(equal(1))
