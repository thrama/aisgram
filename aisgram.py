import os
import json
import logging
import openai
from pathlib import Path

# read settings
with open(Path('confs/settings.json'), 'r') as json_file:
    confs = json.load(json_file)

# load your API key from settings file
openai_apikey = confs['credentials']['openai_apikey']
openai.api_key = openai_apikey

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

print(response)