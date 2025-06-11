#!/usr/bin/env python3
"""
Clean Code in Python

This module demonstrates Python best practices and "Pythonic" code examples
that a senior Python developer should be familiar with.

Topics covered:
- PEP 8 style guidelines
- Idiomatic Python ("Pythonic" code)
- Code organization and structure
- Naming conventions
- Documentation standards
- Effective use of built-in functions and libraries
"""
from typing import List, Dict, Any, Optional, Tuple, Callable, Iterator
import collections
import functools
import itertools
import datetime
import re


def demonstrate_pep8_guidelines():
    """
    Demonstrates PEP 8 style guidelines.
    
    PEP 8 is the official style guide for Python code and covers topics like:
    - Indentation (4 spaces)
    - Maximum line length (79 characters for code, 72 for comments/docstrings)
    - Imports organization
    - Whitespace usage
    - Naming conventions
    - Comments and documentation
    
    This function shows examples of proper PEP 8 style.
    """
    print("\n=== PEP 8 STYLE GUIDELINES ===")
    
    # Proper indentation and whitespace
    if True:
        # 4 spaces for indentation
        print("Properly indented code")
    
    # Proper spacing around operators
    x = 1 + 2 * 3 / 4
    
    # Proper spacing after commas
    my_list = [1, 2, 3, 4, 5]
    
    # Proper line breaks for long lines
    long_string = (
        "This is a very long string that would exceed the recommended "
        "line length limit of 79 characters if written on a single line."
    )
    
    # Proper naming conventions
    CONSTANT_VALUE = 42
    global_variable = "global"
    
    def function_name(parameter_one, parameter_two):
        local_variable = parameter_one + parameter_two
        return local_variable
    
    class MyClass:
        class_variable = "class"
        
        def __init__(self):
            self.instance_variable = "instance"
        
        def method_name(self):
            return self.instance_variable
    
    # Show examples in output
    print("PEP 8 naming conventions:")
    print(f"- CONSTANT_VALUE: {CONSTANT_VALUE}")
    print(f"- global_variable: {global_variable}")
    print(f"- function_name: {function_name(1, 2)}")
    
    my_instance = MyClass()
    print(f"- MyClass.class_variable: {MyClass.class_variable}")
    print(f"- my_instance.instance_variable: {my_instance.instance_variable}")
    print(f"- my_instance.method_name(): {my_instance.method_name()}")


def demonstrate_pythonic_code():
    """
    Demonstrates idiomatic Python code ("Pythonic" code).
    
    Pythonic code leverages Python's unique features and philosophy to write
    code that is more readable, expressive, and efficient.
    """
    print("\n=== PYTHONIC CODE ===")
    
    # Unpacking
    print("Unpacking:")
    a, b, c = [1, 2, 3]
    print(f"a={a}, b={b}, c={c}")
    
    # Extended unpacking (Python 3.0+)
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"first={first}, middle={middle}, last={last}")
    
    # Swapping values
    print("\nSwapping values:")
    a, b = 1, 2
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    
    # List comprehensions instead of loops
    print("\nList comprehensions:")
    numbers = [1, 2, 3, 4, 5]
    
    # Non-Pythonic way
    squares_non_pythonic = []
    for num in numbers:
        squares_non_pythonic.append(num ** 2)
    
    # Pythonic way
    squares_pythonic = [num ** 2 for num in numbers]
    
    print(f"Non-Pythonic result: {squares_non_pythonic}")
    print(f"Pythonic result: {squares_pythonic}")
    
    # Dictionary comprehensions
    print("\nDictionary comprehensions:")
    dict_comp = {str(num): num ** 2 for num in range(1, 6)}
    print(f"Dictionary comprehension result: {dict_comp}")
    
    # Enumerate instead of manual indexing
    print("\nEnumerate:")
    fruits = ['apple', 'banana', 'cherry']
    
    # Non-Pythonic way
    print("Non-Pythonic indexing:")
    for i in range(len(fruits)):
        print(f"{i}: {fruits[i]}")
    
    # Pythonic way
    print("Pythonic indexing with enumerate:")
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")
    
    # Using 'in' for membership testing
    print("\nMembership testing:")
    if 'apple' in fruits:
        print("'apple' is in the list")
    
    # Default dictionaries
    print("\nDefaultdict:")
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    
    # Non-Pythonic way
    word_counts_non_pythonic = {}
    for word in words:
        if word not in word_counts_non_pythonic:
            word_counts_non_pythonic[word] = 0
        word_counts_non_pythonic[word] += 1
    
    # Pythonic way
    word_counts_pythonic = collections.defaultdict(int)
    for word in words:
        word_counts_pythonic[word] += 1
    
    print(f"Non-Pythonic word counts: {dict(word_counts_non_pythonic)}")
    print(f"Pythonic word counts: {dict(word_counts_pythonic)}")
    
    # Counter (even more Pythonic)
    word_counts_counter = collections.Counter(words)
    print(f"Using Counter: {dict(word_counts_counter)}")
    
    # Context managers (with statement)
    print("\nContext managers:")
    try:
        with open('/tmp/example.txt', 'w') as f:
            f.write('Hello, world!')
        print("File written successfully")
        
        with open('/tmp/example.txt', 'r') as f:
            content = f.read()
        print(f"File content: {content}")
    except IOError as e:
        print(f"File operation failed: {e}")
    
    # String formatting (f-strings, Python 3.6+)
    print("\nString formatting:")
    name = "Alice"
    age = 30
    
    # Old way (%s)
    old_style = "Name: %s, Age: %d" % (name, age)
    print(f"Old style: {old_style}")
    
    # str.format()
    format_style = "Name: {}, Age: {}".format(name, age)
    print(f"str.format(): {format_style}")
    
    # f-strings (Python 3.6+)
    f_string = f"Name: {name}, Age: {age}"
    print(f"f-string: {f_string}")
    
    # Expressions in f-strings
    print(f"f-string with expression: Name: {name.upper()}, Next year: {age + 1}")


