from flask import Flask
from api.routes import api

app = Flask(__name__)

app.register_blueprint(api)

@app.route("/")
def home():

    return {
        "Project": "AI-Powered Financial News & Sentiment Analysis Engine",
        "Version": "1.0",
        "Status": "Running"
    }

if __name__ == "__main__":
    app.run(debug=True)