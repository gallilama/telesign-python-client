import json
from telesign.api import Verify
from telesign.exceptions import AuthorizationError, TelesignError

"""
Command line client to call  TeleSign Verify services using TeleSign's Python SDK.
Assumes you've installed the TeleSign Python SDK from github.
Other parameters may be supported, these are the parameters I needed.

Example:
    $ python verify_client.py
    # enter service type
    # enter service arguments
    # rinse and repeat
    # ctrl-c to stop the client

Author: Chris Galli
"""

def prompt_svc_type():
    """
    Prompts for Verify service that will be called (e.g. call, sms, or status check)
    """
    svc_types = ['call', 'sms', 'status']
    svc_type = None
    prompt = "Enter Verify service %s: " % svc_types
    while svc_type not in (svc_types):
        svc_type = raw_input(prompt)
    return svc_type

def prompt_svc_args(params):
    """
    Prompts for arguments to be sent in the Verify service call.
    """
    svc_args = {}
    for key,value in params.items():
        prompt = "Enter %s (%s): " % (key, value)
        svc_args[key] = raw_input(prompt)
    return svc_args

def get_svc_params(svc_type):
    """
    Get list of service input parameters.
    Dictionary key is parameter name, value indicates parameter is required or optional.
    Verify services may accepts additional parameters.  These were the ones I needed.
    """
    svc_map = {
        'status' : {
            'ref_id': 'required',
            'verify_code' : 'optional'
        },
        'sms' : {
            'phone_number': 'required',
            'language' : 'optional',
            'template' : 'optional'
        },
        'call' : {
            'phone_number': 'required',
            'language' : 'optional'
        }
    }
    return svc_map[svc_type]

def call_svc(svc_type, svc_args):
    """
    Perform call to Verify service with desired parameters, and print results.
    You will need to supply the cust_id and secret_key values.
    See the fine folks at TeleSign for that information.
    """
    cust_id = ""     # Your TeleSign customer id here.
    secret_key = ""  # Your TeleSign secret key here.

    try:
        verify = Verify(cust_id, secret_key)
        print "Calling Verify [%s]..." % svc_type
        result = getattr(verify, svc_type)(**svc_args)
        # Not all calls will produce verify_code.  But keeping this simple.
        print "Verify code [%s]  Response: %s\n" % (result.verify_code, json.dumps(result.data))
    except AuthorizationError as ex:
        print '\nAuthorization error, credentials are likely invalid: ', ex
    except TelesignError as ex:
        print '\nTeleSign error: ', ex

def run():
    """
    Prompt for service type and service parameters, and call the Verify service.
    """
    svc_type = prompt_svc_type()
    svc_args = prompt_svc_args(get_svc_params(svc_type))
    call_svc(svc_type, svc_args)

if __name__ == '__main__':
    run()
