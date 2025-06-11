#!/usr/bin/env python3
"""
Pytest Parameterized Tests Examples

This module demonstrates how to use pytest's parameterization features to run
the same test with different inputs, which is a powerful way to test multiple
scenarios without duplicating code.

Topics covered:
- Basic parameterization with @pytest.mark.parametrize
- Multiple parameters
- Combining parameterized tests with fixtures
- Parameterizing test classes
- Indirect parameterization
"""
import pytest
import math
from typing import List, Dict, Any, Tuple, Union


# Functions to test
def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def calculate_circle_area(radius):
    """Calculate the area of a circle with the given radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


# Basic parameterization
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (-1, -1, -2),
    (0, 0, 0),
    (10, -5, 5)
])
def test_add(a, b, expected):
    """Test the add function with multiple inputs."""
    assert add(a, b) == expected


# Multiple parameters with different names
@pytest.mark.parametrize("input_string, expected_result", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),  # Empty string is a palindrome
    ("a", True),  # Single character is a palindrome
    ("Ab ba", True),  # Case insensitive
])
def test_is_palindrome(input_string, expected_result):
    """Test the is_palindrome function with multiple inputs."""
    assert is_palindrome(input_string) == expected_result


# Multiple parameterize decorators (creates a test for each combination)
@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [10, 20])
def test_multiply_combinations(a, b):
    """
    Test the multiply function with combinations of inputs.
    
    This will create 6 tests (3 values for a × 2 values for b).
    """
    result = multiply(a, b)
    assert result == a * b
    assert isinstance(result, int)


# Parameterizing with ids for better test naming
@pytest.mark.parametrize("radius, expected", [
    (0, 0),
    (1, math.pi),
    (2, 4 * math.pi),
], ids=["zero_radius", "unit_circle", "radius_two"])
def test_circle_area(radius, expected):
    """Test the calculate_circle_area function with named test cases."""
    assert calculate_circle_area(radius) == pytest.approx(expected)


# Parameterized test with expected exceptions
@pytest.mark.parametrize("invalid_radius", [-1, -100])
def test_circle_area_with_invalid_radius(invalid_radius):
    """Test that calculate_circle_area raises ValueError for negative radius."""
    with pytest.raises(ValueError) as excinfo:
        calculate_circle_area(invalid_radius)
    assert "Radius cannot be negative" in str(excinfo.value)


# Combining parameterization with fixtures
@pytest.fixture
def number_fixture():
    """A simple fixture that returns a number."""
    return 10


@pytest.mark.parametrize("multiplier, expected", [
    (0, 0),
    (1, 10),
    (2, 20),
])
def test_with_fixture_and_params(number_fixture, multiplier, expected):
    """
    Test combining a fixture with parameterization.
    
    This demonstrates how to use both fixtures and parameterized inputs.
    """
    result = number_fixture * multiplier
    assert result == expected


# Parameterizing a test class
@pytest.mark.parametrize("operation, expected", [
    ("add", 5),
    ("multiply", 6),
])
class TestMathOperations:
    """
    Test class with parameterized tests.
    
    This demonstrates how to apply parameterization to all methods in a class.
    """
    
    def test_positive_numbers(self, operation, expected):
        """Test with positive numbers."""
        a, b = 2, 3
        if operation == "add":
            result = add(a, b)
        else:  # multiply
            result = multiply(a, b)
        assert result == expected
    
    def test_with_zero(self, operation, expected):
        """Test with zero as one of the operands."""
        if operation == "add":
            result = add(expected, 0)
        else:  # multiply
            result = multiply(expected, 1)  # For multiply, using 1 instead of 0
        assert result == expected


# Indirect parameterization
@pytest.fixture
def db_data(request):
    """
    A fixture that provides different test data based on the parameter.
    
    This demonstrates indirect parameterization, where the parameter is used
    to customize a fixture rather than being passed directly to the test.
    """
    param = request.param
    
    if param == "users":
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    elif param == "products":
        return [
            {"id": 1, "name": "Product A", "price": 10.0},
            {"id": 2, "name": "Product B", "price": 20.0}
        ]
    else:
        return []


@pytest.mark.parametrize("db_data, expected_count", [
    ("users", 2),
    ("products", 2),
    ("empty", 0)
], indirect=["db_data"])  # This tells pytest to pass the parameter to the fixture
def test_indirect_parameterization(db_data, expected_count):
    """
    Test using indirect parameterization.
    
    This demonstrates how to use a parameter to customize a fixture.
    """
    assert len(db_data) == expected_count


# Parameterizing with complex data structures
test_data = [
    {
        "input": {"numbers": [1, 2, 3, 4, 5], "operation": "sum"},
        "expected": 15
    },
    {
        "input": {"numbers": [1, 2, 3, 4, 5], "operation": "average"},
        "expected": 3.0
    },
    {
        "input": {"numbers": [2, 4, 6, 8], "operation": "product"},
        "expected": 384
    }
]


def perform_operation(data):
    """Perform the specified operation on the numbers."""
    numbers = data["numbers"]
    operation = data["operation"]
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError(f"Unknown operation: {operation}")


@pytest.mark.parametrize("test_case", test_data, ids=lambda tc: tc["input"]["operation"])
def test_perform_operation(test_case):
    """
    Test the perform_operation function with complex test cases.
    
    This demonstrates how to use complex data structures as test parameters.
    """
    result = perform_operation(test_case["input"])
    assert result == test_case["expected"]


# Parameterized tests with custom logic
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Generate test cases programmatically
prime_test_cases = []
for i in range(20):
    prime_test_cases.append((i, is_prime(i)))


@pytest.mark.parametrize("number, expected", prime_test_cases)
def test_is_prime(number, expected):
    """
    Test the is_prime function with programmatically generated test cases.
    
    This demonstrates how to generate test cases programmatically.
    """
    assert is_prime(number) == expected


if __name__ == "__main__":
    # This allows running the tests with python test_parametrize.py
    # However, it's better to use pytest command line
    pytest.main(["-v", __file__])
