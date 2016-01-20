from . import *
from .country import DiplomaticRelationshipsAudit

def initialize_database():
  Database.create_tables([
    Game,
    User,
    Country,
    DiplomaticRelationship,
    DiplomaticRelationshipsAudit,
  ])
