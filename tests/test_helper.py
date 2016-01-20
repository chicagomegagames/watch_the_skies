import unittest
import freezegun
from expects import *

from app import Database
from app.database import *

from tests.factories import *

def console():
  from nose.tools import set_trace; set_trace()
  import code; code.interact(local=locals())
