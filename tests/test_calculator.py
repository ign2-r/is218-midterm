"""
Unit tests for the Calculator class in the app.calculator module.

This module contains tests for valid calculations, handling division by zero,
invalid operations, and undo functionality.
"""

import pytest
from app.calculator import Calculator

# Test valid calculations and history logging
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
])
def test_calculator_valid_operations(a, b, operation, expected):
    """
    Test valid operations and that history logs the correct calculation.
    """
    calc = Calculator()
    result = calc.calculate_and_log(a, b, operation)

    # Check result
    if operation == 'divide':
        assert result == float(expected)
    else:
        assert result == expected

    # Check history
    expected_str = f"{a} {operation} {b} = {result}"
    assert calc.get_history()[-1] == expected_str

# Test division by zero
@pytest.mark.parametrize("a, b, operation", [
    (10, 0, 'divide'),
    (5, 0, 'divide')
])
def test_calculator_division_by_zero(a, b, operation):
    """
    Test that division by zero returns the appropriate error message.
    """
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Cannot divide by zero."

# Test invalid operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculator_invalid_operation(a, b, operation):
    """
    Test that invalid operations return an error message.
    """
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Invalid operation."

# Test undo functionality
def test_calculator_undo():
    """
    Test that undo removes the last calculation from the history.
    """
    calc = Calculator()
    calc.calculate_and_log(1, 1, 'add')
    calc.calculate_and_log(5, 3, 'subtract')
    undo = calc.undo_last()

    assert undo == "5 subtract 3 = 2"
    assert len(calc.get_history()) == 1
