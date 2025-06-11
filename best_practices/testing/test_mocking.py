#!/usr/bin/env python3
"""
Pytest Mocking Examples

This module demonstrates how to use mocking in pytest to isolate the code being tested
from its dependencies, which is essential for unit testing.

Topics covered:
- Basic mocking with unittest.mock
- Mocking with pytest-mock
- Patching functions and methods
- Mocking return values and side effects
- Mocking classes and objects
- Verifying mock calls
- Mocking context managers
"""
import pytest
import requests
import os
import json
from unittest import mock
from typing import List, Dict, Any, Optional


# A simple function that makes an HTTP request
def get_user_data(user_id):
    """
    Get user data from an API.
    
    Args:
        user_id: The ID of the user to fetch
        
    Returns:
        The user data as a dictionary
    
    Raises:
        requests.RequestException: If the request fails
    """
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


# A function that uses the above function
def get_user_name(user_id):
    """
    Get the name of a user.
    
    Args:
        user_id: The ID of the user to fetch
        
    Returns:
        The user's name
    """
    user_data = get_user_data(user_id)
    return user_data.get("name", "Unknown")


# A class that uses external services
class UserService:
    """A service for managing users."""
    
    def __init__(self, api_client):
        self.api_client = api_client
    
    def get_user(self, user_id):
        """Get a user by ID."""
        return self.api_client.get_user(user_id)
    
    def create_user(self, user_data):
        """Create a new user."""
        return self.api_client.create_user(user_data)
    
    def update_user(self, user_id, user_data):
        """Update an existing user."""
        return self.api_client.update_user(user_id, user_data)
    
    def delete_user(self, user_id):
        """Delete a user."""
        return self.api_client.delete_user(user_id)


# A class that uses file I/O
class ConfigManager:
    """A class for managing configuration files."""
    
    def __init__(self, config_path):
        self.config_path = config_path
    
    def load_config(self):
        """Load configuration from a file."""
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def save_config(self, config):
        """Save configuration to a file."""
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get_setting(self, key, default=None):
        """Get a setting from the configuration."""
        config = self.load_config()
        return config.get(key, default)
    
    def set_setting(self, key, value):
        """Set a setting in the configuration."""
        config = self.load_config()
        config[key] = value
        self.save_config(config)
        return True


# Basic mocking with unittest.mock
def test_get_user_name_with_unittest_mock():
    """
    Test get_user_name using unittest.mock.
    
    This demonstrates how to use unittest.mock.patch to replace a function
    with a mock object.
    """
    # Create a mock for the get_user_data function
    with mock.patch('test_mocking.get_user_data') as mock_get_user_data:
        # Configure the mock to return a specific value
        mock_get_user_data.return_value = {"name": "John Doe", "email": "john@example.com"}
        
        # Call the function under test
        result = get_user_name(123)
        
        # Verify the result
        assert result == "John Doe"
        
        # Verify that the mock was called with the expected arguments
        mock_get_user_data.assert_called_once_with(123)


# Mocking with pytest-mock
def test_get_user_name_with_pytest_mock(mocker):
    """
    Test get_user_name using pytest-mock.
    
    This demonstrates how to use the mocker fixture provided by pytest-mock.
    """
    # Create a mock for the get_user_data function
    mock_get_user_data = mocker.patch('test_mocking.get_user_data')
    
    # Configure the mock to return a specific value
    mock_get_user_data.return_value = {"name": "Jane Doe", "email": "jane@example.com"}
    
    # Call the function under test
    result = get_user_name(456)
    
    # Verify the result
    assert result == "Jane Doe"
    
    # Verify that the mock was called with the expected arguments
    mock_get_user_data.assert_called_once_with(456)


# Mocking a method in a class
def test_user_service_get_user(mocker):
    """
    Test UserService.get_user using mocks.
    
    This demonstrates how to mock a method in a class.
    """
    # Create a mock API client
    mock_api_client = mock.Mock()
    
    # Configure the mock to return a specific value
    mock_api_client.get_user.return_value = {"id": 789, "name": "Bob Smith"}
    
    # Create an instance of UserService with the mock API client
    user_service = UserService(mock_api_client)
    
    # Call the method under test
    result = user_service.get_user(789)
    
    # Verify the result
    assert result == {"id": 789, "name": "Bob Smith"}
    
    # Verify that the mock was called with the expected arguments
    mock_api_client.get_user.assert_called_once_with(789)


