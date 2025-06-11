#!/usr/bin/env python3
"""
Advanced Data Structures in Python

This module demonstrates advanced usage of Python's built-in data structures
that a senior Python developer should be familiar with.
"""

def demonstrate_lists():
    """
    Demonstrates advanced list operations and list comprehensions.
    """
    print("\n=== LISTS ===")
    
    # Basic list comprehension
    squares = [x**2 for x in range(10)]
    print(f"List comprehension (squares): {squares}")
    
    # Filtered list comprehension
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Filtered list comprehension (even squares): {even_squares}")
    
    # Nested list comprehension (creating a matrix)
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Nested list comprehension (matrix): {matrix}")
    
    # List slicing with step
    numbers = list(range(10))
    print(f"Original list: {numbers}")
    print(f"Every second element: {numbers[::2]}")
    print(f"Reversed list: {numbers[::-1]}")
    
    # Advanced operations
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    # Concatenation
    print(f"Concatenation: {a + b}")
    
    # Repetition
    print(f"Repetition: {a * 3}")
    
    # List methods
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original list: {numbers}")
    
    numbers.sort()
    print(f"Sorted list: {numbers}")
    
    numbers.reverse()
    print(f"Reversed list: {numbers}")
    
    # Using key function with sort
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    words.sort(key=len)  # Sort by length
    print(f"Words sorted by length: {words}")


def demonstrate_dictionaries():
    """
    Demonstrates advanced dictionary operations and dictionary comprehensions.
    """
    print("\n=== DICTIONARIES ===")
    
    # Dictionary comprehension
    square_dict = {x: x**2 for x in range(1, 6)}
    print(f"Dictionary comprehension (squares): {square_dict}")
    
    # Conditional dictionary comprehension
    even_square_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Conditional dictionary comprehension: {even_square_dict}")
    
    # Dictionary methods
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    # get() with default value
    print(f"Using get() with default: {person.get('country', 'Unknown')}")
    
    # setdefault() - set a value if key doesn't exist
    person.setdefault("country", "USA")
    print(f"After setdefault(): {person}")
    
    # Dictionary update
    person.update({"age": 31, "profession": "Engineer"})
    print(f"After update(): {person}")
    
    # Dictionary views
    print(f"Keys view: {person.keys()}")
    print(f"Values view: {person.values()}")
    print(f"Items view: {person.items()}")
    
    # Dictionary unpacking (Python 3.5+)
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    combined = {**dict1, **dict2}
    print(f"Dictionary unpacking: {combined}")
    
    # Using defaultdict
    from collections import defaultdict
    
    # defaultdict with int as default factory
    word_counts = defaultdict(int)
    for word in "the quick brown fox jumps over the lazy dog".split():
        word_counts[word] += 1
    
    print(f"Word counts with defaultdict: {dict(word_counts)}")
    
    # defaultdict with list as default factory
    grouped_words = defaultdict(list)
    for word in "the quick brown fox jumps over the lazy dog".split():
        grouped_words[len(word)].append(word)
    
    print(f"Words grouped by length: {dict(grouped_words)}")


def demonstrate_sets():
    """
    Demonstrates advanced set operations.
    """
    print("\n=== SETS ===")
    
    # Set comprehension
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = "hello"
    vowels_in_word = {char for char in word if char in vowels}
    print(f"Vowels in '{word}': {vowels_in_word}")
    
    # Set operations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Union
    print(f"Union (A | B): {set_a | set_b}")
    
    # Intersection
    print(f"Intersection (A & B): {set_a & set_b}")
    
    # Difference
    print(f"Difference (A - B): {set_a - set_b}")
    
    # Symmetric difference
    print(f"Symmetric difference (A ^ B): {set_a ^ set_b}")
    
    # Subset and superset
    subset = {1, 2}
    print(f"Is {subset} a subset of {set_a}? {subset.issubset(set_a)}")
    print(f"Is {set_a} a superset of {subset}? {set_a.issuperset(subset)}")
    
    # Frozen sets (immutable sets)
    frozen = frozenset([1, 2, 3])
    print(f"Frozen set: {frozen}")
    
    # Using sets for deduplication
    duplicates = [1, 2, 2, 3, 4, 3, 5]
    unique = list(set(duplicates))
    print(f"Original list with duplicates: {duplicates}")
    print(f"List after deduplication: {unique}")


