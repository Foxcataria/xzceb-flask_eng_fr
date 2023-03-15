"""
Module used to translate english text to french text and vice versa by means of
the IBM Watson Language Translator API.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Load environment variables containing information about the IBM Watson
# Language Translator API to use.
# apikey  (str): Unique API key used for authentication
# url     (str): Unique API url
# version (str): API version to use
apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

# Create an instance of the IBM Watson Language Translator.
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = version,
    authenticator = authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates the given english text to french text by means of the IBM Watson
    Language Translator API and returns the resulting french text.

    Parameters:
        english_text (str): english text to translate.

    Returns:
        french_text (str): french text the given english text was translated to.
    """
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()

    french_text = translation.get('translations')[0].get('translation')
    return french_text

def french_to_english(french_text):
    """
    Translates the given french text to english text by means of the IBM Watson
    Language Translator API and returns the resulting english text.

    Parameters:
        french_text (str): french text to translate.

    Returns:
        english_text (str): english text the given french text was translated to.
    """
    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = translation.get('translations')[0].get('translation')
    return english_text
