# REST API Authentication with Flask-JWT
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == 'user' and password == 'pass':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as='user'), 200

if __name__ == '__main__':
    app.run(debug=True)