def demonstrate_effective_functions():
    """
    Demonstrates effective function design in Python.
    """
    print("\n=== EFFECTIVE FUNCTIONS ===")
    
    # Default parameter values
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    print(f"Default parameter: {greet('Alice')}")
    print(f"Custom parameter: {greet('Bob', 'Hi')}")
    
    # Keyword arguments for clarity
    def create_person(name, age, city):
        return {"name": name, "age": age, "city": city}
    
    # Using keyword arguments makes the code more readable
    person = create_person(name="Charlie", age=25, city="New York")
    print(f"Person created with keyword args: {person}")
    
    # Variable number of arguments
    def sum_all(*args):
        return sum(args)
    
    print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
    print(f"Sum of 1 through 5: {sum_all(1, 2, 3, 4, 5)}")
    
    # Variable number of keyword arguments
    def print_attributes(**kwargs):
        return ", ".join(f"{k}={v}" for k, v in kwargs.items())
    
    attributes = print_attributes(name="Alice", age=30, city="London")
    print(f"Attributes: {attributes}")
    
    # Combining different parameter types
    def process_data(required, *args, default="Default", **kwargs):
        result = {
            "required": required,
            "args": args,
            "default": default,
            "kwargs": kwargs
        }
        return result
    
    data = process_data("Required", 1, 2, 3, default="Custom", a=1, b=2)
    print(f"Processed data: {data}")
    
    # Function annotations (Python 3.0+)
    def add(a: int, b: int) -> int:
        return a + b
    
    print(f"Annotated function: {add(2, 3)}")
    print(f"Function annotations: {add.__annotations__}")


def demonstrate_error_handling():
    """
    Demonstrates proper error handling in Python.
    """
    print("\n=== ERROR HANDLING ===")
    
    # Basic try-except
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught division by zero error")
    
    # Multiple exception types
    try:
        value = int("not a number")
    except (ValueError, TypeError) as e:
        print(f"Caught conversion error: {e}")
    
    # try-except-else-finally
    try:
        value = int("42")
    except ValueError:
        print("Not a valid number")
    else:
        print(f"Conversion successful: {value}")
    finally:
        print("This always executes")
    
    # Custom exceptions
    class ValidationError(Exception):
        """Exception raised for validation errors."""
        def __init__(self, message, field):
            self.message = message
            self.field = field
            super().__init__(f"{field}: {message}")
    
    def validate_age(age):
        if not isinstance(age, int):
            raise ValidationError("Must be an integer", "age")
        if age < 0:
            raise ValidationError("Cannot be negative", "age")
        if age > 120:
            raise ValidationError("Unrealistic value", "age")
        return age
    
    # Using the custom exception
    try:
        validate_age(150)
    except ValidationError as e:
        print(f"Validation failed: {e}")
    
    # Context manager for error handling
    class ErrorHandler:
        def __init__(self, error_msg):
            self.error_msg = error_msg
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print(f"{self.error_msg}: {exc_val}")
                return True  # Suppress the exception
            return False
    
    with ErrorHandler("Error occurred"):
        x = 1 / 0
    
    print("Execution continues after handled error")


