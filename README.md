# Python Mastery Project

This project demonstrates advanced Python concepts, best practices, and patterns that a senior Python developer should understand. It serves as both a learning resource and a reference for showcasing deep understanding of Python language features, runtime, and best practices.

## Project Structure and File Purposes

### Core Python Language Features (`core/`)

- **`data_structures.py`**: 
  - Advanced usage of Python's built-in data structures (lists, dictionaries, sets, tuples)
  - Collections module (Counter, deque, OrderedDict, ChainMap)
  - Heap queue algorithm implementation (heapq)
  - Performance characteristics and use cases for each data structure

- **`functions.py`**: 
  - First-class functions and higher-order functions
  - Closures and function factories
  - Decorators (function and class-based)
  - Function annotations and type hints
  - Lambda functions and functional programming (map, filter, reduce)
  - Generators and generator expressions

- **`oop.py`**: 
  - Class definition and instantiation
  - Inheritance and multiple inheritance
  - Method Resolution Order (MRO)
  - Encapsulation (public, protected, private attributes)
  - Class methods, static methods, and properties
  - Method overriding and super()

- **`oop_advanced.py`**: 
  - Abstract Base Classes (ABC)
  - Protocol classes and structural typing
  - Properties and descriptors
  - Metaclasses (Singleton, Registry patterns)
  - Dataclasses (mutable and immutable)
  - Context managers (class-based and decorator-based)

- **`async_programming.py`**: 
  - Asynchronous programming with asyncio
  - Coroutines, Tasks, and Futures
  - Async context managers and iterators
  - Synchronization primitives (locks, events, semaphores)
  - Running async code from synchronous code
  - Practical async examples

### Best Practices (`best_practices/`)

- **`clean_code.py`**: 
  - PEP 8 style guidelines
  - Idiomatic Python ("Pythonic" code)
  - Effective function design
  - Error handling best practices
  - Code organization principles
  - Documentation standards
  - Effective use of built-in functions

- **`testing/`**: Unit testing examples with pytest
  - **`test_basic.py`**: Basic pytest usage, assertions, and test organization
  - **`test_fixtures.py`**: Pytest fixtures for setup/teardown and test dependencies
  - **`test_parametrize.py`**: Parameterized tests for multiple test cases
  - **`test_mocking.py`**: Mocking external dependencies for isolated testing
  - **`conftest.py`**: Shared fixtures and pytest configuration

- **`error_handling.py`**: Proper exception handling patterns *(planned)*
- **`logging_example.py`**: Proper logging implementation *(planned)*

### Performance Considerations (`performance/`) *(planned)*

- **`memory_management.py`**: Memory optimization techniques
- **`profiling.py`**: Code profiling examples
- **`optimization.py`**: Code optimization techniques

### Project Example (`project_example/`) *(planned)*

A small but complete project demonstrating all concepts:
- Proper package structure
- Tests, documentation, and configuration
- Integration of all learned concepts

## How to Use This Project

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/malikandemir/python_sheet.git
   cd python_sheet
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Examples

Each module is executable as a standalone script and contains detailed comments explaining the concepts demonstrated:

```bash
# Run a specific module
python -m core.data_structures
python -m core.functions
python -m core.oop
python -m core.oop_advanced
python -m core.async_programming
python -m best_practices.clean_code
```

### Running the Tests

The project includes comprehensive pytest examples in the `best_practices/testing/` directory:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=.

# Run a specific test file
pytest best_practices/testing/test_basic.py
```

## Learning Path

For the best learning experience, follow this recommended path through the modules:

1. Start with `core/data_structures.py` to understand Python's fundamental building blocks
2. Move to `core/functions.py` to learn advanced function concepts
3. Continue with `core/oop.py` and `core/oop_advanced.py` for object-oriented programming
4. Explore `core/async_programming.py` for asynchronous programming concepts
5. Study `best_practices/clean_code.py` to understand Python coding standards
6. Examine the testing examples in `best_practices/testing/`

## Requirements

The project uses the following tools and libraries:

```
pytest==7.4.0
black==23.7.0
flake8==6.1.0
mypy==1.5.1
pytest-cov==4.1.0
memory-profiler==0.61.0
```

These can be installed via the requirements.txt file.
