#!/usr/bin/env python3
"""
Asynchronous Programming in Python

This module demonstrates asynchronous programming concepts in Python using asyncio,
which is essential knowledge for a senior Python developer.

Topics covered:
- Coroutines and async/await syntax
- Tasks and Futures
- Asynchronous context managers
- Asynchronous iterators
- Asynchronous generators
- Synchronization primitives
- Running async code from synchronous code
"""
import asyncio
import time
import random
from typing import List, Dict, Any, AsyncIterator, Optional, TypeVar, Generic
from contextlib import asynccontextmanager


async def simple_coroutine():
    """
    A simple coroutine that demonstrates the basic async/await syntax.
    """
    print("Starting simple coroutine")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("Simple coroutine completed")
    return "Coroutine result"


async def demonstrate_basic_coroutines():
    """
    Demonstrates basic coroutine concepts.
    """
    print("\n=== BASIC COROUTINES ===")
    
    # Awaiting a coroutine
    result = await simple_coroutine()
    print(f"Result: {result}")
    
    # Creating and awaiting multiple coroutines sequentially
    print("\nRunning coroutines sequentially:")
    start = time.time()
    
    await asyncio.sleep(0.5)
    print("First sleep completed")
    
    await asyncio.sleep(0.5)
    print("Second sleep completed")
    
    end = time.time()
    print(f"Sequential execution took {end - start:.2f} seconds")
    
    # Running coroutines concurrently
    print("\nRunning coroutines concurrently:")
    start = time.time()
    
    # gather runs multiple coroutines concurrently and waits for all of them
    await asyncio.gather(
        asyncio.sleep(0.5),
        asyncio.sleep(0.5)
    )
    print("Both sleeps completed")
    
    end = time.time()
    print(f"Concurrent execution took {end - start:.2f} seconds")


async def fetch_data(id: int, delay: float) -> Dict[str, Any]:
    """
    Simulates fetching data from a remote source.
    
    Args:
        id: The ID of the data to fetch
        delay: The delay in seconds to simulate network latency
        
    Returns:
        A dictionary with the fetched data
    """
    print(f"Fetching data for ID {id}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Data for ID {id} fetched")
    return {"id": id, "data": f"Data for ID {id}", "timestamp": time.time()}


async def demonstrate_tasks():
    """
    Demonstrates working with Tasks in asyncio.
    """
    print("\n=== TASKS ===")
    
    # Create a task
    task = asyncio.create_task(fetch_data(1, 1.0))
    print("Task created")
    
    # Do other work while the task is running
    print("Doing other work...")
    await asyncio.sleep(0.5)
    print("Other work completed")
    
    # Wait for the task to complete
    result = await task
    print(f"Task result: {result}")
    
    # Creating multiple tasks
    print("\nCreating multiple tasks:")
    tasks = [
        asyncio.create_task(fetch_data(i, random.uniform(0.5, 1.5)))
        for i in range(1, 4)
    ]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    print(f"All tasks completed. Results: {results}")
    
    # Task cancellation
    print("\nTask cancellation:")
    task = asyncio.create_task(fetch_data(10, 2.0))
    
    # Wait a bit and then cancel the task
    await asyncio.sleep(0.5)
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")


async def demonstrate_futures():
    """
    Demonstrates working with Futures in asyncio.
    """
    print("\n=== FUTURES ===")
    
    # Create a Future
    future = asyncio.Future()
    print("Future created")
    
    # Schedule a task to set the future's result
    async def set_future_result():
        await asyncio.sleep(1)
        future.set_result("Future result")
        print("Future result set")
    
    # Start the task
    asyncio.create_task(set_future_result())
    
    # Wait for the future to complete
    print("Waiting for future...")
    result = await future
    print(f"Future completed with result: {result}")
    
    # Using Future with asyncio.wait_for
    future = asyncio.Future()
    
    try:
        # Wait for the future with a timeout
        await asyncio.wait_for(future, timeout=0.5)
    except asyncio.TimeoutError:
        print("Future timed out")


