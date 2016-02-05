from flask import Flask, request, Response, jsonify
import json
from jsonschema import validate, ValidationError
from database import Game, initialize
import schemas
import time
from peewee import OperationalError


app = Flask(__name__)

def build_error(description, extras=None):
    return {'error': {'description': description, 'extras': extras}}

@app.route('/terror', methods=['POST', 'GET'])
def terror():
    data = None
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

@app.route('/pr', methods=['POST', 'GET'])
def pr():
    data = None
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

@app.route('/news', methods=['POST', 'GET'])
def news():
    data = None
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

@app.route('/announcement', methods=['POST', 'GET'])
def announcement():
    data = None
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
    data = None
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
    data = None
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
    data = None
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
