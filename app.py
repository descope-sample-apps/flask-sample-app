from flask import Flask, render_template, request, redirect, make_response, jsonify, url_for
from descope import DescopeClient
import os
from functools import wraps


app = Flask(__name__)


try:
    descope_client = DescopeClient(project_id=os.environ.get("PROJECT_ID")) # initialize the descope client
except Exception as error:
    print ("failed to initialize. Error:")
    print (error)


def token_required(f): # auth decorator
    @wraps(f)
    def decorator(*args, **kwargs):
        session_token = None
        if 'Authorization' in request.headers: # check if token in request
            auth_request = request.headers['Authorization']
            session_token = auth_request.replace('Bearer ', '')
        if not session_token: # throw error
            return make_response(jsonify({"error": "❌ invalid session token!"}), 401)

        try: # validate token
            jwt_response = descope_client.validate_session(session_token=session_token)
        except:
            return make_response(jsonify({"error": "❌ invalid session token!"}), 401)

        return f(jwt_response, *args, **kwargs)

    return decorator


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login(): 
    return render_template("login.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/get_profile')
@token_required
def get_profile(jwt_response):
    return jwt_response


if __name__ == "main":
    app.run(debug=True, port=8000)