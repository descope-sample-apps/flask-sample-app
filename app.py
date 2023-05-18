from flask import Flask, render_template, request, redirect, make_response, jsonify
from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient,
    AssociatedTenant,
    RoleMapping,
    AttributeMapping,
    LoginOptions
)
import json
import os
from functools import wraps


app = Flask(__name__)


try:
    descope_client = DescopeClient(project_id=os.environ.get("PROJECT_ID")) # initialize the descope client
except Exception as error:
    print ("failed to initialize. Error:")
    print (error)


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            if not 'Authorization' in request.headers:
               abort(401)

            user = None
            data = request.headers['Authorization'].encode('ascii','ignore')
            token = str.replace(str(data), 'Bearer ','')
            try:
                user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
            except:
                abort(401)

            return f(user, *args, **kws)            
    return decorated_function


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login(): 
    if request.method == "POST":
        session_token = request.get_json()
        try:
            jwt_response = descope_client.validate_session(session_token=session_token)
            print(jwt_response)
            return { "status": jwt_response }
        except Exception as error:
            print ("Could not validate user session. Error:")
            print (error)
            return { "error": error }

    return render_template("login.html")


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if request.headers.get('session'):
        return {"status": "Logged In"}
    else:
        redirect("login")

    return render_template("profile.html")


if __name__ == "main":
    app.run(debug=True, port=8000)