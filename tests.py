import unittest
import solution

class TestFizzBuzz(unittest.TestCase):

    
    def test_wrong_type_parameters(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz('2','100')

    def test_return_type(self):
        self.assertEqual(list, type(solution.fizz_buzz(1,100)))

    def test_length_return(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz(100,2)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz(-1, -100)

    def test_output_3_returns_three(self):
        index = 3
        results = solution.fizz_buzz(1,100)
        self.assertEqual(results[index - 1][1], 'Three')

    def test_output_95_returns_five(self):
        index = 95
        results = solution.fizz_buzz(1,100)
        self.assertEqual(results[index - 1][1], 'Five')

    def test_output_90_returns_threefive(self):
        index = 90
        results = solution.fizz_buzz(1,100)
        self.assertEqual(results[index -1][1], 'ThreeFive')

    def test_output_16_returns_empty_string(self):
        index = 16
        results = solution.fizz_buzz(1,100)
        self.assertEqual(results[index -1][1], '')
        
if __name__ == '__main__':
    unittest.main()
