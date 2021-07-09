import sys

import yaml

from flask import Flask, jsonify, request

from flask_cors import CORS

from metrc import Client

app = Flask(__name__)
CORS(app)

vendor_keys = {}

with open('configs.yml') as f:
	config_data = yaml.load(f, Loader=yaml.FullLoader)
	vendor_keys= config_data['vendor_keys']
	environment= config_data['environment']
	

@app.route('/')
def hello_world():
	return "hello world"

@app.route('/user_key', methods = ['POST'])
def user_key():
	
	metrc_client = Client(vendor_keys,environment)

	print(request.form)

	validated = metrc_client.validate(
		request.form['state'], 
		request.form['user_key']
	)

	if validated:
		return jsonify({'message': 'user key validated'}), 200
	else:
		return jsonify({'message': 'user key failed to validate'}), 500