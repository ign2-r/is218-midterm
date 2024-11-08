"""
Conftest module to configure pytest and handle project imports.

This script adds the project root directory to sys.path so that relative imports
in the test files can be resolved correctly.
"""

import sys
import os

# Add the project root directory to sys.path to handle relative imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
