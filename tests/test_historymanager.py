"""
Unit tests for the HistoryManager class in the app.historymanager module.

This module contains tests for adding to history, retrieving history, saving and loading history,
clearing history, and undoing the last entry in the history.
"""

import os
from app.historymanager import HistoryManager

def test_history_manager_initialization_without_file():
    """
    Test that HistoryManager initializes with an empty DataFrame when no history file is present.
    This specifically covers the line setting self.history to an empty DataFrame.
    """
    history_file = "test_history.csv"
    # Ensure the file does not exist before running the test
    if os.path.exists(history_file):
        os.remove(history_file)

    # Instantiate HistoryManager without interacting with load/save to cover initialization
    history_manager = HistoryManager(history_file=history_file)
    # Verify the history is an empty list (empty DataFrame)
    assert history_manager.history.empty  # Directly check the DataFrame
    assert history_manager.get_history() == []  # Check converted list

    # Clean up
    if os.path.exists(history_file):
        os.remove(history_file)

def test_add_to_history():
    """
    Test that adding an entry to history correctly stores it.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    history_manager.add_to_history("1 + 1 = 2")
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_get_history_empty():
    """
    Test that getting history returns an empty list when no entries exist.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    assert not history_manager.get_history()

def test_undo_last():
    """
    Test that undo removes the last entry from the history.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    history_manager.add_to_history("5 - 3 = 2")
    history_manager.add_to_history("10 / 2 = 5")
    undo = history_manager.undo_last()
    assert undo == "10 / 2 = 5"
    assert history_manager.get_history() == ["5 - 3 = 2"]

def test_undo_last_empty():
    """
    Test that undo returns None when history is empty.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    assert history_manager.undo_last() is None

def test_save_history():
    """
    Test saving history to a CSV file.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    history_manager.add_to_history("3 * 3 = 9")
    history_manager.save_history()
    assert os.path.exists("test_history.csv")

def test_load_history():
    """
    Test loading history from a CSV file.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    history_manager.add_to_history("3 + 3 = 6")
    history_manager.save_history()

    # Create a new instance to test loading
    history_manager_new = HistoryManager(history_file="test_history.csv")
    history_manager_new.load_history()
    assert history_manager_new.get_history() == ["3 + 3 = 6"]

def test_clear_history():
    """
    Test clearing history by resetting the DataFrame and deleting the CSV file.
    """
    history_manager = HistoryManager(history_file="test_history.csv")
    history_manager.add_to_history("4 / 2 = 2")
    history_manager.save_history()
    history_manager.clear_history()

    # Verify that the history is now empty
    assert history_manager.get_history() == []
    assert not os.path.exists("test_history.csv")
