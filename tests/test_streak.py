import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -4]) == 0

def test_mixed_numbers():
    assert longest_positive_streak([1, 2, -1, 4, 5, 6, 0, 8]) == 3

def test_streak_at_beginning():
    assert longest_positive_streak([1, 2, 3, -5, 4]) == 3

def test_streak_at_end():
    assert longest_positive_streak([-1, 0, 5, 6, 7, 8]) == 4

def test_no_positive_numbers():
    assert longest_positive_streak([0, -1, -2, -3]) == 0

def test_single_positive():
    assert longest_positive_streak([5]) == 1

def test_single_non_positive():
    assert longest_positive_streak([-5]) == 0

def test_zeros():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_alternating():
    assert longest_positive_streak([1, -1, 2, -2, 3, -3]) == 1
