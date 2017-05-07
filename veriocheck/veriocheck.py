import requests
import json

gURL = "https://www.veriocheck.com/api/v1/"

def generateQueryString(self, jsonObj):
	queryString = "?" + "key=" + self.APIKEY + "&auth=" + self.AUTH
	for item in jsonObj:
		queryString = queryString + "&" + item + "=" + str(jsonObj[item])
	return queryString

	
class veriocheck:
	def __init__(self, APIKEY, AUTH, hideStartupMsg):
		
		self.members = {'Tigers': 2, 'Cat': "Cattt7"}
		self.APIKEY = APIKEY
		self.AUTH = AUTH
		
		if hideStartupMsg != True:
			print "For Free VerioCheck API Keys - https://veriocheck.com/signup"
			print "VerioCheck API Docs - https://veriocheck.com/api-docs"
			print "VerioCheck - Each method accepts a JSON object and JSON fields must be the same as defined in the API docs"
			print "###"
	
		
	def validateKey(self):
		r = requests.get(gURL + "validatekey" + generateQueryString(self, {}))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)

		
	def regeneratePublicKey(self, params):
		r = requests.get(gURL + "regenerate_publickey" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def addressCheck(self, params):
		r = requests.get(gURL + "address" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)

		
	def verifyIdentity(self, params):
		r = requests.get(gURL + "identity" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def cleanAndVerify(self, params):
		r = requests.get(gURL + "cleanandverify" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def smsCreateCode(self, params):
		r = requests.get(gURL + "sms_createcode" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def smsVerifyCode(self, params):
		r = requests.get(gURL + "sms_verifycode" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def smsVerificationStatus(self, params):
		r = requests.get(gURL + "sms_verificationstatus" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def nameCheck(self, params):
		r = requests.get(gURL + "namecheck" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def emailCheck(self, params):
		r = requests.get(gURL + "emailcheck" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


	def ipCheck(self, params):
		r = requests.get(gURL + "ipcheck" + generateQueryString(self, params))
		if r.status_code == 200:
			return (r.status_code, json.loads(r.content))
		else:
			return (r.status_code, r.content)


