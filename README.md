![flask-html](https://github.com/descope-sample-apps/flask-sample-app/assets/59460685/d2d3f9eb-0a49-470c-8f83-eb2dc4d56f9e)

# Flask Sample App 

Use the Flask Python framework and Descope's Python SDK to add and manage basic authentication.

## ⚙️ Setup

1. Clone the repository:

```
git clone https://github.com/descope-sample-apps/flask-sample-app.git
```

2. Install dependencies:

```
make setup
```

3. Setup environment variables:

```
PROJECT_ID="YOUR_DESCOPE_PROJECT_ID"
```

- ```DESCOPE_ID```: can be found in your Descope's account under the [Project page](https://app.descope.com/settings/project)

4. Go to static/descope.js and add your project id in the quotes: ```const projectId = ""```

## 🔮 Running the Application 

To start the application, run:

```
flask run
```

## ⚠️ Issue Reporting

For any issues or suggestions, feel free to open an issue in the GitHub repository.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
