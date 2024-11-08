"""
Operations module: basic calculator functions.
"""
from typing import Union

def addition(a: float, b: float) -> float:
    """Perform addition."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Perform subtraction."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Perform multiplication."""
    return a * b

def division(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def modulo(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return "Cannot modulo by zero."
    return a % b

def power(a: float, b: float) -> float:
    return a ** b
