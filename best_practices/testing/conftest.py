#!/usr/bin/env python3
"""
Pytest Shared Fixtures (conftest.py)

This module contains fixtures that are shared across multiple test modules.
Pytest automatically discovers and makes these fixtures available to all test
files in the same directory and subdirectories.

Topics covered:
- Shared fixtures
- Session-scoped fixtures
- Module-scoped fixtures
- Fixture factories
- Autouse fixtures for the entire test suite
"""
import pytest
import tempfile
import os
import json
from typing import Dict, List, Any, Callable


# Session-scoped fixture for a temporary directory
@pytest.fixture(scope="session")
def temp_dir():
    """
    Create a temporary directory for the entire test session.
    
    This fixture demonstrates how to create a resource that is shared
    across all tests in a session.
    """
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"\nCreated temporary directory: {temp_dir}")
        yield temp_dir
        # Cleanup happens automatically when the context manager exits


# Module-scoped fixture for a sample database
@pytest.fixture(scope="module")
def sample_db():
    """
    Create a sample in-memory database for tests.
    
    This fixture demonstrates how to create a resource that is shared
    across all tests in a module.
    """
    # Create an in-memory database (using a dictionary as a simple example)
    db = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "products": [
            {"id": 1, "name": "Product A", "price": 10.0},
            {"id": 2, "name": "Product B", "price": 20.0}
        ]
    }
    
    yield db
    
    # Cleanup (if needed)
    print("\nCleaning up sample database")


# Fixture for a sample configuration file
@pytest.fixture
def config_file(temp_dir):
    """
    Create a sample configuration file for tests.
    
    This fixture demonstrates how to create a file resource for tests
    and how to use another fixture (temp_dir).
    """
    # Create a configuration file in the temporary directory
    config_path = os.path.join(temp_dir, "config.json")
    config_data = {
        "app_name": "Test App",
        "debug": True,
        "max_connections": 100,
        "timeout": 30
    }
    
    with open(config_path, "w") as f:
        json.dump(config_data, f, indent=2)
    
    yield config_path
    
    # Cleanup
    if os.path.exists(config_path):
        os.remove(config_path)
        print(f"\nRemoved config file: {config_path}")


# Fixture factory for creating test users
@pytest.fixture
def create_test_user():
    """
    A fixture factory for creating test users.
    
    This fixture demonstrates how to create a fixture that returns a function,
    which can be used to create customized test data.
    """
    def _create_user(user_id=None, name=None, email=None, role="user"):
        """
        Create a test user with the specified attributes.
        
        Args:
            user_id: The ID of the user (default: auto-generated)
            name: The name of the user (default: "Test User")
            email: The email of the user (default: generated from name)
            role: The role of the user (default: "user")
            
        Returns:
            A dictionary representing the user
        """
        user_id = user_id or 1000
        name = name or f"Test User {user_id}"
        email = email or f"{name.lower().replace(' ', '.')}@example.com"
        
        return {
            "id": user_id,
            "name": name,
            "email": email,
            "role": role
        }
    
    return _create_user


# Autouse fixture for all tests
@pytest.fixture(autouse=True, scope="session")
def global_setup_teardown():
    """
    A session-scoped autouse fixture for global setup and teardown.
    
    This fixture demonstrates how to perform setup and teardown operations
    that apply to all tests in the test suite.
    """
    # Setup
    print("\n=== Starting test session ===")
    
    yield
    
    # Teardown
    print("\n=== Test session finished ===")


# Fixture for mocking an API client
@pytest.fixture
def mock_api_client():
    """
    Create a mock API client for tests.
    
    This fixture demonstrates how to create a mock object that can be
    configured by individual tests.
    """
    class MockAPIClient:
        def __init__(self):
            self.responses = {}
            self.calls = []
        
        def set_response(self, method, endpoint, response):
            """Set a response for a specific method and endpoint."""
            key = (method, endpoint)
            self.responses[key] = response
        
        def request(self, method, endpoint, data=None):
            """Make a request to the mock API."""
            key = (method, endpoint)
            self.calls.append({"method": method, "endpoint": endpoint, "data": data})
            
            if key not in self.responses:
                raise ValueError(f"No mock response set for {method} {endpoint}")
            
            return self.responses[key]
        
        def get(self, endpoint):
            """Make a GET request."""
            return self.request("GET", endpoint)
        
        def post(self, endpoint, data):
            """Make a POST request."""
            return self.request("POST", endpoint, data)
        
        def put(self, endpoint, data):
            """Make a PUT request."""
            return self.request("PUT", endpoint, data)
        
        def delete(self, endpoint):
            """Make a DELETE request."""
            return self.request("DELETE", endpoint)
    
    return MockAPIClient()


# Fixture for a test environment
@pytest.fixture
def test_env():
    """
    Set up a test environment with configuration variables.
    
    This fixture demonstrates how to set up environment variables for tests.
    """
    # Save original environment variables
    original_env = {}
    test_vars = {
        "TEST_MODE": "True",
        "TEST_DB_URL": "sqlite:///:memory:",
        "TEST_API_KEY": "test-api-key-123"
    }
    
    # Set test environment variables
    for key, value in test_vars.items():
        if key in os.environ:
            original_env[key] = os.environ[key]
        os.environ[key] = value
    
    yield test_vars
    
    # Restore original environment variables
    for key in test_vars:
        if key in original_env:
            os.environ[key] = original_env[key]
        else:
            del os.environ[key]


# Fixture for timing tests
@pytest.fixture
def timer():
    """
    A fixture that provides timing functionality for tests.
    
    This fixture demonstrates how to create a utility fixture that provides
    functionality rather than test data.
    """
    import time
    
    class Timer:
        def __init__(self):
            self.start_time = None
            self.end_time = None
        
        def start(self):
            """Start the timer."""
            self.start_time = time.time()
            return self
        
        def stop(self):
            """Stop the timer."""
            self.end_time = time.time()
            return self
        
        @property
        def elapsed(self):
            """Get the elapsed time in seconds."""
            if self.start_time is None:
                raise ValueError("Timer not started")
            
            end_time = self.end_time if self.end_time is not None else time.time()
            return end_time - self.start_time
    
    return Timer()


# Custom markers
def pytest_configure(config):
    """
    Configure pytest with custom markers.
    
    This function demonstrates how to define custom markers that can be used
    to categorize and select tests.
    """
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "api: mark test as an API test")
    config.addinivalue_line("markers", "database: mark test as a database test")


# Custom command-line options
def pytest_addoption(parser):
    """
    Add custom command-line options to pytest.
    
    This function demonstrates how to add custom command-line options to pytest.
    """
    parser.addoption(
        "--run-slow", action="store_true", default=False, help="Run slow tests"
    )
    parser.addoption(
        "--api-url", action="store", default="https://api.example.com", help="API URL for tests"
    )


# Skip slow tests unless --run-slow is specified
def pytest_collection_modifyitems(config, items):
    """
    Modify test collection based on command-line options.
    
    This function demonstrates how to skip tests based on command-line options.
    """
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="Need --run-slow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)


# Fixture for API URL from command line
@pytest.fixture
def api_url(request):
    """
    Get the API URL from the command line.
    
    This fixture demonstrates how to use command-line options in fixtures.
    """
    return request.config.getoption("--api-url")
