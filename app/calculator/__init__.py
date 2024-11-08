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
        self.operations = {
            "add": self.calculation.calculate,
            "subtract": self.calculation.calculate,
            "multiply": self.calculation.calculate,
            "divide": self.calculation.calculate
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
        func = self.operations.get(operation)
        if func:
            # Use the function based on the operation, handling single and double operand cases
            result = func(a, b, operation) if operation in ["add", "subtract", "multiply", "divide"] else func(a)
            if isinstance(result, (int, float)):
                entry = f"{a} {operation} {b} = {result}"
                self.history_manager.add_to_history(entry)
            return result
        return "Invalid operation."

    def get_history(self) -> list:
        """Return the calculation history."""
        return self.history_manager.get_history()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation."""
        return self.history_manager.undo_last()
