"""
Calculation module: abstract base class for calculator operations.
"""
import logging
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division, modulo, power

# Set up a logger for this module
logger = logging.getLogger(__name__)

class Calculation(ABC):
    """Abstract base class for calculator operations."""
    
    @abstractmethod
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Abstract method to perform a calculation."""
        pass  # pragma: no cover

class BasicCalculation(Calculation):
    """Concrete class for basic calculations with logging."""
    
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Perform the operation based on the input, with logging for each operation."""
        try:
            if operation == 'add':
                result = addition(a, b)
            elif operation == 'subtract':
                result = subtraction(a, b)
            elif operation == 'multiply':
                result = multiplication(a, b)
            elif operation == 'divide':
                result = division(a, b)
            elif operation == 'modulo':
                result = modulo(a, b)
            elif operation == 'power':
                result = power(a, b)
            else:
                logger.warning("Invalid operation requested: %s", operation)
                return "Invalid operation."

            logger.info("Performed %s operation on %s and %s with result: %s", operation, a, b, result)
            return result

        except ZeroDivisionError:
            logger.error("Division or modulo by zero error with operation %s on %s and %s", operation, a, b)
            return "Cannot divide by zero."
        except Exception as e:
            logger.exception("An error occurred while performing the %s operation: %s", operation, e)
            return str(e)
