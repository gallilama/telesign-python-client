telesign-python-client
======================

Command line client for testing/evaluating TeleSign REST API using TeleSign's Python SDK.

TeleSign Python SDK: https://github.com/TeleSign/python

I was recently tasked with evaluating TeleSign's REST API.
The good folks at TeleSign were kind enough to provide SDKs in a few languages.
Being new to Python, I took this an opportunity to get more familiar with Python
while also accomplishing my evaluation tasks.  I cleaned things up a little, and
put it on github in case somebody else found themselves in a similar position.
Feel free to take and modify to suit your needs.

Cheers

Prerequisites
======================
Install TeleSign's Python SDK.
https://github.com/TeleSign/python

Obtain TeleSign customer id and secret key from TeleSign.

    # Update call_svc with your customer id and secrect key
    cust_id = ""     # Your TeleSign customer id here.
    secret_key = ""  # Your TeleSign secret key here.

Examples
======================
Send verification code via SMS:

    $ python verify_client.py
    $ Enter Verify service ['call', 'sms', 'status']: sms
    $ Enter phone_number (required): 12225556666
    $ Enter language (optional):
    $ Enter template (optional):
    $ Calling Verify [sms]...
    $ Code [61216]  Result: {'status': {'updated_on': '2013-03-27T15:12:59.380596Z', 'code': 290, 'description': 'Message in progress'}, 'errors': [], 'verify': {'code_state': 'UNKNOWN', 'code_entered': ''}, 'sub_resource': 'sms', 'reference_id': '113DAC68C1AC0E0BE4D42FE500000D25', 'resource_uri': '/v1/verify/113DAC68C1AC0E0BE4D42FE500000D25'}
    $ Enter Verify service ['call', 'sms', 'status']:
    // rinse and repeat, ctrl-c to stop

Verify the status of the previous SMS:

    $ python verify_client.py
    $ Enter Verify service ['call', 'sms', 'status']: status
    $ Enter verify_code (optional):
    $ Enter ref_id (required): 113DAC68C1AC0E0BE4D42FE500000D25
    $ Calling Verify [status]...
    $ Code [None]  Result: {'status': {'updated_on': '2013-03-27T15:13:12.235918Z', 'code': 203, 'description': 'Delivered to gateway'}, 'errors': [], 'verify': {'code_state': 'UNKNOWN', 'code_entered': ''}, 'sub_resource': 'sms', 'reference_id': '113DAC68C1AC0E0BE4D42FE500000D25', 'resource_uri': '/v1/verify/113DAC68C1AC0E0BE4D42FE500000D25'}
    $ Enter Verify service ['call', 'sms', 'status']:
    // rinse and repeat, ctrl-c to stop
