from tests.test_helper import *
from expects import *
from datetime import datetime, timedelta

from app.models import BaseModel
from peewee import SqliteDatabase, CharField


class TestModel(BaseModel):
  test = CharField(null=True)

  class Meta:
    database = Database

Database.create_tables([TestModel])

class BaseModelTest(unittest.TestCase):
  def test_created_at(self):
    time = datetime.now()
    with freezegun.freeze_time(time):
      model = TestModel.create()

      expect(model.created_at).to(equal(time))

  def test_created_at_doesnt_change_on_save(self):
    model = None

    create_time = datetime.now() - timedelta(days=1)
    with freezegun.freeze_time(create_time):
      model = TestModel.create()
      expect(model.created_at).to(equal(create_time))

    update_time = create_time + timedelta(days=1)
    with freezegun.freeze_time(update_time):
      model.text = "something"
      model.save()

      expect(model.created_at).to(equal(create_time))

  def test_updated_at_when_created(self):
    time = datetime.now()
    with freezegun.freeze_time(time):
      model = TestModel.create()

      expect(model.updated_at).to(equal(time))

  def test_updated_at_when_saved(self):
    model = None

    create_time = datetime.now() - timedelta(days=1)
    with freezegun.freeze_time(create_time):
      model = TestModel.create()
      expect(model.updated_at).to(equal(create_time))

    update_time = create_time + timedelta(days=1)
    with freezegun.freeze_time(update_time):
      model.text = "something"
      model.save()

      expect(model.updated_at).to(equal(update_time))