# Mocking with side effects
def test_user_service_create_user_with_side_effect(mocker):
    """
    Test UserService.create_user with a side effect.
    
    This demonstrates how to configure a mock to have a side effect
    (e.g., raising an exception or calling a function).
    """
    # Create a mock API client
    mock_api_client = mock.Mock()
    
    # Configure the mock to raise an exception
    mock_api_client.create_user.side_effect = ValueError("Invalid user data")
    
    # Create an instance of UserService with the mock API client
    user_service = UserService(mock_api_client)
    
    # Call the method under test and expect an exception
    with pytest.raises(ValueError) as excinfo:
        user_service.create_user({"name": "Invalid User"})
    
    # Verify the exception message
    assert "Invalid user data" in str(excinfo.value)
    
    # Verify that the mock was called with the expected arguments
    mock_api_client.create_user.assert_called_once_with({"name": "Invalid User"})


# Mocking with a function as a side effect
def test_user_service_update_user_with_function_side_effect(mocker):
    """
    Test UserService.update_user with a function as a side effect.
    
    This demonstrates how to configure a mock to call a function as a side effect.
    """
    # Create a function to use as a side effect
    def side_effect_func(user_id, user_data):
        return {"id": user_id, **user_data, "updated_at": "2023-01-01"}
    
    # Create a mock API client
    mock_api_client = mock.Mock()
    
    # Configure the mock to use the function as a side effect
    mock_api_client.update_user.side_effect = side_effect_func
    
    # Create an instance of UserService with the mock API client
    user_service = UserService(mock_api_client)
    
    # Call the method under test
    result = user_service.update_user(101, {"name": "Updated User"})
    
    # Verify the result
    assert result == {"id": 101, "name": "Updated User", "updated_at": "2023-01-01"}
    
    # Verify that the mock was called with the expected arguments
    mock_api_client.update_user.assert_called_once_with(101, {"name": "Updated User"})


# Mocking multiple return values
def test_user_service_with_multiple_return_values(mocker):
    """
    Test UserService with multiple return values.
    
    This demonstrates how to configure a mock to return different values
    on successive calls.
    """
    # Create a mock API client
    mock_api_client = mock.Mock()
    
    # Configure the mock to return different values on successive calls
    mock_api_client.get_user.side_effect = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"},
        {"id": 3, "name": "User 3"}
    ]
    
    # Create an instance of UserService with the mock API client
    user_service = UserService(mock_api_client)
    
    # Call the method under test multiple times
    result1 = user_service.get_user(1)
    result2 = user_service.get_user(2)
    result3 = user_service.get_user(3)
    
    # Verify the results
    assert result1 == {"id": 1, "name": "User 1"}
    assert result2 == {"id": 2, "name": "User 2"}
    assert result3 == {"id": 3, "name": "User 3"}
    
    # Verify that the mock was called with the expected arguments
    assert mock_api_client.get_user.call_count == 3
    mock_api_client.get_user.assert_has_calls([
        mock.call(1),
        mock.call(2),
        mock.call(3)
    ])


# Mocking context managers
def test_config_manager_load_config(mocker):
    """
    Test ConfigManager.load_config by mocking the file I/O.
    
    This demonstrates how to mock a context manager (open).
    """
    # Create a mock file object
    mock_file = mock.Mock()
    mock_file.__enter__ = mock.Mock(return_value=mock_file)
    mock_file.__exit__ = mock.Mock(return_value=None)
    mock_file.read.return_value = '{"setting1": "value1", "setting2": "value2"}'
    
    # Create a mock for the open function
    mock_open = mocker.patch('builtins.open', return_value=mock_file)
    
    # Create an instance of ConfigManager
    config_manager = ConfigManager('/path/to/config.json')
    
    # Call the method under test
    result = config_manager.load_config()
    
    # Verify the result
    assert result == {"setting1": "value1", "setting2": "value2"}
    
    # Verify that open was called with the expected arguments
    mock_open.assert_called_once_with('/path/to/config.json', 'r')


