import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')

    auth = {
        '0cp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        '0cp-Apim-Subscription-Region': 'westus3',
    }
    r = requests.post(
        f'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={source_language}&to{dest_language}', headers=auth, json=[{'Text': text}]
    )
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']