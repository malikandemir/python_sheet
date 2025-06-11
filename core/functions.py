#!/usr/bin/env python3
"""
Advanced Function Concepts in Python

This module demonstrates advanced function concepts that a senior Python developer
should be familiar with, including:
- First-class functions
- Closures
- Decorators
- Function annotations
- Lambda functions
- Higher-order functions
- Generators and coroutines
"""
import functools
import time
from typing import Callable, List, Dict, Any, TypeVar, Generator, Iterator

T = TypeVar('T')  # Generic type variable for type hints


def demonstrate_first_class_functions():
    """
    Demonstrates that functions in Python are first-class objects.
    First-class objects can be:
    - Assigned to variables
    - Passed as arguments to functions
    - Returned from functions
    - Stored in data structures
    """
    print("\n=== FIRST-CLASS FUNCTIONS ===")
    
    # Assigning functions to variables
    def greet(name):
        return f"Hello, {name}!"
    
    greeting_function = greet
    print(f"Function assigned to variable: {greeting_function('Alice')}")
    
    # Storing functions in data structures
    function_list = [str.lower, str.upper, str.title]
    text = "Python is Awesome"
    
    print("Functions stored in a list:")
    for func in function_list:
        print(f"  {func.__name__}: {func(text)}")
    
    # Functions as arguments (higher-order functions)
    def apply_function(func, value):
        return func(value)
    
    print(f"Function as argument: {apply_function(len, 'Python')}")
    print(f"Function as argument: {apply_function(str.upper, 'python')}")
    
    # Returning functions from functions
    def get_multiplier(factor):
        def multiply(x):
            return x * factor
        return multiply
    
    double = get_multiplier(2)
    triple = get_multiplier(3)
    
    print(f"Function returned from function (double): {double(5)}")
    print(f"Function returned from function (triple): {triple(5)}")


def demonstrate_closures():
    """
    Demonstrates closures in Python.
    A closure is a function that remembers the values from the enclosing lexical scope
    even when the program flow is no longer in that scope.
    """
    print("\n=== CLOSURES ===")
    
    def create_counter(start=0):
        """Creates a counter function that remembers its state."""
        count = [start]  # Using a list as mutable object
        
        def increment(step=1):
            count[0] += step
            return count[0]
        
        return increment
    
    # Create counters with different starting points
    counter1 = create_counter(10)
    counter2 = create_counter(100)
    
    print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
    print(f"Counter2: {counter2()}, {counter2()}, {counter2()}")
    print(f"Counter1 again: {counter1()}")
    
    # Accessing the closure variables
    print(f"Closure variables: {counter1.__closure__[0].cell_contents}")
    
    # Practical example: Function factory
    def power_function(exponent):
        def power_of(base):
            return base ** exponent
        return power_of
    
    square = power_function(2)
    cube = power_function(3)
    
    print(f"Square of 4: {square(4)}")
    print(f"Cube of 3: {cube(3)}")


def demonstrate_decorators():
    """
    Demonstrates decorators in Python.
    Decorators are a way to modify or enhance functions without changing their code.
    """
    print("\n=== DECORATORS ===")
    
    # Simple decorator
    def simple_decorator(func):
        @functools.wraps(func)  # Preserves the original function's metadata
        def wrapper(*args, **kwargs):
            print(f"Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"After calling {func.__name__}")
            return result
        return wrapper
    
    # Applying the decorator
    @simple_decorator
    def say_hello(name):
        print(f"Hello, {name}!")
        return f"Hello, {name}!"
    
    result = say_hello("Bob")
    print(f"Function returned: {result}")
    print(f"Function name: {say_hello.__name__}")  # Without @wraps this would be 'wrapper'
    
    # Decorator with arguments
    def repeat(n=1):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(n):
                    results.append(func(*args, **kwargs))
                return results
            return wrapper
        return decorator
    
    @repeat(3)
    def say_hi(name):
        return f"Hi, {name}!"
    
    print(f"\nRepeated function: {say_hi('Charlie')}")
    
    # Practical decorator: timing function execution
    def timing_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
            return result
        return wrapper
    
    @timing_decorator
    def slow_function():
        time.sleep(0.5)
        return "Function completed"
    
    print(f"\nTiming decorator: {slow_function()}")
    
    # Class-based decorator
    class CountCalls:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func
            self.count = 0
            
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"{self.func.__name__} has been called {self.count} times")
            return self.func(*args, **kwargs)
    
    @CountCalls
    def say_goodbye(name):
        return f"Goodbye, {name}!"
    
    print(f"\nClass-based decorator:")
    print(say_goodbye("Alice"))
    print(say_goodbye("Bob"))
    print(say_goodbye("Charlie"))


def demonstrate_function_annotations():
    """
    Demonstrates function annotations and type hints in Python.
    """
    print("\n=== FUNCTION ANNOTATIONS AND TYPE HINTS ===")
    
    # Basic function annotations
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    print(f"Function: {greet('Dave')}")
    print(f"Annotations: {greet.__annotations__}")
    
    # More complex type hints
    def process_items(items: List[str], options: Dict[str, Any] = None) -> List[str]:
        if options is None:
            options = {}
        
        processed = []
        for item in items:
            if options.get('upper', False):
                item = item.upper()
            if options.get('reverse', False):
                item = item[::-1]
            processed.append(item)
        
        return processed
    
    items = ["apple", "banana", "cherry"]
    options = {"upper": True, "reverse": True}
    
    print(f"Processed items: {process_items(items, options)}")
    print(f"Complex annotations: {process_items.__annotations__}")
    
    # Higher-order function with type hints
    def apply_to_list(func: Callable[[T], T], items: List[T]) -> List[T]:
        return [func(item) for item in items]
    
    numbers = [1, 2, 3, 4, 5]
    doubled = apply_to_list(lambda x: x * 2, numbers)
    print(f"Doubled numbers: {doubled}")


