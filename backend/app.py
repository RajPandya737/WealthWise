from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
from os import environ
from datetime import datetime

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

  return jsonify({'message': '{0} The server is running'.format(current_time)})


if __name__ == "__main__":
  app.run(debug=True)