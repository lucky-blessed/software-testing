# ==============================================================================
# ALL COLLECTED CODE - COMPLETED CHALLENGES ONLY
# Generated: 2026-01-21 18:15:08
# Total Completed Challenges: 7
# Note: Only challenges that passed all tests are included
# ==============================================================================


# ==============================================================================
# Challenge 1: First Pytest Test ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

def add(a, b):
   # TODO: Implement addition
   return a + b

def test_add():
   # TODO: Write test to check add(2, 3) equals 5
   assert add(2, 3) == 5


# ==============================================================================
# Challenge 2: Multiple Assertions ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

def multiply(a, b):
   # TODO: Implement multiplication
   return a * b

def test_multiply():
   # TODO: Test multiply(2, 3) == 6
   # TODO: Test multiply(5, 0) == 0
   # TODO: Test multiply(-1, 5) == -5
   assert multiply(2, 3) == 6
   assert multiply(5, 0) == 0
   assert multiply(-1, 5) == -5 


# ==============================================================================
# Challenge 3: Testing Exceptions ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def divide(a, b):
   # TODO: Implement division, raise ValueError if b is 0
   if b == 0:
      raise ValueError("Cannot divide by zero")

def test_divide_by_zero():
   # TODO: Use pytest.raises to test ValueError is raised
   assert divide(10, 2) == 5
   with pytest.raises(ValueError):
      divide(10, 0)


# ==============================================================================
# Challenge 4: Parametrized Tests ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def is_even(n):
   # TODO: Return True if n is even, False otherwise
   if (n % 2 == 0):
      return True
   else:
      return False

# TODO: Add @pytest.mark.parametrize decorator
# Test with: (2, True), (3, False), (0, True), (-4, True)
def test_is_even():
   # TODO: Add parameters and assertion
   assert is_even(2) == True
   @pytest.mark.paramtrize("test_input, expected", [(2, True), (3, False), (0, True), (-4, True)])


# ==============================================================================
# Challenge 5: Basic Fixtures ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

#import pytest

# TODO: Create a fixture named 'sample_list' that returns [1, 2, 3, 4, 5]

@pytest.fixture
def sample_list():
   return [1,2,3,4,5]

def test_list_length(sample_list):
   # TODO: Assert length is 5
   assert len(sample_list) == 5

def test_list_sum(sample_list):
   # TODO: Assert sum is 15
   assert sum(sample_list) == 15


# ==============================================================================
# Challenge 6: Testing Calculator Module ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# Type: Multi-File Project
# ==============================================================================

# --- File: calculator.py ---
def add(a, b):
   # TODO: Implement addition
   return a + b

def subtract(a, b):
   # TODO: Implement subtraction
   return a - b

def multiply(a, b):
   #TODO: Implement multiplication
   return a * b

# --- File: test_calculator.py ---
import pytest
from calculator import add, subtract, multiply

def test_add():
    # TODO: Test addition (5 + 3 should equal 8)
    assert add(5, 3) == 8

def test_subtract():
    # TODO: Test subtraction (10 - 4 should equal 6)
    assert subtract(10, 4) == 6

def test_multiply():
    # TODO: Test multiplication (3 * 7 should equal 21)
    assert multiply(3, 7) == 21



# ==============================================================================
# Challenge 7: Testing with Approximate Values ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def calculate_average(numbers):
   # TODO: Return the average of numbers
   average = sum(numbers) / len(numbers)
   return average

def test_average():
   # TODO: Test that average of [1, 2, 3] is approximately 2.0
   # TODO: Test that average of [1.5, 2.5, 3.0] is approximately 2.333
   # Use pytest.approx for floating point comparison
   assert calculate_average([1, 2, 3]) == pytest.approx(2.0)
   assert calculate_average([1.5, 2.5, 3.0]) == pytest.approx(2.333)
