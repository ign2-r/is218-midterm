"""
History manager: manages history of calculations and undo operations.
"""
import os
from typing import Union
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEFAULT_HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

class HistoryManager:
    """Class to manage history of calculations with Pandas."""

    def __init__(self, history_file: str = DEFAULT_HISTORY_FILE):
        """Initialize the history manager with an empty DataFrame and specified history file."""
        self.history_file = history_file
        self.history = pd.DataFrame(columns=["entry"])

    def add_to_history(self, entry: str):
        """Add a calculation entry to the history."""
        new_record = {"entry": entry}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    def get_history(self) -> list:
        """Return the history of calculations as a list of entries."""
        return self.history["entry"].tolist()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation entry in the history."""
        if not self.history.empty:
            last_entry = self.history.iloc[-1]["entry"]
            self.history = self.history.iloc[:-1]
            return last_entry
        return None

    def save_history(self):
        """Save the history DataFrame to a CSV file."""
        self.history.to_csv(self.history_file, index=False)

    def load_history(self):
        """Load the history DataFrame from a CSV file."""
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
        else:
            self.history = pd.DataFrame(columns=["entry"]) # pragma: no cover

    def clear_history(self):
        """Clear the history DataFrame and delete the CSV file."""
        self.history = pd.DataFrame(columns=["entry"])
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
