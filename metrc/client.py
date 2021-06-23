import requests

class Client(object):

	def __init__(self, vendor_keys):
		self.vendor_keys = vendor_keys

	states = {
		'MD': 'https://sandbox-api-md.metrc.com',
		'OR': 'https://sandbox-api-or.metrc.com',
		'CO': 'https://sandbox-api-co.metrc.com',
		'LA': 'https://sandbox-api-or.metrc.com',
		'ME': 'https://sandbox-api-md.metrc.com',
		'AK': 'https://sandbox-api-or.metrc.com'
	}

	def validate(self, state, user_key):
		
		base_url = Client.states[state]

		vendor_key = self.vendor_keys[state]

		validate_url = base_url + "/facilities/v1/"

		r = requests.get(validate_url, auth=(vendor_key, user_key))

		return r.status_code == 200
