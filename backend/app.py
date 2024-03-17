from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
from os import environ

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
@app.route('/test', methods=['GET'])
def test():
  return jsonify({'message': 'The server is running'})

if __name__ == "__main__":
  app.run(debug=True)