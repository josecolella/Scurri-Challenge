#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import print_function
import solution


if __name__ == '__main__':
    beginning_index = 1
    ending_index = 100
    results = solution.fizz_buzz(beginning_index, ending_index)
    for result in results:
        print(result)