def demonstrate_tuples():
    """
    Demonstrates tuple operations and named tuples.
    """
    print("\n=== TUPLES ===")
    
    # Basic tuple operations
    point = (10, 20)
    x, y = point  # Tuple unpacking
    print(f"Point: {point}, x: {x}, y: {y}")
    
    # Tuples as dictionary keys (since they're immutable)
    locations = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles",
        (51.5074, -0.1278): "London"
    }
    print(f"Location at (40.7128, -74.0060): {locations[(40.7128, -74.0060)]}")
    
    # Named tuples
    from collections import namedtuple
    
    Person = namedtuple('Person', ['name', 'age', 'city'])
    alice = Person('Alice', 30, 'New York')
    
    print(f"Named tuple: {alice}")
    print(f"Accessing by name: {alice.name}, {alice.age}, {alice.city}")
    print(f"Accessing by index: {alice[0]}, {alice[1]}, {alice[2]}")
    
    # Converting to dictionary
    alice_dict = alice._asdict()
    print(f"Named tuple as dictionary: {alice_dict}")
    
    # Creating a new instance with _replace
    bob = alice._replace(name='Bob', age=25)
    print(f"New instance with _replace: {bob}")


def demonstrate_advanced_collections():
    """
    Demonstrates advanced collections from the collections module.
    """
    print("\n=== ADVANCED COLLECTIONS ===")
    
    from collections import Counter, deque, OrderedDict, ChainMap
    
    # Counter
    print("-- Counter --")
    word_counts = Counter("mississippi")
    print(f"Character counts: {word_counts}")
    print(f"Most common characters: {word_counts.most_common(2)}")
    
    # Deque (double-ended queue)
    print("\n-- Deque --")
    dq = deque([1, 2, 3])
    print(f"Original deque: {dq}")
    
    dq.append(4)        # Add to right
    dq.appendleft(0)    # Add to left
    print(f"After append operations: {dq}")
    
    dq.pop()            # Remove from right
    dq.popleft()        # Remove from left
    print(f"After pop operations: {dq}")
    
    dq.rotate(1)        # Rotate right by 1
    print(f"After rotating right: {dq}")
    
    dq.rotate(-1)       # Rotate left by 1
    print(f"After rotating left: {dq}")
    
    # OrderedDict (less important in Python 3.7+ as regular dicts maintain insertion order)
    print("\n-- OrderedDict --")
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(f"OrderedDict: {od}")
    
    # Move to end
    od.move_to_end('a')
    print(f"After moving 'a' to end: {od}")
    
    # ChainMap (search through multiple dictionaries)
    print("\n-- ChainMap --")
    defaults = {'theme': 'Default', 'language': 'English', 'showIndex': True}
    user_settings = {'language': 'Spanish'}
    
    # ChainMap searches through the dictionaries in order
    settings = ChainMap(user_settings, defaults)
    print(f"Combined settings: {dict(settings)}")
    print(f"Language setting: {settings['language']}")  # From user_settings
    print(f"Theme setting: {settings['theme']}")        # From defaults


def demonstrate_heapq():
    """
    Demonstrates the heapq module for priority queue operations.
    """
    print("\n=== HEAPQ (PRIORITY QUEUE) ===")
    
    import heapq
    
    # Creating a heap
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(numbers)  # Transform list into a heap in-place
    print(f"Heap: {numbers}")  # Note: this is still a list, but organized as a heap
    
    # Pushing items onto the heap
    heapq.heappush(numbers, 0)
    print(f"After push: {numbers}")
    
    # Popping the smallest item
    smallest = heapq.heappop(numbers)
    print(f"Popped smallest item: {smallest}")
    print(f"Heap after pop: {numbers}")
    
    # Push and pop in one operation
    next_smallest = heapq.heappushpop(numbers, 7)  # Push 7, then pop smallest
    print(f"Result of heappushpop: {next_smallest}")
    print(f"Heap after heappushpop: {numbers}")
    
    # Replace (pop smallest, then push new item)
    replaced = heapq.heapreplace(numbers, 0)  # Pop smallest, then push 0
    print(f"Result of heapreplace: {replaced}")
    print(f"Heap after heapreplace: {numbers}")
    
    # Getting the n largest/smallest items
    original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Original list: {original}")
    print(f"3 largest items: {heapq.nlargest(3, original)}")
    print(f"3 smallest items: {heapq.nsmallest(3, original)}")
    
    # Priority queue with tuples
    tasks = [(4, "Study Python"), (1, "Walk dog"), (3, "Write code"), (2, "Buy groceries")]
    heapq.heapify(tasks)  # Heapify based on first element of tuple
    
    print("\nTask priority queue:")
    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"Priority {priority}: {task}")


if __name__ == "__main__":
    print("ADVANCED DATA STRUCTURES IN PYTHON")
    print("=================================")
    
    demonstrate_lists()
    demonstrate_dictionaries()
    demonstrate_sets()
    demonstrate_tuples()
    demonstrate_advanced_collections()
    demonstrate_heapq()
