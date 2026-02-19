import unittest
import sys
import io
import  consolidation

class TestConsolidation(unittest.TestCase):

    def test_fibonacci(self):
        """Test fibonacci function with various inputs"""
        # Test edge case n=0
        self.assertEqual(consolidation.fibonacci(0), [])
        
        # Test n=1 (first number)
        self.assertEqual(consolidation.fibonacci(1), [0])
        
        # Test n=2 (first two numbers)
        self.assertEqual(consolidation.fibonacci(2), [0, 1])
        
        # Test basic sequence
        self.assertEqual(consolidation.fibonacci(5), [0, 1, 1, 2, 3])
        
        # Test extended sequence
        self.assertEqual(consolidation.fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        
        # Test longer sequence
        self.assertEqual(consolidation.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_factorial(self):
        """Test factorial function with various inputs"""
        # Test factorial of 0 (0! = 1 by definition)
        self.assertEqual(consolidation.factorial(0), 1)
        
        # Test factorial of 1
        self.assertEqual(consolidation.factorial(1), 1)
        
        # Test factorial of 2
        self.assertEqual(consolidation.factorial(2), 2)
        
        # Test factorial of 3
        self.assertEqual(consolidation.factorial(3), 6)
        
        # Test factorial of 4
        self.assertEqual(consolidation.factorial(4), 24)
        
        # Test factorial of 5
        self.assertEqual(consolidation.factorial(5), 120)
        
        # Test factorial of 6
        self.assertEqual(consolidation.factorial(6), 720)
        
        # Test factorial of 7
        self.assertEqual(consolidation.factorial(7), 5040)
        
        # Test negative number returns empty string
        self.assertEqual(consolidation.factorial(-1), "")
        self.assertEqual(consolidation.factorial(-5), "")

    def test_count_letters_and_punctuation(self):
        """Test count_letters_and_punctuation function"""
        # Test "Hello, World!"
        # h=1, e=1, l=3, o=2, ,=1, w=1, r=1, d=1, !=1
        expected1 = {'!': 1, ',': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
        self.assertEqual(consolidation.count_letters_and_punctuation("Hello, World!"), expected1)
        
        # Test empty string
        self.assertEqual(consolidation.count_letters_and_punctuation(""), {})
        
        # Test single character repeated "aaa"
        expected3 = {'a': 3}
        self.assertEqual(consolidation.count_letters_and_punctuation("aaa"), expected3)
        
        # Test "A!B@C#" - mixed case and punctuation
        expected4 = {'!': 1, '#': 1, '@': 1, 'a': 1, 'b': 1, 'c': 1}
        self.assertEqual(consolidation.count_letters_and_punctuation("A!B@C#"), expected4)
        
        # Test "Python is awesome!"
        # P-y-t-h-o-n (space) i-s (space) a-w-e-s-o-m-e-!
        # p=1, y=1, t=1, h=1, o=2, n=1, i=1, s=2, a=1, w=1, e=2, m=1, !=1
        expected5 = {'!': 1, 'a': 1, 'e': 2, 'h': 1, 'i': 1, 'm': 1, 'n': 1, 'o': 2, 'p': 1, 's': 2, 't': 1, 'w': 1, 'y': 1}
        self.assertEqual(consolidation.count_letters_and_punctuation("Python is awesome!"), expected5)
        
        # Test "123 abc!" - numbers should be ignored, spaces ignored
        expected6 = {'!': 1, 'a': 1, 'b': 1, 'c': 1}
        self.assertEqual(consolidation.count_letters_and_punctuation("123 abc!"), expected6)

    def test_count_perfect_squares_in_list(self):
        """Test count_perfect_squares_in_list function"""
        # Test [4, 9, 16, 17] - 4, 9, 16 are perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([4, 9, 16, 17]), 3)
        
        # Test [1, 4, 9] - all are perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([1, 4, 9]), 3)
        
        # Test [2, 3, 5, 7] - no perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([2, 3, 5, 7]), 0)
        
        # Test empty list
        self.assertEqual(consolidation.count_perfect_squares_in_list([]), 0)
        
        # Test [0] - 0 is a perfect square (0*0 = 0)
        self.assertEqual(consolidation.count_perfect_squares_in_list([0]), 1)
        
        # Test [1] - 1 is a perfect square (1*1 = 1)
        self.assertEqual(consolidation.count_perfect_squares_in_list([1]), 1)
        
        # Test [25, 36, 49, 50] - 25, 36, 49 are perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([25, 36, 49, 50]), 3)
        
        # Test [100, 121, 144, 150] - 100, 121, 144 are perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([100, 121, 144, 150]), 3)
        
        # Test [-4, 4, 9] - negative numbers are not perfect squares
        self.assertEqual(consolidation.count_perfect_squares_in_list([-4, 4, 9]), 2)
        
        # Test [16, 16, 25, 25] - duplicates count separately
        self.assertEqual(consolidation.count_perfect_squares_in_list([16, 16, 25, 25]), 4)

    def test_draw_triangle_prime(self):
        """Test draw_triangle_prime function"""
        # Capture printed output for testing
        
        # Test height = 1
        captured_output = io.StringIO()
        sys.stdout = captured_output
        consolidation.draw_triangle_prime(1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "2")
        
        # Test height = 2
        captured_output = io.StringIO()
        sys.stdout = captured_output
        consolidation.draw_triangle_prime(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "2\n3 5")
        
        # Test height = 3
        captured_output = io.StringIO()
        sys.stdout = captured_output
        consolidation.draw_triangle_prime(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "2\n3 5\n7 11 13")
        
        # Test height = 4
        captured_output = io.StringIO()
        sys.stdout = captured_output
        consolidation.draw_triangle_prime(4)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "2\n3 5\n7 11 13\n17 19 23 29")

    def test_matrix_multiply(self):
        """Test matrix_multiply function"""
        # Basic 2x3 * 3x2 = 2x2
        matrix1 = [[1, 2, 3],
                   [4, 5, 6]]
        matrix2 = [[7, 8],
                   [9, 10],
                   [11, 12]]
        expected1 = [[58, 64],
                     [139, 154]]
        self.assertEqual(consolidation.matrix_multiply(matrix1, matrix2), expected1)
        
        # 1x1 * 1x1 = 1x1
        matrix3 = [[5]]
        matrix4 = [[3]]
        expected2 = [[15]]
        self.assertEqual(consolidation.matrix_multiply(matrix3, matrix4), expected2)
        
        # 2x2 * 2x2 = 2x2
        matrix5 = [[1, 2],
                   [3, 4]]
        matrix6 = [[5, 6],
                   [7, 8]]
        expected3 = [[19, 22],
                     [43, 50]]
        self.assertEqual(consolidation.matrix_multiply(matrix5, matrix6), expected3)
        
        # 3x1 * 1x3 = 3x3
        matrix7 = [[1],
                   [2],
                   [3]]
        matrix8 = [[4, 5, 6]]
        expected4 = [[4, 5, 6],
                     [8, 10, 12],
                     [12, 15, 18]]
        self.assertEqual(consolidation.matrix_multiply(matrix7, matrix8), expected4)
        
        # 1x3 * 3x1 = 1x1
        matrix9 = [[1, 2, 3]]
        matrix10 = [[4],
                    [5],
                    [6]]
        expected5 = [[32]]
        self.assertEqual(consolidation.matrix_multiply(matrix9, matrix10), expected5)

    def test_is_palindrome_iterative(self):
        """Test is_palindrome_iterative function"""
        # Test basic palindromes
        self.assertTrue(consolidation.is_palindrome_iterative("civic"))
        self.assertTrue(consolidation.is_palindrome_iterative("Civic"))  # Case insensitive
        self.assertTrue(consolidation.is_palindrome_iterative("madam"))
        self.assertTrue(consolidation.is_palindrome_iterative("madAm"))  # Case insensitive
        self.assertTrue(consolidation.is_palindrome_iterative("racecar"))
        
        # Test non-palindromes
        self.assertFalse(consolidation.is_palindrome_iterative("hello"))
        self.assertFalse(consolidation.is_palindrome_iterative("world"))
        
        # Test edge cases
        self.assertTrue(consolidation.is_palindrome_iterative("A"))      # Single character
        self.assertTrue(consolidation.is_palindrome_iterative(""))       # Empty string
        self.assertTrue(consolidation.is_palindrome_iterative("Aa"))     # Two identical characters (case insensitive)
        self.assertFalse(consolidation.is_palindrome_iterative("Ab"))    # Two different characters
        
        # Test complex cases with spaces and punctuation
        self.assertTrue(consolidation.is_palindrome_iterative("A man a plan a canal Panama"))
        self.assertFalse(consolidation.is_palindrome_iterative("race a car"))
        self.assertTrue(consolidation.is_palindrome_iterative("Was it a car or a cat I saw"))
        
        # Test numbers
        self.assertTrue(consolidation.is_palindrome_iterative("12321"))
        self.assertFalse(consolidation.is_palindrome_iterative("12345"))


if __name__ == '__main__':
 
    unittest.main()
