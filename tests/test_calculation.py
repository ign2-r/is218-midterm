"""
Test module for the BasicCalculation class.

This module contains tests to validate the basic operations like addition, subtraction,
multiplication, division, modulo, and power, as well as error handling for division by zero,
invalid operations, and unexpected exceptions.
"""

import pytest
from app.calculation import BasicCalculation

# Test valid calculations
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
    (10, 3, 'modulo', 1),
    (2, 3, 'power', 8)
])
def test_basic_calculation_valid(a, b, operation, expected):
    """
    Test operations (add, subtract, multiply, divide, modulo, power) return the expected results.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == expected

# Test division and modulo by zero with distinct messages
@pytest.mark.parametrize("a, b, operation, expected_message", [
    (10, 0, 'divide', "Cannot divide by zero."),
    (5, 0, 'modulo', "Cannot modulo by zero.")
])
def test_divide_or_modulo_by_zero(a, b, operation, expected_message):
    """
    Test that division and modulo by zero return distinct error messages.
    """
    calc = BasicCalculation()
    result = calc.calculate(a, b, operation)
    assert result == expected_message

# Test invalid operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculation_invalid_operation(a, b, operation):
    """
    Test that invalid operations return the appropriate error message.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Invalid operation."

# Test unsupported operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'log'),  # Unsupported operation
    (2, 2, 'sqrt')  # Unsupported operation
])
def test_calculation_unsupported_operation(a, b, operation):
    """
    Test that unsupported operations return an invalid operation error message.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Invalid operation."

# Test edge cases for valid operations
@pytest.mark.parametrize("a, b, operation, expected", [
    (-1, 1, 'add', 0),        # negative + positive
    (0, 0, 'add', 0),         # zero + zero
    (1.5, 2.5, 'add', 4),     # floats
    (-5, -5, 'multiply', 25), # negative * negative
    (2, -3, 'power', 0.125)   # positive base, negative exponent
])
def test_edge_cases(a, b, operation, expected):
    """
    Test edge cases like negative numbers, zeros, and floats.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == expected

# Test unexpected exceptions by passing invalid input
@pytest.mark.parametrize("a, b, operation", [
    (None, 3, 'add'),         # None as an operand
    (2, "string", 'multiply') # Non-numeric string as an operand
])
def test_calculation_unexpected_exception(a, b, operation):
    """
    Test that unexpected input results in an error message.
    """
    calc = BasicCalculation()
    result = calc.calculate(a, b, operation)
    # Check that result is a string message and not a numeric value
    assert isinstance(result, str) and not result.isdigit()
