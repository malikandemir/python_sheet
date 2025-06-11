#!/usr/bin/env python3
"""
Pytest Fixtures Examples

This module demonstrates the use of pytest fixtures, which are a powerful feature
for setting up test environments, sharing resources, and managing test dependencies.

Topics covered:
- Basic fixtures
- Fixture scopes
- Parameterized fixtures
- Fixture factories
- Autouse fixtures
- Fixture dependencies
"""
import pytest
import tempfile
import os
from typing import List, Dict, Any, Tuple


# Basic fixture
@pytest.fixture
def sample_data():
    """
    A simple fixture that returns sample data for tests.
    
    This fixture demonstrates the basic usage of pytest fixtures.
    """
    return [1, 2, 3, 4, 5]


def test_sample_data(sample_data):
    """Test using a basic fixture."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15


# Fixture with setup and teardown
@pytest.fixture
def temp_file():
    """
    A fixture that creates a temporary file and cleans it up after the test.
    
    This demonstrates setup and teardown functionality in fixtures.
    """
    # Setup
    fd, path = tempfile.mkstemp()
    with open(path, 'w') as f:
        f.write("Hello, World!")
    
    # Provide the resource
    yield path
    
    # Teardown
    os.close(fd)
    os.unlink(path)


def test_temp_file(temp_file):
    """Test using a fixture with setup and teardown."""
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Hello, World!"


# Fixture scopes
@pytest.fixture(scope="function")
def function_scope():
    """This fixture has function scope (default)."""
    print("\nSetting up function-scoped fixture")
    yield
    print("\nTearing down function-scoped fixture")


@pytest.fixture(scope="class")
def class_scope():
    """This fixture has class scope."""
    print("\nSetting up class-scoped fixture")
    yield
    print("\nTearing down class-scoped fixture")


@pytest.fixture(scope="module")
def module_scope():
    """This fixture has module scope."""
    print("\nSetting up module-scoped fixture")
    yield
    print("\nTearing down module-scoped fixture")


@pytest.fixture(scope="session")
def session_scope():
    """This fixture has session scope."""
    print("\nSetting up session-scoped fixture")
    yield
    print("\nTearing down session-scoped fixture")


def test_scopes1(function_scope, module_scope, session_scope):
    """First test using fixtures with different scopes."""
    print("Running test_scopes1")


def test_scopes2(function_scope, module_scope, session_scope):
    """Second test using fixtures with different scopes."""
    print("Running test_scopes2")


class TestScopesInClass:
    """Test class to demonstrate class-scoped fixtures."""
    
    def test_scopes3(self, function_scope, class_scope, module_scope, session_scope):
        """First test in class using fixtures with different scopes."""
        print("Running test_scopes3")
    
    def test_scopes4(self, function_scope, class_scope, module_scope, session_scope):
        """Second test in class using fixtures with different scopes."""
        print("Running test_scopes4")


# Parameterized fixtures
@pytest.fixture(params=[1, 2, 3])
def number(request):
    """
    A parameterized fixture that provides different values for each test.
    
    This demonstrates how to create fixtures that run tests with different inputs.
    """
    return request.param


def test_parameterized_fixture(number):
    """Test using a parameterized fixture."""
    assert number in [1, 2, 3]


# Fixture with multiple parameters
@pytest.fixture(params=[
    (1, 2, 3),
    (4, 5, 9),
    (10, -5, 5)
])
def addition_data(request):
    """Fixture providing test cases for addition."""
    a, b, expected = request.param
    return a, b, expected


def test_addition(addition_data):
    """Test addition with multiple test cases."""
    a, b, expected = addition_data
    assert a + b == expected


# Fixture factories
@pytest.fixture
def make_dataset():
    """
    A fixture factory that creates datasets with specified properties.
    
    This demonstrates how to create flexible fixtures that can be customized
    for each test.
    """
    def _make_dataset(size=5, start=0, step=1):
        return list(range(start, start + size * step, step))
    
    return _make_dataset


def test_fixture_factory(make_dataset):
    """Test using a fixture factory."""
    # Create different datasets for different test cases
    small_dataset = make_dataset(3)
    assert small_dataset == [0, 1, 2]
    
    custom_dataset = make_dataset(size=4, start=10, step=2)
    assert custom_dataset == [10, 12, 14, 16]


# Autouse fixtures
@pytest.fixture(autouse=True)
def setup_test_environment():
    """
    An autouse fixture that runs for every test.
    
    This demonstrates fixtures that run automatically without being explicitly
    requested by test functions.
    """
    print("\nSetting up test environment")
    yield
    print("\nTearing down test environment")


def test_with_autouse_fixture():
    """This test will use the autouse fixture automatically."""
    print("Running test with autouse fixture")
    assert True


# Fixture dependencies
@pytest.fixture
def user():
    """Fixture providing a user."""
    return {"id": 1, "name": "Test User"}


@pytest.fixture
def user_posts(user):
    """
    Fixture that depends on another fixture.
    
    This demonstrates how fixtures can use other fixtures.
    """
    # This fixture depends on the user fixture
    return [
        {"id": 1, "user_id": user["id"], "title": "Post 1"},
        {"id": 2, "user_id": user["id"], "title": "Post 2"}
    ]


def test_user_posts(user, user_posts):
    """Test using fixtures with dependencies."""
    assert user["id"] == 1
    assert len(user_posts) == 2
    assert all(post["user_id"] == user["id"] for post in user_posts)


# Fixture with database simulation
class MockDatabase:
    """A mock database for testing."""
    
    def __init__(self):
        self.data = {}
    
    def insert(self, collection, document):
        """Insert a document into a collection."""
        if collection not in self.data:
            self.data[collection] = []
        document_copy = document.copy()
        document_copy["id"] = len(self.data[collection]) + 1
        self.data[collection].append(document_copy)
        return document_copy["id"]
    
    def find(self, collection, query=None):
        """Find documents in a collection."""
        if collection not in self.data:
            return []
        
        if query is None:
            return self.data[collection]
        
        result = []
        for doc in self.data[collection]:
            match = True
            for key, value in query.items():
                if key not in doc or doc[key] != value:
                    match = False
                    break
            if match:
                result.append(doc)
        
        return result


@pytest.fixture
def mock_db():
    """Fixture providing a mock database."""
    return MockDatabase()


@pytest.fixture
def populated_db(mock_db):
    """Fixture providing a populated mock database."""
    # Insert test data
    mock_db.insert("users", {"name": "Alice", "email": "alice@example.com"})
    mock_db.insert("users", {"name": "Bob", "email": "bob@example.com"})
    
    mock_db.insert("products", {"name": "Product 1", "price": 10.0})
    mock_db.insert("products", {"name": "Product 2", "price": 20.0})
    
    return mock_db


def test_find_users(populated_db):
    """Test finding users in the populated database."""
    users = populated_db.find("users")
    assert len(users) == 2
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Bob"


def test_find_products_by_price(populated_db):
    """Test finding products by price in the populated database."""
    products = populated_db.find("products", {"price": 20.0})
    assert len(products) == 1
    assert products[0]["name"] == "Product 2"


# conftest.py fixtures can be imported and used here
# They are defined in a separate file to be shared across multiple test modules


if __name__ == "__main__":
    # This allows running the tests with python test_fixtures.py
    # However, it's better to use pytest command line
    pytest.main(["-v", __file__])
