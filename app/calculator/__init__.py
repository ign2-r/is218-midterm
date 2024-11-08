"""
Calculator Module

This module provides the `Calculator` class, which integrates basic arithmetic operations, 
history management, and a plugin system to allow dynamically loaded operations.

Classes:
    Calculator: Manages calculations and history, with support for dynamic plugins.

Functions and Functionalities:
    - Performs arithmetic operations such as addition, subtraction, multiplication, division, modulo, and power.
    - Supports history management, including saving, loading, clearing, and undoing the last calculation.
    - Loads plugins dynamically to extend supported operations.
    - Logs calculation activity and errors for monitoring and debugging.

Usage:
    The `Calculator` class can be used in an interactive REPL environment or integrated into other applications 
    where a calculation engine with history and plugin support is needed.
"""

import os
import importlib
from typing import Union
from app.calculation import BasicCalculation
from app.historymanager import HistoryManager

class Calculator:
    """Class that integrates calculation, history management, and dynamically loaded plugins."""
    def __init__(self):
        self.calculation = BasicCalculation()
        self.history_manager = HistoryManager()
        # Add modulo and power to operations
        self.operations = {
            "add": self.calculation.calculate,
            "subtract": self.calculation.calculate,
            "multiply": self.calculation.calculate,
            "divide": self.calculation.calculate,
            "modulo": self.calculation.calculate,
            "power": self.calculation.calculate
        }
        self.load_plugins()

    def load_plugins(self):
        """Dynamically load plugins from the plugins directory."""
        plugins_dir = "plugins"
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{plugins_dir}.{module_name}")
                if hasattr(module, "plugin"):
                    self.operations.update(module.plugin)

    def calculate_and_log(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Calculate the result, log the operation in history, and return the result or error."""
        # Call calculate, which will handle logging of invalid operations
        result = self.calculation.calculate(a, b, operation)
        if isinstance(result, (int, float)):
            entry = f"{a} {operation} {b} = {result}"
            self.history_manager.add_to_history(entry)
        return result

    def get_history(self) -> list:
        """Return the calculation history."""
        return self.history_manager.get_history()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation."""
        return self.history_manager.undo_last()
