from setuptools import setup

setup(
		name='veriocheck',
      description='VerioCheck Contact Validation & Identity Verification API',
		long_description='VerioCheck Python library provides convenient access to the VerioCheck API calls from applications written in server-side Python. Please keep in mind that this package is for use with server-side Python script that uses VerioCheck secret keys.',
      version='1.0.2',
      url='https://veriocheck.com',
      author='VerioCheck',
      author_email='info@veriocheck.com',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable'
      ],
      packages=['veriocheck'],
		keywords = 'VerioCheck Address Validation Identity Verification Name Gender SMS Verification IP Reputation Check Email API'
)