import unittest 
from io import StringIO
import fundamentals as fun
import sys

class TestFundamentals(unittest.TestCase):
    
    
    def test_get_date_of_birth(self):
        test_cases = [
        ('0004185035083', '18/04/00'),
        ('0111224903088', '22/11/01'),
        ('9809126723080', '12/09/98'),
        ('8503157834056', '15/03/85'),
        ('7212084561029', '08/12/72')
        ]
        
        
        for id_number, expected in test_cases:
            result = fun.get_date_of_birth(id_number)
            self.assertEqual(result, expected, f"get_date_of_birth('{id_number}') returned incorrect date format")
            
            
    def test_get_gender(self):
        
        test_cases = [
        ('9106236034082', 'Male'),
        ('9402030894089', 'Female'),
        ('0312264983083', 'Female'),
        ('8907125678092', 'Male'),
        ('9205034321087', 'Female')
        ]
        
        
        for id_number, expected in test_cases:
            result = fun.get_gender(id_number)
            self.assertEqual(result, expected, f"get_gender('{id_number}') returned incorrect gender")
            
    def test_get_citizenship(self):
        
        test_cases = [
        ('9407076583088', 'South African'),     
        ('9210304503182', 'Non-South African'), 
        ('0312264983083', 'South African'),     
        ('8503157834001', 'South African'),     
        ('7212084561129', 'Non-South African')  
        ]
        
        
        for id_number, expected in test_cases:
            result = fun.get_citizenship(id_number)
            self.assertEqual(result, expected, f"get_citizenship('{id_number}') returned incorrect citizenship")
            
            
    def test_fizzbuzz(self):
        
        
        test_scenarios = [
        (15, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"),
        (10, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n"),
        (5, "1\n2\nFizz\n4\nBuzz\n"),
        (3, "1\n2\nFizz\n"),
        (30, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n"),
        (50, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\n"),
        (100, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n")
        ]
        
        for n, expected_output in test_scenarios:
            text_capture = StringIO()
            original_stdout = sys.stdout
            sys.stdout = text_capture
            
            fun.fizzbuzz(n)
            
            sys.stdout = original_stdout
            actual_output = text_capture.getvalue()
            
            self.assertEqual(actual_output, expected_output, f"fizzbuzz({n}) produced incorrect output")
            
            
    def test_check_weirdness(self):
        
        test_cases = [
        (0, 'Neutral'),  
        (1, 'Weird'),   
        (3, 'Weird'),    
        (7, 'Weird'),    
        (2, 'Not Weird'), 
        (4, 'Not Weird'), 
        (6, 'Weird'),   
        (10, 'Weird'),    
        (18, 'Weird'),    
        (20, 'Weird'),    
        (22, 'Not Weird'), 
        (50, 'Not Weird'), 
        (100, 'Not Weird'), 
        (-2, 'Very weird'), 
        (-4, 'Very weird'), 
        (-1, 'Extremely Weird'),
        (-3, 'Extremely Weird'), 
        (-15, 'Extremely Weird') 
        ]
        
    
        for n, expected in test_cases:
            result = fun.check_weirdness(n)
            self.assertEqual(result, expected, f"check_weirdness({n}) returned '{result}', expected '{expected}'")
            
