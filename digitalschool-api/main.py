# from flask import Flask, jsonify,request

# app = Flask(__name__)

# @app.route("/api/login", methods=["GET"])
# def get_data():
    
#     return {
#         "username":"Santhosh",
#         "responsemessage": "Successfuly Login",
#         }

from flask import Flask, jsonify,request
import getlist
app = Flask(__name__)

@app.before_request
def add_cors_headers():
  if request.method == 'OPTIONS':
    resp = app.make_default_options_response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Custom-Header'
    return resp

@app.route('/api/login', methods=['Post'])
# def get_data():

#     return {
#         "username":"Santhosh",
#         "responsemessage": "Successfuly Login",
#         }
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username=='' or password=='':
      return jsonify({
          'error':True,
          'errorMessage':'Empty field username or password',
      }),200
    else:
      if username == 'santhosh' and password == '@0001':
        return jsonify({
        'error':False,
        'response':{
            'username':username,
            'responseMessage': 'Login successfully'
        }
       }), 200
      else:
        return jsonify({
          'error':True,
          'errorMessage':'Invalid username or password',
          }), 401
