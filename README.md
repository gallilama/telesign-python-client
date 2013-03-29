telesign-python-client
======================

Command line client for using TeleSign Python SDK

See https://github.com/TeleSign/python_telesign for SDK.

Example
======================
Assuming the TeleSign SDK is installed, you can run this client from the command line.

Verify the status of a previous verify/call request:

    $ python verify_client.py
    $ Enter Verify service ['call', 'sms', 'status']: status
    $ Enter verify_code (optional):
    $ Enter ref_id (required): ABC123
    $ Calling Verify [status]...
    $ Code [None]  Result: {"status": {"updated_on": "2013-03-29T01:52:29.242327Z", "code": 100, "description": "Call answered"}, "errors": [], "verify": {"code_state": "UNKNOWN", "code_entered": ""}, "sub_resource": "call", "reference_id": "ABC123", "resource_uri": "/v1/verify/ABC123"}
