# This simulates jobs that are received from the Enterprise into Dispatch. 
# You will subsequently pick these up and process into your environment.

import requests
import binascii
import hmac
import hashlib
import gzip

# The public key/secret in this section simulates what the keys given to the enterprise
# (i.e. these are just for setting up test data). Therefore, please leave these as they are
secret_key = 'ask_for_secret'
headers = {
    'Content-Type': 'application/json',
    'X-Dispatch-Key': 'account|110|noop'
}

# Please note:
# 1. Use the <external_organization_id> that we provide you in the introductory email
# 2. Make sure to change the <external_id> for every run. If you don't and run again, it will 
#    update rather than insert a new record
payload = r"""
[
    {
        "header":{
            "record_type": "job",
            "version": "v3"
        },
        "record":{
            "external_organization_id": "your_company_name",
            "title": "some title - give a decent name for identifying",
            "source": "web",
            "status": "offered",
            "description": "some description",
            "external_id": "some_unique_job_id",
            "address":{
                "postal_code": "01235",
                "city": "Boston",
                "state": "MA",
                "street_1": "122 Summer St",
                "street_2": "apt 1"
            },
            "service_type": "plumber",
            "customer": {
                "first_name": "Jason",
                "last_name": "Davis",
                "external_id": "some_unique_customer_id",
                "email": "devs+jasondavis@dispatch.me",
                "home_address": {
                        "street_1": "71601 Ford Street",
                        "city": "Revere",
                        "state": "MA",
                        "postal_code": "02151"
                }               
            },
            "equipment_descriptions": [{
                  "manufacturer": "Sub-Zero Freezer Company",
                  "model_number": "700BCI",
                  "serial_number": "2397767",
                  "installation_date": "2006-10-23T00:00:00+0000",
                  "equipment_type": "Pro 48"
            }],
            "symptom": "Display dark | Alyssa DeJong - 11/21/2018 4:02:04 PM (Central Standard Time)\n- interior light on, display dark, unit not cooling\n- advised reset at breaker\n- advised if no change possible panel, electrical, or board issue\n- referred to FCS if reset does not resolve\n- referred to FCS, dispatched\n- cust. can be reached by phone or email, phone best after 2:00pm",
            "service_fee_precollected": 0,
            "service_fee": 100,
            "service_instructions": "some instruction"                        
        }
    }
]
"""

payload = gzip.compress(payload.encode())   
secret_key = bytearray.fromhex(secret_key)  
digester = hmac.new(secret_key, payload, hashlib.sha256)
headers['X-Dispatch-Signature'] = binascii.hexlify(digester.digest()).decode('utf-8')
post = requests.post('https://connect-sbx.dispatch.me/agent/in', headers=headers, data=payload)