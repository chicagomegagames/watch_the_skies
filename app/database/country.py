from . import BaseModel, Database, Game, User
from peewee import CharField, ForeignKeyField


class Country(BaseModel):
  name = CharField()
  flag_url = CharField(null=True)
  successor_to = ForeignKeyField(
    "self",
    null = True,
    related_name = "succeeded_by"
  )
  game = ForeignKeyField(Game)

  class Meta:
    database = Database

  def set_relationship(self, **kwargs):
    for required_arg in ["user", "country", "relationship_type"]:
      if required_arg not in kwargs:
        raise Exception("set_relationship expected " + required_arg)

    relationship = DiplomaticRelationship(
      country1 = self,
      country2 = kwargs["country"],
      relationship_type = kwargs["relationship_type"],
    )
    relationship.save(user = kwargs["user"])


  def relationship_with(self, country):
    return DiplomaticRelationship.select().where(
      ((DiplomaticRelationship.country1 == self) | (DiplomaticRelationship.country1 == self)) &
      ((DiplomaticRelationship.country2 == self) | (DiplomaticRelationship.country2 == self))
    )

  def current_pr(self):
    current_pr = 0
    for pr_change in self.pr_changes:
      current_pr += pr_change.delta
    return current_pr


  @staticmethod
  def initialize_defaults(game):
    # USA
    Country.create(
      name = "United States of America",
      flag_url = None,
      game = game,
    )

    # UK
    Country.create(
      name = "United Kingdom of Great Britain and Northern Ireland",
      flag_url = None,
      game = game,
    )

    # Russia
    Country.create(
      name = "Russian Federation",
      flag_url = None,
      game = game,
    )

    # France
    Country.create(
      name = "French Republic",
      flag_url = None,
      game = game,
    )

    # India
    Country.create(
      name = "Republic of India",
      flag_url = None,
      game = game,
    )

    # Brazil
    Country.create(
      name = "Federative Republic of Brazil",
      flag_url = None,
      game = game,
    )

    # Japan
    Country.create(
      name = "State of Japan",
      flag_url = None,
      game = game,
    )

    # China
    Country.create(
      name = "People's Republic of China",
      flag_url = None,
      game = game,
    )


"""
  IF YOU ARE USING THIS CLASS DIRECTLY, YOU ARE
  DOING IT WRONG™

  Do not directly use the DiplomaticRelationship class, instead, use
  the helpers attached to Country. This is to ensure we never fuck the
  database.
"""

class DiplomaticRelationship(BaseModel):
  relationship_type = CharField()
  country1 = ForeignKeyField(Country, related_name = "country_one")
  country2 = ForeignKeyField(Country, related_name = "country_two")

  def save(self, **kwargs):
    if "user" not in kwargs:
      raise Exception("Must pass in user to DiplomaticRelationship.save!")

    with Database.atomic() as txn:
      user = kwargs.pop("user")
      super().save(**kwargs)

      DiplomaticRelationshipsAudit.create(
        changed_by = user,
        new_status = self.relationship_type,
        relationship_changed = self,
      )


  def audits(self):
    return DiplomaticRelationshipsAudit.select().where(
      DiplomaticRelationshipsAudit.relationship_changed == self)

  class Meta:
    database = Database


DiplomaticRelationship.WAR = "war"
DiplomaticRelationship.ALLIANCE = "alliance"

class DiplomaticRelationshipsAudit(BaseModel):
  changed_by = ForeignKeyField(User)
  relationship_changed = ForeignKeyField(DiplomaticRelationship)
  new_status = CharField()

  class Meta:
    database = Database
