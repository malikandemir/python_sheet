#!/usr/bin/env python3
"""
Advanced Object-Oriented Programming in Python

This module demonstrates more advanced OOP concepts in Python that a senior developer
should be familiar with, including:
- Abstract Base Classes
- Interfaces
- Properties and descriptors
- Metaclasses
- Dataclasses
- Protocol classes
- Context managers
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Type, Protocol
import dataclasses
import functools
import inspect


# Abstract Base Classes
class AbstractShape(ABC):
    """
    Abstract base class for shapes.
    
    This demonstrates how to create interfaces in Python using ABC.
    """
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self) -> str:
        """
        Non-abstract method that can use abstract methods.
        
        This demonstrates that abstract classes can have concrete methods
        that use the abstract methods.
        """
        return f"Shape with area {self.area()} and perimeter {self.perimeter()}"


class Circle(AbstractShape):
    """Implementation of AbstractShape for circles."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        """Calculate the area of the circle."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        import math
        return 2 * math.pi * self.radius


class Rectangle(AbstractShape):
    """Implementation of AbstractShape for rectangles."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


# Properties and descriptors
class PositiveNumber:
    """
    A descriptor that ensures a number is positive.
    
    This demonstrates how to create a descriptor in Python.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.private_name = f"_{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, 0)
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(instance, self.private_name, value)


class Product:
    """
    Class that uses properties and descriptors.
    
    This demonstrates how to use properties and descriptors to control
    attribute access and validation.
    """
    
    # Using a descriptor
    price = PositiveNumber("price")
    quantity = PositiveNumber("quantity")
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._discount = 0
    
    # Using a property
    @property
    def discount(self) -> float:
        """Get the current discount."""
        return self._discount
    
    @discount.setter
    def discount(self, value: float):
        """
        Set the discount with validation.
        
        Args:
            value: Discount percentage (0-100)
        
        Raises:
            ValueError: If discount is not between 0 and 100
        """
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = value
    
    @property
    def total_price(self) -> float:
        """
        Calculate the total price with discount.
        
        This demonstrates a read-only property that depends on other attributes.
        """
        discounted_price = self.price * (1 - self.discount / 100)
        return discounted_price * self.quantity


# Metaclasses
class SingletonMeta(type):
    """
    Metaclass for creating singleton classes.
    
    This demonstrates how to create and use metaclasses in Python.
    """
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    A singleton class.
    
    This demonstrates how to use a metaclass to create a singleton.
    """
    
    def __init__(self, value: str = ""):
        self.value = value


class RegistryMeta(type):
    """
    Metaclass that registers all classes that use it.
    
    This demonstrates another use case for metaclasses.
    """
    
    registry = {}
    
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != 'RegistryBase':  # Don't register the base class
            mcs.registry[name] = cls
        return cls


class RegistryBase(metaclass=RegistryMeta):
    """Base class for all classes that should be registered."""
    pass


class RegisteredClass1(RegistryBase):
    """A class that will be automatically registered."""
    pass


class RegisteredClass2(RegistryBase):
    """Another class that will be automatically registered."""
    pass


# Dataclasses
@dataclasses.dataclass
class Point:
    """
    A simple dataclass representing a 2D point.
    
    This demonstrates how to use dataclasses to create simple data containers.
    """
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        """Calculate the distance from the origin."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass(frozen=True)
class ImmutablePoint:
    """
    An immutable dataclass representing a 2D point.
    
    This demonstrates how to create immutable dataclasses.
    """
    x: float
    y: float


# Protocol classes (structural subtyping)
class Drawable(Protocol):
    """
    A protocol defining objects that can be drawn.
    
    This demonstrates how to use Protocol for structural subtyping.
    """
    
    def draw(self) -> None:
        """Draw the object."""
        ...


class Canvas:
    """
    A class that can work with any Drawable object.
    
    This demonstrates how to use Protocol for duck typing.
    """
    
    def __init__(self):
        self.drawables = []
    
    def add(self, drawable: Drawable) -> None:
        """
        Add a drawable object to the canvas.
        
        Args:
            drawable: Any object that implements the draw method
        """
        self.drawables.append(drawable)
    
    def draw_all(self) -> None:
        """Draw all objects on the canvas."""
        for drawable in self.drawables:
            drawable.draw()


class Circle2D:
    """A class that conforms to the Drawable protocol."""
    
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self) -> None:
        """Draw the circle."""
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")


class Rectangle2D:
    """Another class that conforms to the Drawable protocol."""
    
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self) -> None:
        """Draw the rectangle."""
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with dimensions {self.width}x{self.height}")


