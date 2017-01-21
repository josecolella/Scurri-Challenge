#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
Copyright (c) 2017 Jose Colella

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import unittest
import types
import solution


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.default_beginning_index = 1
        self.default_ending_index = 100

    def test_wrong_type_parameters(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz('2', '100')

    def test_return_type(self):
        self.assertEqual(types.GeneratorType, type(solution.fizz_buzz(1, 100)))

    def test_length_return(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz(100, 2)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            solution.fizz_buzz(-1, -100)

    def test_output_wrong_type_for_key_raises_exception(self):
        with self.assertRaises(TypeError):
            solution.fizz_buzz(1, 100, 'hello')

    def test_exception_raised_when_key_not_present(self):
        with self.assertRaises(ValueError):
            result = solution.fizz_buzz(1, 100, 0)
            next(result)

    def test_output_3_returns_three(self):
        index = 3
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index, index)
        self.assertEqual(next(results), 'Three')

    def test_output_95_returns_five(self):
        index = 95
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index, index)
        self.assertEqual(next(results), 'Five')

    def test_output_90_returns_threefive(self):
        index = 90
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index, index)
        self.assertEqual(next(results), 'ThreeFive')

    def test_output_16_returns_number(self):
        index = 16
        expected_result = 16
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index, index)
        self.assertEqual(next(results), expected_result)

    def test_output_30_returns_threefive_string(self):
        index = 30
        expected_result = 'ThreeFive'
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index, index)
        self.assertEqual(next(results), expected_result)

    def test_output_fizz_buzz_from_one_to_hundred(self):
        expected_results = [1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five', 11,
                            'Three', 13, 14, 'ThreeFive', 16, 17, 'Three', 19,
                            'Five', 'Three', 22, 23, 'Three', 'Five', 26, 'Three', 28, 29,
                            'ThreeFive', 31, 32, 'Three', 34, 'Five', 'Three', 37, 38, 'Three', 'Five',
                            41, 'Three', 43, 44, 'ThreeFive', 46, 47, 'Three', 49, 'Five',
                            'Three', 52, 53, 'Three', 'Five', 56, 'Three', 58, 59,
                            'ThreeFive', 61, 62, 'Three', 64, 'Five', 'Three', 67, 68, 'Three',
                            'Five', 71, 'Three', 73, 74, 'ThreeFive', 76, 77, 'Three',
                            79, 'Five', 'Three', 82, 83, 'Three', 'Five', 86, 'Three', 88, 89,
                            'ThreeFive', 91, 92, 'Three', 94, 'Five', 'Three', 97, 98, 'Three', 'Five']
        results = list(solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index))
        for expected_result, result in zip(expected_results, results):
            self.assertEqual(expected_result, result)

    def test_output_empty_parameters_returns_type(self):
        results = solution.fizz_buzz()
        self.assertEqual(types.GeneratorType, type(results))

    def test_output_length_fizz_buzz_from_one_to_hundred(self):
        expected_result = 100
        results = solution.fizz_buzz(
            self.default_beginning_index, self.default_ending_index)
        self.assertEqual(len(list(results)), expected_result)

    def test_output_135_returns_threefive_string(self):
        expected_result = 'ThreeFive'
        index = 135
        results = solution.fizz_buzz(self.default_beginning_index, 200, index)
        self.assertEqual(next(results), expected_result)

    def test_output_1440_returns_threefive_string(self):
        expected_result = 'ThreeFive'
        index = 1440
        results = solution.fizz_buzz(self.default_beginning_index, 2000, 1440)
        self.assertEqual(next(results), expected_result)

    def test_output_7368_returns_three_string(self):
        expected_result = 'Three'
        index = 7368
        results = solution.fizz_buzz(self.default_beginning_index, 8000, index)
        self.assertEqual(next(results), expected_result)

    def test_output_148140_not_returns_five_string(self):
        error_result = 'Three'
        index = 148140
        results = solution.fizz_buzz(1, 200000, index)
        self.assertNotEqual(next(results), error_result)

    def test_output_6_not_returns_integer_type(self):
        index = 6
        results = solution.fizz_buzz(key=index)
        self.assertNotEqual(type(next(results)), int)


if __name__ == '__main__':
    unittest.main()
