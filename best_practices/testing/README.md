# Testing in Python

This directory demonstrates best practices for testing in Python using pytest.

## Contents

- `test_basic.py`: Basic pytest examples
- `test_fixtures.py`: Examples of pytest fixtures
- `test_parametrize.py`: Examples of parameterized tests
- `test_mocking.py`: Examples of mocking with pytest
- `conftest.py`: Shared fixtures for all tests

## Running the Tests

To run all tests:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=.
```

To run a specific test file:

```bash
pytest test_basic.py
```

## Testing Best Practices

1. **Write tests first (TDD)** - Consider writing tests before implementing functionality
2. **Keep tests simple** - Each test should verify one specific behavior
3. **Use descriptive test names** - Names should describe what the test is verifying
4. **Use fixtures for setup/teardown** - Avoid duplicating setup code
5. **Test edge cases** - Don't just test the happy path
6. **Use mocks appropriately** - Mock external dependencies, but don't over-mock
7. **Run tests often** - Integrate testing into your development workflow
