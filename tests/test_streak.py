import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the longest streak is returned when multiple streaks exist."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, -1, 1]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([2, 3, 0, 5, 6, 7, 8]) == 4

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7]) == 3

def test_all_positive():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 1, 1, 1, 1]) == 5

def test_no_positive():
    """Test a case with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_example_from_description():
    """Test the primary example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3