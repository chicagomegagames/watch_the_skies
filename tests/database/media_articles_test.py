from tests.test_helper import *

class MediaArticlesTest(TestBase):
  def test_derives_turn_from_game_if_not_set(self):
    game = GameFactory()
    user = User.create(game = game, name = "Media User", email = "foo@bar.com")

    game.turn = 1
    game.save()
    article = MediaArticle.create(
      game = game,
      user = user,

      title = "Media Declares Crisis!",
      author = "FatCat McNewspaperman",
      organization = "NewsCorpIncLLP",
      body = "this is some nice newspaper text, don't you think?",
    )

    expect(article.turn).to(equal(1))

  def test_derives_author_from_user_if_not_set(self):
    game = GameFactory()
    user = User.create(game = game, name = "Media User", email = "foo@bar.com")

    article = MediaArticle.create(
      user = user,

      title = "Media Declares Crisis!",
      organization = "NewsCorpIncLLP",
      body = "this is some nice newspaper text, don't you think?",
    )

    expect(article.author).to(equal("Media User"))

  def test_can_get_current_news_items_from_game(self):
    game = GameFactory()
    user = User.create(game = game, name = "Media User", email = "foo@bar.com")

    article = MediaArticle.create(
      user = user,

      title = "Media Declares Crisis!",
      organization = "NewsCorpIncLLP",
      body = "this is some nice newspaper text, don't you think?",
    )

    expect(MediaArticle.current_news(game)).to(equal([article]))

  def test_game_current_news_items_excludes_items_for_future_turns(self):
    game = GameFactory()
    user = User.create(game = game, name = "Media User", email = "foo@bar.com")

    article = MediaArticle.create(
      user = user,
      title = "Media Declares Crisis!",
      organization = "NewsCorpIncLLP",
      body = "this is some nice newspaper text, don't you think?",
    )
    future_article = MediaArticle.create(
      user = user,
      turn = 500,
      title = "Media Declares Crisis!",
      organization = "NewsCorpIncLLP",
      body = "this is some nice newspaper text, don't you think?",
    )

    expect(MediaArticle.current_news(game)).to(equal([article]))
