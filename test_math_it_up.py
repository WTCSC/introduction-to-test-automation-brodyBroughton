import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():

    assert math_it_up.is_even(2)
    assert not math_it_up.is_even(3)
    assert math_it_up.is_even(-2)
    assert not math_it_up.is_even(-3)

def test_is_odd():
    
    assert not math_it_up.is_odd(2)
    assert math_it_up.is_odd(3)
    assert not math_it_up.is_odd(-2)
    assert math_it_up.is_odd(-3)

def test_mean():
    
    assert math_it_up.mean([1,1]) == 1
    assert math_it_up.mean([-2,-2,-2]) == -2
    assert math_it_up.mean([1,2,3,4]) == 2.5

def test_median():
  
    assert math_it_up.median([1,2,3]) == 2
    assert math_it_up.median([2,3]) == 2.5
    assert math_it_up.median([-1,-1,-1]) == -1

def test_mode():
  
    assert math_it_up.mode([1,2,1,3,1,4]) == [1]
    assert math_it_up.mode([-2,3,-4,-2]) == [-2]
    assert math_it_up.mode([6]) == [6]
    assert math_it_up.mode([-5]) == [-5]