# Context managers
class FileManager:
    """
    A context manager for file operations.
    
    This demonstrates how to create a context manager using the __enter__
    and __exit__ methods.
    """
    
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """
        Enter the context.
        
        This method is called when entering a with statement.
        """
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context.
        
        This method is called when exiting a with statement.
        
        Args:
            exc_type: Exception type if an exception was raised, None otherwise
            exc_val: Exception value if an exception was raised, None otherwise
            exc_tb: Exception traceback if an exception was raised, None otherwise
            
        Returns:
            True if the exception was handled, False otherwise
        """
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False


def contextmanager_decorator(func):
    """
    A simplified version of the contextlib.contextmanager decorator.
    
    This demonstrates how to create a context manager using a generator function.
    
    Args:
        func: A generator function that yields once
        
    Returns:
        A context manager
    """
    @functools.wraps(func)
    class ContextManager:
        def __enter__(self):
            self.gen = func()
            return next(self.gen)
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                if exc_type is not None:
                    # Pass the exception to the generator
                    self.gen.throw(exc_type, exc_val, exc_tb)
                else:
                    next(self.gen, None)
            except StopIteration:
                return True
            return False
    
    return ContextManager()


@contextmanager_decorator
def temp_file(content: str):
    """
    A context manager that creates a temporary file.
    
    This demonstrates how to use a decorator to create a context manager.
    
    Args:
        content: Content to write to the file
    
    Yields:
        The name of the temporary file
    """
    import tempfile
    import os
    
    # Create a temporary file
    fd, name = tempfile.mkstemp(text=True)
    try:
        with open(name, 'w') as f:
            f.write(content)
        yield name
    finally:
        os.close(fd)
        os.unlink(name)


def demonstrate_abstract_classes():
    """Demonstrates abstract base classes."""
    print("\n=== ABSTRACT BASE CLASSES ===")
    
    # Cannot instantiate abstract class
    try:
        shape = AbstractShape()
        print("Created abstract shape")
    except TypeError as e:
        print(f"Error creating abstract shape: {e}")
    
    # Create concrete implementations
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")
    print(f"Circle description: {circle.describe()}")
    
    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    print(f"Rectangle description: {rectangle.describe()}")


def demonstrate_properties_descriptors():
    """Demonstrates properties and descriptors."""
    print("\n=== PROPERTIES AND DESCRIPTORS ===")
    
    # Create a product
    product = Product("Laptop", 1000, 2)
    print(f"Product: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print(f"Total price: ${product.total_price}")
    
    # Set discount
    product.discount = 10
    print(f"After 10% discount, total price: ${product.total_price}")
    
    # Try to set invalid values
    try:
        product.price = -100
    except ValueError as e:
        print(f"Error setting negative price: {e}")
    
    try:
        product.discount = 110
    except ValueError as e:
        print(f"Error setting invalid discount: {e}")


def demonstrate_metaclasses():
    """Demonstrates metaclasses."""
    print("\n=== METACLASSES ===")
    
    # Singleton metaclass
    s1 = Singleton("First")
    s2 = Singleton("Second")
    
    print(f"s1 value: {s1.value}")
    print(f"s2 value: {s2.value}")
    print(f"s1 is s2: {s1 is s2}")
    
    # Change value
    s1.value = "Changed"
    print(f"s1 value after change: {s1.value}")
    print(f"s2 value after change: {s2.value}")
    
    # Registry metaclass
    print(f"\nRegistry contents: {list(RegistryMeta.registry.keys())}")
    
    # Create instance from registry
    cls = RegistryMeta.registry['RegisteredClass1']
    instance = cls()
    print(f"Created instance of {instance.__class__.__name__}")


def demonstrate_dataclasses():
    """Demonstrates dataclasses."""
    print("\n=== DATACLASSES ===")
    
    # Create points
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"Distance from origin: {p1.distance_from_origin()}")
    
    # Immutable point
    ip = ImmutablePoint(1, 2)
    print(f"Immutable point: {ip}")
    
    try:
        ip.x = 5
    except dataclasses.FrozenInstanceError as e:
        print(f"Error modifying immutable point: {e}")


def demonstrate_protocols():
    """Demonstrates protocol classes."""
    print("\n=== PROTOCOL CLASSES ===")
    
    # Create drawable objects
    circle = Circle2D(10, 10, 5)
    rectangle = Rectangle2D(20, 20, 8, 6)
    
    # Create canvas
    canvas = Canvas()
    canvas.add(circle)
    canvas.add(rectangle)
    
    # Draw all objects
    canvas.draw_all()


def demonstrate_context_managers():
    """Demonstrates context managers."""
    print("\n=== CONTEXT MANAGERS ===")
    
    # Using the context manager class
    print("Using FileManager context manager:")
    try:
        with FileManager("nonexistent_file.txt") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    # Using the decorator-based context manager
    print("\nUsing decorator-based context manager:")
    with temp_file("Hello, world!") as filename:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of temporary file: {content}")
    
    # File should be deleted after the with block
    try:
        with open(filename, 'r'):
            pass
    except FileNotFoundError:
        print("Temporary file was properly deleted")


if __name__ == "__main__":
    print("ADVANCED OBJECT-ORIENTED PROGRAMMING IN PYTHON")
    print("============================================")
    
    demonstrate_abstract_classes()
    demonstrate_properties_descriptors()
    demonstrate_metaclasses()
    demonstrate_dataclasses()
    demonstrate_protocols()
    demonstrate_context_managers()
