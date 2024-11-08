"""
History manager: manages history of calculations and undo operations.
"""
import os
import pandas as pd
from typing import Union
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

class HistoryManager:
    """Class to manage history of calculations with Pandas."""

    def __init__(self):
        """Initialize the history manager with an empty DataFrame."""
        # Define an empty DataFrame for storing history
        self.history = pd.DataFrame(columns=["entry"])

    def add_to_history(self, entry: str):
        """Add a calculation entry to the history."""
        # Append the new entry to the DataFrame
        new_record = {"entry": entry}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    def get_history(self) -> list:
        """Return the history of calculations as a list of entries."""
        # Convert the DataFrame to a list of strings for compatibility
        return self.history["entry"].tolist()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation entry in the history."""
        if not self.history.empty:
            last_entry = self.history.iloc[-1]["entry"]
            self.history = self.history.iloc[:-1]  # Remove the last entry
            return last_entry
        return None

    def save_history(self):
        """Save the history DataFrame to a CSV file."""
        self.history.to_csv(HISTORY_FILE, index=False)

    def load_history(self):
        """Load the history DataFrame from a CSV file."""
        if os.path.exists(HISTORY_FILE):
            self.history = pd.read_csv(HISTORY_FILE)
        else:
            self.history = pd.DataFrame(columns=["entry"])

    def clear_history(self):
        """Clear the history DataFrame and delete the CSV file."""
        self.history = pd.DataFrame(columns=["entry"])
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