class AsyncResource:
    """
    A class that demonstrates an asynchronous context manager.
    """
    
    async def __aenter__(self):
        """
        Asynchronous enter method.
        """
        print("Acquiring resource asynchronously...")
        await asyncio.sleep(0.5)  # Simulate async acquisition
        print("Resource acquired")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Asynchronous exit method.
        """
        print("Releasing resource asynchronously...")
        await asyncio.sleep(0.5)  # Simulate async release
        print("Resource released")
        return False  # Don't suppress exceptions


@asynccontextmanager
async def async_resource_decorator():
    """
    An asynchronous context manager implemented as a decorator.
    """
    print("Acquiring resource asynchronously (decorator)...")
    await asyncio.sleep(0.5)  # Simulate async acquisition
    print("Resource acquired (decorator)")
    try:
        yield "Resource"
    finally:
        print("Releasing resource asynchronously (decorator)...")
        await asyncio.sleep(0.5)  # Simulate async release
        print("Resource released (decorator)")


async def demonstrate_async_context_managers():
    """
    Demonstrates asynchronous context managers.
    """
    print("\n=== ASYNC CONTEXT MANAGERS ===")
    
    # Using a class-based async context manager
    async with AsyncResource() as resource:
        print("Using the resource...")
        await asyncio.sleep(0.5)
    
    # Using a decorator-based async context manager
    async with async_resource_decorator() as resource:
        print(f"Using the resource: {resource}")
        await asyncio.sleep(0.5)


class AsyncCounter:
    """
    A class that demonstrates an asynchronous iterator.
    """
    
    def __init__(self, stop: int):
        self.current = 0
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(0.2)  # Simulate async work
            self.current += 1
            return self.current - 1
        else:
            raise StopAsyncIteration


async def async_generator(n: int) -> AsyncIterator[int]:
    """
    An asynchronous generator function.
    
    Args:
        n: The number of values to generate
        
    Yields:
        Integers from 0 to n-1
    """
    for i in range(n):
        await asyncio.sleep(0.2)  # Simulate async work
        yield i


async def demonstrate_async_iterators_generators():
    """
    Demonstrates asynchronous iterators and generators.
    """
    print("\n=== ASYNC ITERATORS AND GENERATORS ===")
    
    # Using an asynchronous iterator
    print("Using async iterator:")
    counter = AsyncCounter(3)
    async for value in counter:
        print(f"Iterator value: {value}")
    
    # Using an asynchronous generator
    print("\nUsing async generator:")
    async for value in async_generator(3):
        print(f"Generator value: {value}")
    
    # Using asynchronous comprehensions
    print("\nUsing async comprehension:")
    result = [value async for value in async_generator(3)]
    print(f"Comprehension result: {result}")
    
    # Using asyncio.gather with async generators
    print("\nGathering values from multiple async generators:")
    generators = [async_generator(2) for _ in range(3)]
    
    async def collect_from_generator(gen):
        return [value async for value in gen]
    
    results = await asyncio.gather(*(collect_from_generator(gen) for gen in generators))
    print(f"Gathered results: {results}")


async def demonstrate_synchronization_primitives():
    """
    Demonstrates asyncio synchronization primitives.
    """
    print("\n=== SYNCHRONIZATION PRIMITIVES ===")
    
    # Lock
    lock = asyncio.Lock()
    
    async def critical_section(task_id: int):
        print(f"Task {task_id} waiting for lock")
        async with lock:
            print(f"Task {task_id} acquired lock")
            await asyncio.sleep(0.5)  # Simulate work in critical section
            print(f"Task {task_id} releasing lock")
    
    print("Using Lock:")
    await asyncio.gather(critical_section(1), critical_section(2), critical_section(3))
    
    # Event
    event = asyncio.Event()
    
    async def waiter(task_id: int):
        print(f"Waiter {task_id} waiting for event")
        await event.wait()
        print(f"Waiter {task_id} received event")
    
    async def setter():
        print("Setter will set event in 1 second")
        await asyncio.sleep(1)
        print("Setter setting event")
        event.set()
    
    print("\nUsing Event:")
    await asyncio.gather(waiter(1), waiter(2), setter())
    
    # Semaphore
    semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent tasks
    
    async def worker(task_id: int):
        print(f"Worker {task_id} waiting for semaphore")
        async with semaphore:
            print(f"Worker {task_id} acquired semaphore")
            await asyncio.sleep(1)  # Simulate work
            print(f"Worker {task_id} releasing semaphore")
    
    print("\nUsing Semaphore:")
    await asyncio.gather(worker(1), worker(2), worker(3), worker(4))


def run_async_from_sync():
    """
    Demonstrates how to run asynchronous code from synchronous code.
    """
    print("\n=== RUNNING ASYNC CODE FROM SYNC CODE ===")
    
    # Using asyncio.run (preferred way in Python 3.7+)
    print("Using asyncio.run:")
    asyncio.run(simple_coroutine())
    
    # Using an event loop directly
    print("\nUsing event loop directly:")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(simple_coroutine())
    finally:
        loop.close()


async def main():
    """
    Main coroutine that demonstrates all asyncio concepts.
    """
    print("ASYNCHRONOUS PROGRAMMING IN PYTHON")
    print("=================================")
    
    await demonstrate_basic_coroutines()
    await demonstrate_tasks()
    await demonstrate_futures()
    await demonstrate_async_context_managers()
    await demonstrate_async_iterators_generators()
    await demonstrate_synchronization_primitives()


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
    
    # Demonstrate running async code from sync code
    run_async_from_sync()
