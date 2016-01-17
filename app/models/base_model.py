from peewee import Model, DateTimeField
from datetime import datetime


class BaseModel(Model):
  created_at = DateTimeField()
  updated_at = DateTimeField()

  def save(self, **kwargs):
    now = datetime.now()
    if self.created_at is None:
    	self.created_at = now

    self.updated_at = now
    super().save(**kwargs)
