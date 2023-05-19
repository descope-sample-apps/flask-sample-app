# Flask Sample App + Descope Auth

Using the Python framework Flask + Descope Python SDK to add authentication and manage basic authentication

<br>

## Setup + Installing Dependencies 🛠️

1. cd into flask-sample-app: ```pip3 install -r requirements.txt``` 
2. You can choose to create a virtual environment before you install all the dependencies: <br>
```python3 -m venv ENV_NAME``` and to activate: ```source ENV_NAME/bin/activate``` 
3. Go to static/descope.js and add your project id in the quotes: ```const projectId = ""```
4. Create a ```.env``` file and inside and add your project id in the file:  ```PROJECT_ID=YOUR_PROJECT_ID```
5. ```flask run```

<br>

## What is going on? 🤔

### How do I get started with Descope?
If you don't have a descope project or don't know what a project ID is check out the [docs](https://docs.descope.com/build/guides/gettingstarted/)

### What is Flask?
Flask is a light-weight framework written in Python. It's super simple to get your web app started and running using Flask with just a couple of lines. To learn the basics of Flask check out the official [documentation](https://flask.palletsprojects.com/en/2.3.x/quickstart/)<br>