from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'  # Adjust this for your database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)  # Allow cross-origin requests for your frontend

# Example route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to my portfolio API!"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)