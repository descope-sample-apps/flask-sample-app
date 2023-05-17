from flask import Flask, render_template, request, redirect
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


app = Flask(__name__)


try:
    descope_client = DescopeClient(project_id=os.environ.get("PROJECT_ID")) # initialize the descope client
except Exception as error:
    print ("failed to initialize. Error:")
    print (error)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
# add decorator 
def login():
    if request.method == "POST":
        session_token = request.get_json()['session_token']

        try:
            jwt_response = descope_client.validate_session(session_token=session_token)
            print(jwt_response)
            return { "status": jwt_response }
        except Exception as error:
            print ("Could not validate user session. Error:")
            print (error)
            return { "error": error }
    
    return render_template('loggedIn.html')


if __name__ == "main":
    app.run(debug=True, port=8000)