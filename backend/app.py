from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #This allows requests from the frontend

@app.route('/')
def home():
    return jsonify ({"message": "Welcome to Smart Cart AI!"})

if __name__ == '__main__':
    app.run(debug=True)