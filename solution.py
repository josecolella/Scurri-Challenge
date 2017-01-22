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

import itertools
import typing


def fizz_buzz(beginning_number: int = 1, ending_number: int = 100, key: int=None):
    """Returns a generator that yields an integer or a string after verifying
    if the integer from `beginning_number` to `ending_number` is divisible by 3, 5
    or 15

    Args:
        beginning_number: The integer that denotes the beginning of the sequence
        ending_number: The integer that denotes the end of the sequence
        key: An optional integer that when specified only returns the result for the key
    Returns:
        A generator that yields an integer or a string based on the following conditions:
        - the string is `ThreeFive` if the integer is divisible by 3 and 5,
        -`Three` if integer is only divisible by 3,
        - `Five` if integer is only divisible by 5.
        - the integer if none of the above conditions apply
    """

    if beginning_number > ending_number:
        raise ValueError(
            "`beginning_number` should be less than `ending_number`")
    if beginning_number < 0:
        raise ValueError("`beginning_number` should be greater than 0")
    if ending_number < 0:
        raise ValueError("`ending_number` should be greater than 0")
    result_list = None
    # Create set with range from `beginning_number` to `ending_number`
    # inclusive
    all_numbers = set(range(beginning_number, ending_number + 1))
    # Create three buckets; 1. Multiple of 3 and 5. 2. Multiple of 3. 3.
    # Multiple of 5
    multiple_three = set(filter(lambda x: x % 3 == 0, all_numbers))
    multiple_five = set(filter(lambda x: x % 5 == 0, all_numbers))

    # Create a set with the remaining numbers that do not fullfill the
    # conditions
    remaining_numbers = all_numbers.difference(multiple_three, multiple_five)
    # Set that is interesection of numbers that are multiple of 3 and multiple
    # of 5
    multiple_both = multiple_three.intersection(multiple_five)
    # Set that contains multiples of three that are not also multiples of 5
    multiple_three_restrict = multiple_three.difference(multiple_both)
    # Set that contains multiples of five that are not also multiples of 3
    multiple_five_restrict = multiple_five.difference(multiple_both)

    # Create transformations for printing
    transform_remaining_numbers = map(lambda x: (x, ''), remaining_numbers)
    transform_multiple_both = map(lambda x: (x, 'ThreeFive'), multiple_both)
    transform_multiple_five = map(lambda x: (x, 'Five'), multiple_five_restrict)
    transform_multiple_three = map(lambda x: (x, 'Three'), multiple_three_restrict)

    # Create sorted list, that is sorted based on the first index: integer
    transformed_result_list = sorted(
        itertools.chain(transform_remaining_numbers,
                        transform_multiple_both,
                        transform_multiple_five,
                        transform_multiple_three
                        ), key=lambda x: x[0])
    # Create clean result list
    clean_result_tuple = lambda result_tuple: result_tuple[0] if result_tuple[1] is '' else result_tuple[1]
    result_list = (clean_result_tuple(trans_tuple)
                   for trans_tuple in transformed_result_list)
    if key is not None:
        result_list = itertools.islice(result_list, key - 1, key)

    return result_list