def demonstrate_code_organization():
    """
    Demonstrates proper code organization and structure.
    """
    print("\n=== CODE ORGANIZATION ===")
    
    # Example of a well-structured module
    print("A well-structured Python module should have:")
    print("1. Module docstring at the top")
    print("2. Imports organized in groups:")
    print("   - Standard library imports")
    print("   - Related third-party imports")
    print("   - Local application/library specific imports")
    print("3. Constants and global variables")
    print("4. Class definitions")
    print("5. Function definitions")
    print("6. Main execution code (under if __name__ == '__main__')")
    
    # Example of proper import organization
    print("\nProper import organization:")
    import_example = """
    # Standard library imports
    import os
    import sys
    from datetime import datetime
    
    # Third-party imports
    import numpy as np
    import pandas as pd
    
    # Local application imports
    from myapp import models
    from myapp.utils import helpers
    """
    print(import_example)
    
    # Example of proper class structure
    print("\nProper class structure:")
    class_example = """
    class MyClass:
        \"\"\"Class docstring explaining purpose and usage.\"\"\"
        
        # Class variables
        class_var = "class variable"
        
        def __init__(self, param1, param2):
            \"\"\"Initialize the instance.\"\"\"
            self.param1 = param1
            self.param2 = param2
            self._private_var = None
        
        # Special methods
        def __str__(self):
            return f"MyClass({self.param1}, {self.param2})"
        
        # Public methods
        def public_method(self):
            \"\"\"Public method docstring.\"\"\"
            return self.param1
        
        # Private methods (by convention)
        def _private_method(self):
            \"\"\"Private method docstring.\"\"\"
            return self._private_var
    """
    print(class_example)


def demonstrate_documentation_standards():
    """
    Demonstrates proper documentation standards in Python.
    
    Python documentation typically follows specific formats:
    - Docstrings for modules, classes, and functions
    - Inline comments for complex code sections
    - Type hints for function parameters and return values
    
    This function shows examples of proper documentation.
    """
    print("\n=== DOCUMENTATION STANDARDS ===")
    
    # Example of a well-documented function with Google style docstring
    def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
        """
        Calculate basic statistics for a list of numbers.
        
        Args:
            numbers: A list of numbers to analyze
            
        Returns:
            A dictionary containing the mean, median, and standard deviation
            
        Raises:
            ValueError: If the input list is empty
            
        Examples:
            >>> calculate_statistics([1, 2, 3, 4, 5])
            {'mean': 3.0, 'median': 3.0, 'std_dev': 1.4142135623730951}
        """
        if not numbers:
            raise ValueError("Input list cannot be empty")
        
        n = len(numbers)
        mean = sum(numbers) / n
        
        # Calculate median
        sorted_numbers = sorted(numbers)
        if n % 2 == 0:
            median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            median = sorted_numbers[n//2]
        
        # Calculate standard deviation
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_dev = variance ** 0.5
        
        return {
            'mean': mean,
            'median': median,
            'std_dev': std_dev
        }
    
    # Show example usage
    try:
        stats = calculate_statistics([1, 2, 3, 4, 5])
        print(f"Statistics: {stats}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Print the docstring
    print("\nFunction docstring:")
    print(calculate_statistics.__doc__)
    
    # Example of inline comments
    print("\nExample of proper inline comments:")
    code_with_comments = """
    def complex_algorithm(data):
        # Initialize variables
        result = []
        seen = set()
        
        # First pass: remove duplicates
        for item in data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        
        # Second pass: transform items
        # We use a list comprehension for efficiency
        result = [transform(x) for x in result]
        
        return result
    """
    print(code_with_comments)


def demonstrate_built_in_functions():
    """
    Demonstrates effective use of Python's built-in functions.
    """
    print("\n=== EFFECTIVE USE OF BUILT-IN FUNCTIONS ===")
    
    # map, filter, reduce
    numbers = [1, 2, 3, 4, 5]
    
    # map
    squares = list(map(lambda x: x**2, numbers))
    print(f"map: {squares}")
    
    # filter
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter: {even}")
    
    # reduce
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print(f"reduce: {product}")
    
    # zip
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    people = list(zip(names, ages))
    print(f"zip: {people}")
    
    # any, all
    print(f"any even? {any(x % 2 == 0 for x in numbers)}")
    print(f"all positive? {all(x > 0 for x in numbers)}")
    
    # sorted with key
    words = ["apple", "banana", "cherry", "date"]
    sorted_by_length = sorted(words, key=len)
    print(f"sorted by length: {sorted_by_length}")
    
    # reversed
    print(f"reversed: {list(reversed(numbers))}")
    
    # enumerate
    for i, name in enumerate(names, 1):
        print(f"Person {i}: {name}")
    
    # sum, min, max
    print(f"sum: {sum(numbers)}")
    print(f"min: {min(numbers)}")
    print(f"max: {max(numbers)}")
    
    # round
    print(f"round(3.14159, 2): {round(3.14159, 2)}")
    
    # isinstance, type
    print(f"isinstance('hello', str): {isinstance('hello', str)}")
    print(f"type(42): {type(42)}")
    
    # dir
    print(f"Some attributes of a string: {dir('hello')[:5]}")


if __name__ == "__main__":
    print("CLEAN CODE IN PYTHON")
    print("===================")
    
    demonstrate_pep8_guidelines()
    demonstrate_pythonic_code()
    demonstrate_effective_functions()
    demonstrate_error_handling()
    demonstrate_code_organization()
    demonstrate_documentation_standards()
    demonstrate_built_in_functions()
