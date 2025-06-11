#!/usr/bin/env python3
"""
Basic pytest examples

This module demonstrates fundamental pytest concepts that a senior Python developer
should be familiar with, including:
- Basic test functions
- Test assertions
- Test discovery
- Test organization
- Expected exceptions
"""
import pytest


# A simple function to test
def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Basic test function
def test_add():
    """Test the add function with positive numbers."""
    # Arrange
    a, b = 2, 3
    expected = 5
    
    # Act
    result = add(a, b)
    
    # Assert
    assert result == expected


# Test with negative numbers
def test_add_negative():
    """Test the add function with negative numbers."""
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0


# Multiple assertions in one test
def test_add_multiple_assertions():
    """Test the add function with multiple assertions."""
    assert add(0, 0) == 0
    assert add(1, 0) == 1
    assert add(0, 1) == 1


# Testing for expected exceptions
def test_divide_by_zero():
    """Test that divide raises ValueError when dividing by zero."""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    
    # Optionally check the exception message
    assert "Cannot divide by zero" in str(excinfo.value)


# Test with expected failure
@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_failure():
    """This test is expected to fail."""
    assert 1 == 2


# Test with skip
@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    """This test is skipped."""
    assert True


# Conditional skip
@pytest.mark.skipif(True, reason="This test is conditionally skipped")
def test_conditional_skip():
    """This test is conditionally skipped."""
    assert True


# Test classes can be used to group related tests
class TestMathFunctions:
    """Test class for math functions."""
    
    def test_add_in_class(self):
        """Test the add function within a class."""
        assert add(2, 3) == 5
    
    def test_divide_in_class(self):
        """Test the divide function within a class."""
        assert divide(10, 2) == 5


# Tests can be organized by functionality
class TestAddFunction:
    """Tests specifically for the add function."""
    
    def test_add_integers(self):
        """Test adding integers."""
        assert add(1, 2) == 3
    
    def test_add_floats(self):
        """Test adding floats."""
        assert add(1.5, 2.5) == 4.0
    
    def test_add_mixed(self):
        """Test adding an integer and a float."""
        assert add(1, 2.5) == 3.5


class TestDivideFunction:
    """Tests specifically for the divide function."""
    
    def test_divide_integers(self):
        """Test dividing integers."""
        assert divide(10, 2) == 5
    
    def test_divide_floats(self):
        """Test dividing floats."""
        assert divide(5.0, 2.5) == 2.0
    
    def test_divide_mixed(self):
        """Test dividing an integer by a float."""
        assert divide(10, 4.0) == 2.5


if __name__ == "__main__":
    # This allows running the tests with python test_basic.py
    # However, it's better to use pytest command line
    pytest.main(["-v", __file__])
