import unittest
from io import StringIO
import sys
from unittest.mock import patch
import quote_system

class TestQuoteSystemSample(unittest.TestCase):

    def test_ask_file_name_with_input(self):
        """Test that ask_file_name returns the provided filename"""
        self.assertEqual(quote_system.ask_file_name('quotes.txt'), "quotes.txt")
    
    def test_ask_file_name_blank_input(self):
        """Test that ask_file_name defaults to quotes.txt for blank input"""
        self.assertEqual(quote_system.ask_file_name(''), "quotes.txt")
      
    def test_select_random_quotee_single(self):
        """Test random quotee selection with single item"""
        self.assertEqual(quote_system.select_random_quotee(["Eleanor Roosevelt"]), "Eleanor Roosevelt")

    def test_find_quote_exists(self):
        """Test finding an existing quote"""
        quotes = ['Thomas Edison ~ "I failed my way to success."', 'Anne Frank ~ "Whoever is happy will make others happy too."']
        self.assertEqual(
            quote_system.find_quote("Thomas Edison", quotes),
            'Thomas Edison ~ "I failed my way to success."'
        )

    def test_find_quote_not_exists(self):
        """Test handling when quote doesn't exist"""
        quotes = ['Thomas Edison ~ "I failed my way to success."', 'Anne Frank ~ "Whoever is happy will make others happy too."']
        self.assertEqual(
            quote_system.find_quote("Walt Disney", quotes), 
            "Quote/quotee does not exist."
        )

    def test_final_output_format(self):
        """Test the final output formatting"""
        text_capture = StringIO()
        sys.stdout = text_capture

        quote_system.final_output('Eleanor Roosevelt ~ "The future belongs to those who believe in the beauty of their dreams."', "Eleanor Roosevelt")
        
        expected = 'Quote found in file:\n\'Eleanor Roosevelt\': "The future belongs to those who believe in the beauty of their dreams."\n'
        self.assertEqual(expected, text_capture.getvalue())
        
        sys.stdout = sys.__stdout__

    def test_final_output_unquoted(self):
        """Test final output with unquoted quote"""
        text_capture = StringIO()
        sys.stdout = text_capture

        quote_system.final_output('Miriam Makeba ~ Age is getting to know all the ways the world turns, so that if you cannot turn the world the way you want, you can at least get out of the way so you won\'t get run over.', "Miriam Makeba")
        
        expected = 'Quote found in file:\n\'Miriam Makeba\': Age is getting to know all the ways the world turns, so that if you cannot turn the world the way you want, you can at least get out of the way so you won\'t get run over.\n'
        self.assertEqual(expected, text_capture.getvalue())
        
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
