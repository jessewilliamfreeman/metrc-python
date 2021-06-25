import sys

sys.path.append('../..')

import yaml

from flask import Flask, jsonify, request

from flask_cors import CORS

from metrc.client import Client

app = Flask(__name__)
CORS(app)

vendor_keys = {}

with open('vendor_keys.yml') as f:
	vendor_keys = yaml.load(f, Loader=yaml.FullLoader)
	vendor_keys= vendor_keys['vendor_keys']

@app.route('/')
def hello_world():
	return "hello world"

@app.route('/user_key', methods = ['POST'])
def user_key():
	
	metrc_client = Client(vendor_keys)

	print(request.form)

	validated = metrc_client.validate(
		request.form['state'], 
		request.form['user_key']
	)

	if validated:
		return jsonify({'message': 'user key validated'}), 200
	else:
		return jsonify({'message': 'user key failed to validate'}), 500