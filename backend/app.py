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



  return jsonify({'message': 
                  "1day: 97.82,\t week: 97.1,\n month: 97.34,\n three_months: 98.54,\n six_months: 92.83,\n year: 97.19,\n five_year: 96.6"
})


if __name__ == "__main__":
  app.run(debug=True)