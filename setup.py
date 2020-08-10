from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")
def index():
  return "Home page!"

@app.route("/users")
def get_users():
  user = User.query.filter_by(username="admin").first()
  return {
    "username": user.username
  }

if __name__ == "__main__":
  app.run()