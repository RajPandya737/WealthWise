from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
from os import environ
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  


@app.route('/', methods=['GET'])
def home():
  return jsonify({'message': 'The server is running'})

@app.route('/test', methods=['GET'])
def test():
  # get current time
  time = datetime.now()
  current_time = time.strftime("%H:%M:%S")

  return jsonify({
    'last_day': 97.82,
    'week': 97.1,
    'month': 97.34,
    'three_months': 98.54,
    'six_months': 92.83,
    'year': 97.19,
    'five_year': 96.6
  })

if __name__ == "__main__":
  app.run(debug=True)