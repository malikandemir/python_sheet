#!/usr/bin/env python3
"""
Object-Oriented Programming in Python

This module demonstrates advanced OOP concepts in Python that a senior developer
should be familiar with, including:
- Classes and objects
- Inheritance and composition
- Encapsulation
- Polymorphism
- Abstract classes and interfaces
- Class and static methods
- Properties and descriptors
- Metaclasses
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Type, TypeVar, Generic


class BasicClassDemo:
    """
    Demonstrates basic class concepts in Python.
    """
    
    def __init__(self, name: str, value: int = 0):
        """
        Constructor method.
        
        Args:
            name: The name of the instance
            value: An integer value (default: 0)
        """
        self.name = name        # Public attribute
        self._value = value     # Protected attribute (by convention)
        self.__secret = "This is a private attribute"  # Name mangling
    
    def __str__(self) -> str:
        """String representation of the object."""
        return f"{self.name} with value {self._value}"
    
    def __repr__(self) -> str:
        """Representation of the object for debugging."""
        return f"BasicClassDemo(name='{self.name}', value={self._value})"
    
    def increment(self, amount: int = 1) -> None:
        """Increment the value by the given amount."""
        self._value += amount
    
    def get_value(self) -> int:
        """Get the current value."""
        return self._value
    
    def _protected_method(self) -> str:
        """
        Protected method (by convention).
        Not meant to be called outside the class or its subclasses.
        """
        return "This is a protected method"
    
    def __private_method(self) -> str:
        """
        Private method (name mangling).
        Not meant to be called outside the class.
        """
        return "This is a private method"
    
    def access_private(self) -> str:
        """Access the private method from within the class."""
        return self.__private_method()
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BasicClassDemo':
        """
        Class method to create an instance from a dictionary.
        
        Args:
            data: Dictionary containing name and value
            
        Returns:
            A new instance of the class
        """
        return cls(data.get('name', 'Default'), data.get('value', 0))
    
    @staticmethod
    def is_positive(value: int) -> bool:
        """
        Static method to check if a value is positive.
        
        Args:
            value: The value to check
            
        Returns:
            True if value is positive, False otherwise
        """
        return value > 0


class InheritanceDemo(BasicClassDemo):
    """
    Demonstrates inheritance in Python.
    """
    
    def __init__(self, name: str, value: int = 0, category: str = "Default"):
        """
        Constructor method.
        
        Args:
            name: The name of the instance
            value: An integer value (default: 0)
            category: The category of the instance (default: "Default")
        """
        # Call the parent class constructor
        super().__init__(name, value)
        self.category = category
    
    def __str__(self) -> str:
        """Override the string representation."""
        return f"{self.name} ({self.category}) with value {self._value}"
    
    # Override a method from the parent class
    def increment(self, amount: int = 1) -> None:
        """
        Override the increment method to double the amount.
        
        Args:
            amount: The amount to increment by (default: 1)
        """
        # Call the parent class method
        super().increment(amount * 2)
        print(f"Value incremented by {amount * 2}")
    
    # Add a new method
    def get_details(self) -> Dict[str, Any]:
        """
        Get details of the instance.
        
        Returns:
            A dictionary with instance details
        """
        return {
            'name': self.name,
            'value': self._value,
            'category': self.category
        }
    
    # Access protected method from parent
    def access_protected(self) -> str:
        """Access the protected method from the parent class."""
        return self._protected_method()


class MultipleInheritanceDemo(BasicClassDemo, dict):
    """
    Demonstrates multiple inheritance in Python.
    
    This class inherits from both BasicClassDemo and dict.
    """
    
    def __init__(self, name: str, value: int = 0, **kwargs):
        """
        Constructor method.
        
        Args:
            name: The name of the instance
            value: An integer value (default: 0)
            **kwargs: Additional key-value pairs for the dict
        """
        # Initialize both parent classes
        BasicClassDemo.__init__(self, name, value)
        dict.__init__(self, **kwargs)
    
    def __str__(self) -> str:
        """String representation combining both parent classes."""
        return f"{self.name} with value {self._value} and dict {dict.__str__(self)}"
    
    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """
        Update both the BasicClassDemo attributes and dict items.
        
        Args:
            data: Dictionary with data to update
        """
        if 'name' in data:
            self.name = data['name']
        if 'value' in data:
            self._value = data['value']
        
        # Update dict items
        for key, value in data.items():
            if key not in ('name', 'value'):
                self[key] = value


# Method Resolution Order (MRO) demonstration
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass


def demonstrate_basic_classes():
    """Demonstrates basic class usage."""
    print("\n=== BASIC CLASSES ===")
    
    # Create an instance
    obj = BasicClassDemo("Example", 10)
    print(f"Object: {obj}")
    print(f"Repr: {repr(obj)}")
    
    # Access attributes and methods
    print(f"Name: {obj.name}")
    print(f"Value: {obj.get_value()}")
    
    # Modify the object
    obj.increment(5)
    print(f"After increment: {obj.get_value()}")
    
    # Create from class method
    data = {'name': 'FromDict', 'value': 20}
    obj2 = BasicClassDemo.from_dict(data)
    print(f"Created from dict: {obj2}")
    
    # Use static method
    print(f"Is 10 positive? {BasicClassDemo.is_positive(10)}")
    print(f"Is -5 positive? {BasicClassDemo.is_positive(-5)}")
    
    # Try to access private attribute (will use name mangling)
    try:
        print(obj.__secret)
    except AttributeError as e:
        print(f"Error accessing private attribute: {e}")
    
    # Access private method through public method
    print(f"Access private method: {obj.access_private()}")
    
    # Access the mangled name directly
    print(f"Access mangled name: {obj._BasicClassDemo__secret}")


def demonstrate_inheritance():
    """Demonstrates inheritance concepts."""
    print("\n=== INHERITANCE ===")
    
    # Create an instance of the child class
    child = InheritanceDemo("Child", 5, "Test")
    print(f"Child object: {child}")
    
    # Use inherited method
    print(f"Initial value: {child.get_value()}")
    
    # Use overridden method
    child.increment(3)
    print(f"Value after increment: {child.get_value()}")
    
    # Use new method
    details = child.get_details()
    print(f"Details: {details}")
    
    # Access protected method
    print(f"Access protected: {child.access_protected()}")
    
    # Check instance relationships
    print(f"child is InheritanceDemo? {isinstance(child, InheritanceDemo)}")
    print(f"child is BasicClassDemo? {isinstance(child, BasicClassDemo)}")
    print(f"InheritanceDemo is subclass of BasicClassDemo? {issubclass(InheritanceDemo, BasicClassDemo)}")


def demonstrate_multiple_inheritance():
    """Demonstrates multiple inheritance concepts."""
    print("\n=== MULTIPLE INHERITANCE ===")
    
    # Create an instance with dict items
    multi = MultipleInheritanceDemo("Multi", 15, a=1, b=2, c=3)
    print(f"Multi object: {multi}")
    
    # Access as BasicClassDemo
    print(f"Name: {multi.name}")
    print(f"Value: {multi.get_value()}")
    
    # Access as dict
    print(f"Dict keys: {multi.keys()}")
    print(f"Dict values: {multi.values()}")
    print(f"Item 'a': {multi['a']}")
    
    # Update from dict
    multi.update_from_dict({'name': 'Updated', 'value': 25, 'd': 4})
    print(f"After update: {multi}")
    
    # Demonstrate Method Resolution Order (MRO)
    d = D()
    print(f"\nMethod Resolution Order (MRO) for class D: {D.__mro__}")
    print(f"D().method() returns: {d.method()}")  # Should return "B" due to MRO


if __name__ == "__main__":
    print("OBJECT-ORIENTED PROGRAMMING IN PYTHON (PART 1)")
    print("=============================================")
    
    demonstrate_basic_classes()
    demonstrate_inheritance()
    demonstrate_multiple_inheritance()
