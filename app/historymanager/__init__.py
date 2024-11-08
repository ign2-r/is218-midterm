"""
History manager: manages history of calculations and undo operations.
"""
from typing import Union

class HistoryManager:
    """Class to manage history of calculations."""
    def __init__(self):
        """Initialize the history manager with an empty history."""
        self.history = []

    def add_to_history(self, entry: str):
        """Add a calculation to the history."""
        self.history.append(entry)

    def get_history(self) -> list:
        """Return the history of calculations."""
        return self.history

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation."""
        if self.history:
            return self.history.pop()
        return None
