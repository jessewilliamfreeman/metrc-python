import requests

class Client(object):

	def __init__(self, vendor_keys,environment):
		self.vendor_keys = vendor_keys
		self.environment = environment

	states ={
		'sandbox_states':{
			'AK': 'https://sandbox-api-or.metrc.com',
			'CA': 'https://sandbox-api-ca.metrc.com',
			'DC': 'https://sandbox-api-dc.metrc.com',
			'CO': 'https://sandbox-api-co.metrc.com',
			'LA': 'https://sandbox-api-or.metrc.com',
			'ME': 'https://sandbox-api-md.metrc.com',
			'MA': 'https://sandbox-api-ma.metrc.com',
			'MD': 'https://sandbox-api-md.metrc.com',
			'MI': 'https://sandbox-api-mi.metrc.com',
			'MO': 'https://sandbox-api-mo.metrc.com',
			'MT': 'https://sandbox-api-mt.metrc.com',
			'NV': 'https://sandbox-api-nv.metrc.com',
			'OH': 'https://sandbox-api-oh.metrc.com',
			'OK': 'https://sandbox-api-ok.metrc.com',
			'OR': 'https://sandbox-api-or.metrc.com',
			'WV': 'https://sandbox-api-wv.metrc.com'
		},
		'production_states':{
			'AK': 'https://api-ak.metrc.com',
			'CA': 'https://api-ca.metrc.com',
			'DC': 'https://api-dc.metrc.com',
			'CO': 'https://api-co.metrc.com',
			'LA': 'https://api-la.metrc.com',
			'ME': 'https://api-me.metrc.com',
			'MA': 'https://api-ma.metrc.com',
			'MD': 'https://api-md.metrc.com',
			'MI': 'https://api-mi.metrc.com',
			'MO': 'https://api-mo.metrc.com',
			'MT': 'https://api-mt.metrc.com',
			'NV': 'https://api-nv.metrc.com',
			'OH': 'https://api-oh.metrc.com',
			'OK': 'https://api-ok.metrc.com',
			'OR': 'https://api-or.metrc.com',
			'WV': 'https://api-wv.metrc.com'	
		}
	}

	def validate(self, state, user_key):

		environment = self.environment
		if(environment =='sandbox'):
			base_url = Client.states['sandbox_states'][state]
		elif(environment=='production'):
			base_url = Client.states['production_states'][state]

		vendor_key = self.vendor_keys[state]

		validate_url = base_url + "/facilities/v1/"
		print(validate_url)

		r = requests.get(validate_url, auth=(vendor_key, user_key))

		return r.status_code == 200