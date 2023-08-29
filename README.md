![flask-sample-app](https://github.com/descope-sample-apps/flask-sample-app/assets/59460685/307e5349-3b6d-4b7d-87d0-5e0a4e63f5e0)

---

Using the Python framework Flask + Descope Python SDK to add and manage basic authentication

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
