"""Tests for square root function"""
import pytest
from app.calculator import Calculator

@pytest.mark.parametrize("a, operation, expected", [
    (4, 'sqrt', 2),
    (16, 'sqrt', 4),
])
def test_calculator_sqrt_plugin(a, operation, expected):
    """Test dynamically loaded sqrt plugin operation."""
    calc = Calculator()
    result = calc.calculate_and_log(a, None, operation)
    assert result == expected
