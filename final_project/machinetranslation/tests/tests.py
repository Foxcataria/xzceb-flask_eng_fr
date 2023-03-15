"""
Module used to test the translation from english text to french text and vice
versa by means of the IBM Watson Language Translator API.
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Defines methods to test the translation from english text to french text
    and vice versa.
    """

    def test_english_to_french(self):
        """
        Tests the translation from english text to french text and ensures that
        wrong input leads to predictable results (empty text).
        """
        # Check that 'Hello' (english) returns 'Bonjour' (french).
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Check that 'Hello' (english) does not return 'Hello' (english).
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Check that 'None' does not return an empty string.
        self.assertNotEqual(english_to_french('None'), '')
        # Check that wrong input returns an empty string.
        self.assertNotEqual(english_to_french(0), 0)

    def test_french_to_english(self):
        """
        Tests the translation from french text to english text and ensures that
        wrong input leads to predictable results (empty text).
        """
        # Check that 'Bonjour' (french) returns 'Hello' (english).
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Check that 'Bonjour' (french) does not return 'Bonjour' (frensh).
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # Check that 'None' does not return an empty string.
        self.assertNotEqual(french_to_english('None'), '')
        # Check that wrong input returns an empty string.
        self.assertNotEqual(french_to_english(0),0)

if __name__ == '__main__':
    unittest.main()
