import unittest 
from io import StringIO
import fundamentals as fun
import sys

class TestFundamentals(unittest.TestCase):
    def test_get_date_of_birth(self):
        self.assertEqual(fun.get_date_of_birth('0004185035083'), '18/04/00')


    def test_get_gender(self):
        self.assertEqual(fun.get_gender('9106236034082'), 'Male')


    def test_get_citizenship(self):
        self.assertEqual(fun.get_citizenship('9407076583088'), 'South African')

    def test_fizzbuzz(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        fun.fizzbuzz(20)
        expected_output = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\n"
        self.assertEqual(expected_output,text_capture.getvalue())
        

    def test_check_weirdness(self):
        self.assertEqual(fun.check_weirdness(15), 'Weird')
