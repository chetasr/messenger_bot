# Import essentials

from wit import Wit
import simplejson as json
import random, os
from engine import dynamicgen

# Entity processing

def extract_entities(response):
    # Extract entites from NLP response
    entities = {}
    for x in response['entities']:
        if x == 'intent':
            pass
        else:
            if 'suggested' in response['entities'][x][0].keys():
                continue
            entities[x] = response['entities'][x][0]['value']

    return entities

# Main stuff

def do(text, logging=False):
    # Process input and act accordingly
    witClient = Wit(access_token=os.environ['WIT_ACCESS_TOKEN'])
    response = witClient.message(text)
    if logging:
        print response
    intent = response['entities']['intent'][0]['value']
    entities = extract_entities(response)
    if logging:
        print entities, intent
    t = str(intent)
    f = str(entities.keys()[0])
    return dynamicgen.create_program_stack(f, t, entities, logging)[t]
