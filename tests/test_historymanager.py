"""
Unit tests for the HistoryManager class in the app.historymanager module.

This module contains tests for adding to history, retrieving history, and 
undoing the last entry in the history.
"""

from app.historymanager import HistoryManager

def test_add_to_history():
    """
    Test that adding an entry to history correctly stores it.
    """
    history_manager = HistoryManager()
    history_manager.add_to_history("1 + 1 = 2")
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_get_history():
    """
    Test that getting history returns an empty list when no entries exist.
    """
    history_manager = HistoryManager()
    assert not history_manager.get_history()  # Simplified the check

def test_undo_last():
    """
    Test that undo removes the last entry from the history.
    """
    history_manager = HistoryManager()
    history_manager.add_to_history("5 - 3 = 2")
    history_manager.add_to_history("10 / 2 = 5")
    undo = history_manager.undo_last()
    assert undo == "10 / 2 = 5"
    assert history_manager.get_history() == ["5 - 3 = 2"]

def test_undo_last_empty():
    """
    Test that undo returns None when history is empty.
    """
    history_manager = HistoryManager()
    assert history_manager.undo_last() is None
