from flask import Flask, request, Response, jsonify
import json
from jsonschema import validate, ValidationError
from database import Game, Country, Terror, User, PR, MediaArticle, initialize
import schemas
import time
from peewee import OperationalError

def build_error(description, extras=None):
    return {'error': {'description': description, 'extras': extras}}

app = Flask(__name__)

@app.route('/terror', methods=['POST', 'GET'])
def terror():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    if request.method == 'POST':
        try:
            validate(inputJson, schemas.terror)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 204

            tDelta = Terror()
            tDelta.delta = inputJson["delta"]
            tDelta.reason = inputJson["reason"]
            tDelta.user = User.get(User.id == inputJson["user"])
            tDelta.game = Game.get(Game.id == inputJson["game"])

            tDelta.save()
    elif request.method == 'GET':
        try:
            validate(inputJson, schemas.terror_request)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 200
            tLog = Terror.select().where(Terror.game == inputJson["game"])
            terrorCount = 0
            for t in tLog:
                if t.delta:
                    terrorCount += t.delta

            data = {"count": terrorCount}
       
    return (jsonify(**data), code, {'Content-Type': rType})

@app.route('/pr', methods=['POST', 'GET'])
def pr():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    if request.method == 'POST':
        try:
            validate(inputJson, schemas.pr)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 204

            pDelta = PR()
            pDelta.delta = inputJson["delta"]
            pDelta.reason = inputJson["reason"]
            pDelta.user = User.get(User.id == inputJson["user"])
            pDelta.country = Country.get(Country.id == inputJson["country"])

            pDelta.save()
    elif request.method == 'GET':
        try:
            validate(inputJson, schemas.pr_request)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 200
            pLog = PR.select().where(PR.country == inputJson["country"])
            PRCount = 0
            for p in pLog:
                if p.delta:
                    PRCount += p.delta

            data = {"count": PRCount}
       
    return (jsonify(**data), code, {'Content-Type': rType})

@app.route('/news', methods=['POST', 'GET'])
def news():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    if request.method == 'POST':
        try:
            validate(inputJson, schemas.post_article)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 204

            article = MediaArticle()
            article.title = inputJson["title"]
            article.author = inputJson["author"]
            article.organization = inputJson["organization"]
            article.body = inputJson["body"]
            article.turn = inputJson["turn"]
            article.game = Game.get(Game.id == inputJson["game"])
            article.user = User.get(User.id == inputJson["user"])

            article.save()
    elif request.method == 'GET':
        try:
            validate(inputJson, schemas.get_articles)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            code = 200
            articles = MediaArticle.select().where(MediaArticle.game == inputJson["game"] and MediaArticle.turn == inputJson["turn"])
            data = {"articles": [a.__dict__() for a in articles]}
       
    return (jsonify(**data), code, {'Content-Type': rType})

@app.route('/announcement', methods=['POST', 'GET'])
def announcement():
    data = {}
    code = 500
    rType = "application/json"

    if request.method == 'POST':
        app.logger.debug(request.get_data())
        code = 501
        data = build_error('POST Not implemented')
    elif request.method == 'GET':
        code = 501
        data = build_error('GET Not implemented')
       
    return (jsonify(**data), code, {'Content-Type': rType})

#This might be better served under /country/relationship
@app.route('/relationship', methods=['POST', 'GET'])
def relationship():
    data = {}
    code = 500
    rType = "application/json"

    if request.method == 'POST':
        app.logger.debug(request.get_data())
        code = 501
        data = build_error('POST Not implemented')
    elif request.method == 'GET':
        code = 501
        data = build_error('GET Not implemented')
       
    return (jsonify(**data), code, {'Content-Type': rType})

@app.route('/game', methods=['POST', 'GET'])
def game():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    if request.method == 'POST':
        try:
            validate(inputJson, schemas.game_create)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            g = Game()
            g.location = inputJson["location"]
            if "date" in inputJson:
                g.date = inputJson()["date"]
            else:
                g.date = time.time()
            if "turn" in inputJson:
                g.turn = inputJson()["turn"]
            else:
                g.turn = 0
            g.save()
            Country.initialize_defaults(g)
            code = 200
            data = {"id": g.id, "location": g.location, "date": g.date, "turn": g.turn}
    elif request.method == 'GET':
        try:
            validate(inputJson, schemas.game_id)
        except ValidationError:
            code = 400
            data = build_error('Payload missing `id` field.')
        else:
            g = Game.get(Game.id == inputJson["id"])
            data = {"id": g.id, "location": g.location, "date": g.date, "turn": g.turn}
            code = 200
       
    return (jsonify(**data), code, {'Content-Type': rType})

# Maybe just use a PUT call to game instead.
@app.route('/game/turn', methods=['POST'])
def game_turn():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    try:
        validate(inputJson, schemas.game_id)
    except ValidationError:
        code = 400
        data = build_error('Payload missing `id` field.')
    else:
        g = Game.get(Game.id == inputJson["id"])
        g.turn += 1
        g.save()
        data = {"id": g.id, "location": g.location, "date": g.date, "turn": g.turn}
        code = 200
       
    return (jsonify(**data), code, {'Content-Type': rType})

@app.route('/user', methods=["POST", "GET"])
def user():
    data = {}
    code = 500
    rType = "application/json"
    inputJson = request.get_json();

    if request.method == 'POST':
        try:
            validate(inputJson, schemas.user_create)
        except ValidationError as sErr:
            code = 400
            data = build_error('Invalid JSON payload', extras=str(sErr))
        else:
            u = User()
            u.name = inputJson["name"]
            u.email = inputJson["email"]
            u.position = inputJson["position"]
            u.game = Game.get(Game.id == inputJson["game"])
            u.save()

            code = 200
            data = {"id": u.id}
    elif request.method == 'GET':
        try:
            validate(inputJson, schemas.user_id)
        except ValidationError:
            code = 400
            data = build_error('Payload missing `id` field.')
        else:
            u = User.get(User.id == inputJson["id"])
            data = {"id": u.id, "name": u.name, "email": u.email, "position": u.position}
            code = 200
       
    return (jsonify(**data), code, {'Content-Type': rType})


@app.errorhandler(404)
@app.errorhandler(405)
def error_response(e):
    return (jsonify(**build_error(e.description)), e.code, {'Content-Type': 'application/json'})

if __name__ == "__main__":
    try:
       initialize.initialize_database()
    except OperationalError:
        print("DB already exists")
    finally:
        app.run(debug=True)
