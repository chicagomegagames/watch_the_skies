from . import Database, Game, User

def initialize_database():
  Database.create_tables([
    Game,
    User,
  ])
