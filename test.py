from veriocheck import veriocheck

veriocheck = veriocheck("YOUR_PRIVATE_KEY", "YOUR_AUTH_CODE", False)

# Example: Validates if your API Keys are valid
returnCode, returnValue = veriocheck.validateKey()
print returnCode, returnValue


# Example: Regenerates your public keys
returnCode, returnValue = veriocheck.regeneratePublicKey({"login": "veriocheck@gmail.com"})
if returnCode == 200:
	print ("Successful API Call ", returnValue["status"])
else:
	print ("Error with API Call ", returnValue)

