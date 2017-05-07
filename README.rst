VerioCheck Python Library
=========================

VerioCheck Python library provides convenient access to the VerioCheck API calls from
applications written in server-side Python script.


Please keep in mind that this package is for use with server-side Python script that uses VerioCheck secret keys. 

VerioCheck provides FREE Address validation, Identity Verification, SMS Verification, Contact Data Cleaning, Name & Gender Validation, Email & IP  Validation.



 
Signup for FREE API Keys
^^^^^^^^^^^^^^^^^^^^^^^^

You can Signup for Free API Keys at `VerioCheck Free API Signup <https://veriocheck.com/signup>`_


Documentation
^^^^^^^^^^^^^

See the `VerioCheck API Documentation <https://veriocheck.com/api-docs>`_

Installation
^^^^^^^^^^^^^^^^^^^^^^^^
Install the package with:

    pip install veriocheck


Usage
^^^^^^^^^^^^^^^^^^^^^^^^

The package needs to be configured with your account's secret key which is
available in your `VerioCheck Dashboard <https://veriocheck.com/account/dashboard>`_. Require it with the key's value:

.. code:: python

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




Methods
^^^^^^^^^^^^^^^^^^^^^^^^

This module contains easy access to the following methods. All these methods accept (inputJSONParams, CallbackFunction). Refer to the VerioCheck.nameCheck example above. Refer to API documentation for required parameters.

regeneratePublicKey, addressCheck, verifyIdentity, cleanAndVerify, smsCreateCode, smsVerifyCode, smsVerificationStatus, nameCheck, emailCheck, ipCheck


More Information
^^^^^^^^^^^^^^^^^^^^^^^^

 `VerioCheck Website <https://www.veriocheck.com>`_

 `VerioCheck API Documentation <https://veriocheck.com/api-docs>`_

 `VerioCheck Free Signup <https://veriocheck.com/signup>`_
