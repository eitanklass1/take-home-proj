import hubspot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate, ApiException

import os
from dotenv import load_dotenv
load_dotenv()

def create_contact(data):
  client = hubspot.Client.create(access_token=os.getenv('HUBSPOT_TOKEN'))

  properties = {
    "firstname": data['first_name'],
    "lastname": data['last_name'],
    "email": data['email'],
    "company": data['company_name'],
  }
  simple_public_object_input_for_create = SimplePublicObjectInputForCreate(properties=properties)
  try:
    client.crm.contacts.basic_api.create(simple_public_object_input_for_create=simple_public_object_input_for_create)
    print("Success")
  except ApiException as e:
    print("Exception when calling basic_api->create: %s\n" % e)
