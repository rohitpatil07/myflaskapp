from flask import Flask, request,jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return 'Hello World Major Changes !!!', 200      # 200 is HTTP the response code to be returned to client

@app.route('/health', methods=['GET'])
def health():
	return 'Healthy', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
