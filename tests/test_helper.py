import unittest
import freezegun
from expects import *

from app import Database
from app.database import *
from app.database.country import DiplomaticRelationshipsAudit

from tests.factories import *

def console():
  from nose.tools import set_trace; set_trace()
  import code; code.interact(local=locals())

class TestBase(unittest.TestCase):
  def setUp(self):
    Database.create_tables([
      Game,
      User,
      Country,
      DiplomaticRelationship,
      DiplomaticRelationshipsAudit,
      Terror,
    ])

  def tearDown(self):
    Database.drop_tables([
      Game,
      User,
      Country,
      DiplomaticRelationship,
      DiplomaticRelationshipsAudit,
      Terror,
    ])
