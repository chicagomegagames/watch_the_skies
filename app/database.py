from peewee import Proxy, SqliteDatabase
from .models import *
from os import environ


Database = Proxy()

db = None
if "APP_ENV" in environ:
  if environ["APP_ENV"] == "testing":
    db = SqliteDatabase(":memory:")

if db == None:
  db = SqliteDatabase("watch_the_skies.db")

Database.initialize(db)
