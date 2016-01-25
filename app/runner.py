from flask import Flask, request, Response, jsonify

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

    if request.method == 'POST':
        app.logger.debug(request.get_data())
        code = 501
        data = build_error('POST Not implemented')
    elif request.method == 'GET':
        code = 501
        data = build_error('GET Not implemented')
       
    return (jsonify(**data), code, {'Content-Type': rType})

# Maybe just use a PUT call to game instead.
@app.route('/game/turn', methods=['POST', 'GET'])
def game_turn():
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

@app.errorhandler(404)
@app.errorhandler(405)
def error_response(e):
    return (jsonify(**build_error(e.description)), e.code, {'Content-Type': 'application/json'})

if __name__ == "__main__":
    app.run(debug=True)