def demonstrate_lambda_functions():
    """
    Demonstrates lambda functions (anonymous functions) in Python.
    """
    print("\n=== LAMBDA FUNCTIONS ===")
    
    # Simple lambda function
    square = lambda x: x**2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple arguments
    add = lambda x, y: x + y
    print(f"5 + 3 = {add(5, 3)}")
    
    # Lambda with conditional expression
    is_even = lambda x: True if x % 2 == 0 else False
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 5 even? {is_even(5)}")
    
    # Lambda in higher-order functions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Using lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")
    
    # Using lambda with map
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers: {squared_numbers}")
    
    # Using lambda with sorted
    pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
    sorted_by_second = sorted(pairs, key=lambda pair: pair[1])
    print(f"Sorted by second element: {sorted_by_second}")
    
    # Immediately invoked lambda expression (IILE)
    result = (lambda x, y: x + y)(5, 3)
    print(f"IILE result: {result}")


def demonstrate_functional_programming():
    """
    Demonstrates functional programming concepts in Python.
    """
    print("\n=== FUNCTIONAL PROGRAMMING ===")
    
    # map, filter, reduce
    from functools import reduce
    
    numbers = [1, 2, 3, 4, 5]
    
    # map: Apply function to each item
    squared = list(map(lambda x: x**2, numbers))
    print(f"map (squared): {squared}")
    
    # filter: Keep only items that match predicate
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter (evens): {evens}")
    
    # reduce: Accumulate values
    sum_all = reduce(lambda x, y: x + y, numbers)
    print(f"reduce (sum): {sum_all}")
    
    # all, any
    print(f"all numbers > 0: {all(x > 0 for x in numbers)}")
    print(f"any number > 4: {any(x > 4 for x in numbers)}")
    
    # Function composition
    def compose(*functions):
        def inner(arg):
            result = arg
            for f in reversed(functions):
                result = f(result)
            return result
        return inner
    
    def add_one(x):
        return x + 1
    
    def double(x):
        return x * 2
    
    def square(x):
        return x**2
    
    # Compose functions: square(double(add_one(x)))
    composed = compose(square, double, add_one)
    print(f"Composed function with x=3: {composed(3)}")  # (3+1)*2^2 = 16
    
    # Partial functions
    from functools import partial
    
    def power(base, exponent):
        return base ** exponent
    
    square_func = partial(power, exponent=2)
    cube_func = partial(power, exponent=3)
    
    print(f"Partial function (square of 4): {square_func(4)}")
    print(f"Partial function (cube of 3): {cube_func(3)}")


def demonstrate_generators():
    """
    Demonstrates generators and generator expressions in Python.
    """
    print("\n=== GENERATORS ===")
    
    # Simple generator function
    def count_up_to(n):
        i = 0
        while i < n:
            yield i
            i += 1
    
    # Using the generator
    counter = count_up_to(5)
    print(f"Generator type: {type(counter)}")
    
    print("Generator values:")
    for num in counter:
        print(f"  {num}")
    
    # Generator expression (like list comprehension but lazy)
    squares_gen = (x**2 for x in range(5))
    print(f"Generator expression type: {type(squares_gen)}")
    
    print("Generator expression values:")
    for square in squares_gen:
        print(f"  {square}")
    
    # Infinite generator
    def infinite_sequence():
        num = 0
        while True:
            yield num
            num += 1
    
    # Taking only what we need from an infinite generator
    gen = infinite_sequence()
    first_five = [next(gen) for _ in range(5)]
    print(f"First five from infinite generator: {first_five}")
    
    # Generator with send
    def echo_generator():
        value = yield "Ready"
        while True:
            value = yield f"Got: {value}"
    
    echo = echo_generator()
    print(f"Initial: {next(echo)}")  # Prime the generator
    print(f"Send 'Hello': {echo.send('Hello')}")
    print(f"Send 123: {echo.send(123)}")
    
    # Generator pipeline
    def pipeline_generator() -> Generator[int, None, None]:
        for i in range(5):
            yield i
    
    def double_generator(gen: Iterator[int]) -> Generator[int, None, None]:
        for num in gen:
            yield num * 2
    
    def add_one_generator(gen: Iterator[int]) -> Generator[int, None, None]:
        for num in gen:
            yield num + 1
    
    # Building a pipeline
    pipeline = add_one_generator(double_generator(pipeline_generator()))
    print("Generator pipeline results:")
    for result in pipeline:
        print(f"  {result}")


if __name__ == "__main__":
    print("ADVANCED FUNCTION CONCEPTS IN PYTHON")
    print("===================================")
    
    demonstrate_first_class_functions()
    demonstrate_closures()
    demonstrate_decorators()
    demonstrate_function_annotations()
    demonstrate_lambda_functions()
    demonstrate_functional_programming()
    demonstrate_generators()
