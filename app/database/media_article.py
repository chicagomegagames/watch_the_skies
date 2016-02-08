from . import BaseModel, Database, Game, User
from peewee import IntegerField, CharField, ForeignKeyField, TextField

class MediaArticle(BaseModel):
  title = CharField()
  turn = IntegerField()
  author = CharField()
  organization = CharField()
  body = TextField()

  game = ForeignKeyField(Game, related_name = "media_articles")
  user = ForeignKeyField(User, related_name = "media_articles")

  def __dict__(self):
    return {
      "title": self.title,
      "turn": self.turn,
      "author": self.author,
      "organization": self.organization,
      "body": self.body,
      "game": self.game.id,
      "user": self.user.id
    }

  class Meta:
    database = Database

  @staticmethod
  def current_news(game):
    return MediaArticle.select().where(
        MediaArticle.game == game &
        MediaArticle.turn >= game.turn)

  def save(self, **kwargs):
    try:
      self.game
    except Exception as e:
      self.game = self.user.game

    if self.turn is None:
      self.turn = self.game.turn

    if self.author is None:
      self.author = self.user.name

    super().save(**kwargs)

