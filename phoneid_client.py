import json
from telesign.api import PhoneId
from telesign.exceptions import AuthorizationError, TelesignError

"""
Command line client to call  TeleSign PhoneId Standard service using TeleSign's Python SDK.
Assumes you've installed the TeleSign Python SDK from github.
Other parameters may be supported, these are the parameters I needed.

Example:
    $ python verify_client.py
    # enter phone number
    # rinse and repeat
    # ctrl-c to stop the client

Author: Chris Galli
"""

def prompt_svc_args(params):
    """
    Prompts for arguments to be sent in the Verify service call.
    """
    svc_args = {}
    for key,value in params.items():
        prompt = "Enter %s (%s): " % (key, value)
        svc_args[key] = raw_input(prompt)
    return svc_args

def call_svc(svc_args):
    """
    Perform call to PhoneId service with desired parameters, and print results.
    You will need to supply the cust_id and secret_key values.
    See the fine folks at TeleSign for that information.
    """
    cust_id = ""     # Your TeleSign customer id here.
    secret_key = ""

    try:
        phoneId = PhoneId(cust_id, secret_key)
        print "Calling PhoneID standard"
        result = phoneId.standard(**svc_args)
        # Not all calls will produce verify_code.  But keeping this simple.
        print "Response: %s\n" % json.dumps(result.data)
    except AuthorizationError as ex:
        print '\nAuthorization error, credentials are likely invalid: ', ex
    except TelesignError as ex:
        print '\nTeleSign error: ', ex

def run():
    """
    Prompt for service type and service parameters, and call the Verify service.
    """
    svc_args = prompt_svc_args({'phone_number': 'required'})
    call_svc(svc_args)

if __name__ == '__main__':
    run()