# Alternative way to mock open using mock_open
def test_config_manager_save_config(mocker):
    """
    Test ConfigManager.save_config by mocking the file I/O.
    
    This demonstrates how to use mock_open to mock file I/O.
    """
    # Create a mock for the open function using mock_open
    mock_file = mock.mock_open()
    mocker.patch('builtins.open', mock_file)
    
    # Create an instance of ConfigManager
    config_manager = ConfigManager('/path/to/config.json')
    
    # Call the method under test
    config_manager.save_config({"setting1": "new_value1", "setting2": "new_value2"})
    
    # Verify that open was called with the expected arguments
    mock_file.assert_called_once_with('/path/to/config.json', 'w')
    
    # Verify that write was called with the expected JSON string
    # Note: The exact format of the JSON string may vary, so we check for the presence of key elements
    handle = mock_file()
    handle.write.assert_called_once()
    written_data = handle.write.call_args[0][0]
    assert '"setting1": "new_value1"' in written_data
    assert '"setting2": "new_value2"' in written_data


# Mocking a class
def test_mocking_entire_class(mocker):
    """
    Test by mocking an entire class.
    
    This demonstrates how to mock an entire class.
    """
    # Create a mock class
    mock_requests = mocker.patch('test_mocking.requests')
    
    # Configure the mock response
    mock_response = mock.Mock()
    mock_response.json.return_value = {"id": 42, "name": "Mocked User"}
    mock_response.raise_for_status = mock.Mock()
    
    # Configure the mock get method
    mock_requests.get.return_value = mock_response
    
    # Call the function under test
    result = get_user_data(42)
    
    # Verify the result
    assert result == {"id": 42, "name": "Mocked User"}
    
    # Verify that the mock was called with the expected arguments
    mock_requests.get.assert_called_once_with("https://api.example.com/users/42")
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()


# Mocking with spy
def test_with_spy(mocker):
    """
    Test using a spy.
    
    This demonstrates how to use a spy to observe calls to a real object
    without replacing its functionality.
    """
    # Create a simple class to spy on
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def multiply(self, a, b):
            return a * b
    
    # Create an instance of the class
    calculator = Calculator()
    
    # Create a spy for the add method
    spy = mocker.spy(calculator, 'add')
    
    # Call the method
    result = calculator.add(2, 3)
    
    # Verify the result (the real method was called)
    assert result == 5
    
    # Verify that the method was called with the expected arguments
    spy.assert_called_once_with(2, 3)


# Mocking with autospec
def test_with_autospec(mocker):
    """
    Test using autospec.
    
    This demonstrates how to use autospec to create a mock that has the same
    attributes and methods as the original object.
    """
    # Create a class with methods
    class APIClient:
        def get_user(self, user_id):
            # In a real implementation, this would make an API call
            pass
        
        def create_user(self, user_data):
            # In a real implementation, this would make an API call
            pass
    
    # Create a mock with autospec
    mock_api_client = mock.create_autospec(APIClient)
    
    # Configure the mock
    mock_api_client.get_user.return_value = {"id": 123, "name": "Autospec User"}
    
    # Create an instance of UserService with the mock
    user_service = UserService(mock_api_client)
    
    # Call the method under test
    result = user_service.get_user(123)
    
    # Verify the result
    assert result == {"id": 123, "name": "Autospec User"}
    
    # Verify that the mock was called with the expected arguments
    mock_api_client.get_user.assert_called_once_with(123)
    
    # Trying to call a method that doesn't exist on the original object will raise an AttributeError
    with pytest.raises(AttributeError):
        mock_api_client.nonexistent_method()


if __name__ == "__main__":
    # This allows running the tests with python test_mocking.py
    # However, it's better to use pytest command line
    pytest.main(["-v", __file__])
