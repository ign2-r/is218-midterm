"""
Simple REPL interface for the calculator with plugin support, history management, and logging.
"""
import os
import logging
from dotenv import load_dotenv
from app.calculator import Calculator
from app.historymanager import HistoryManager

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration to log to a file
log_file = os.getenv("LOG_FILE", "calculator.log")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    filename=log_file,
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def repl():
    """REPL for interacting with the calculator, plugins, and managing history."""
    calc = Calculator()
    history_manager = HistoryManager()

    # Load history at the start of the REPL session
    history_manager.load_history()
    logging.info("Calculator REPL started.")

    print("Simple Calculator with Plugin Support.")
    print("Type 'exit' to quit, 'history' to view history, 'menu' to view available commands.")
    print("Commands: 'save_history' to save, 'load_history' to load, 'clear_history' to clear.")

    while True:
        user_input = input("Enter operation (e.g., 1 1 add or 4 sqrt): ").strip()

        if user_input.lower() == 'exit':
            logging.info("User exited the REPL.")
            break
        elif user_input.lower() == 'menu':
            # Display available operations (including plugins)
            print("Available operations:", ', '.join(calc.operations.keys()))
        elif user_input.lower() == 'history':
            # Display and log history
            history = history_manager.get_history()
            if history:
                logging.info("User requested history.")
                for entry in history:
                    print(entry)
            else:
                logging.info("User requested history, but it was empty.")
                print("No history available.")
        elif user_input.lower() == 'save_history':
            history_manager.save_history()
            logging.info("User saved the calculation history.")
            print("History saved.")
        elif user_input.lower() == 'load_history':
            history_manager.load_history()
            logging.info("User loaded the calculation history.")
            print("History loaded.")
            for entry in history_manager.get_history():
                print(entry)
        elif user_input.lower() == 'clear_history':
            history_manager.clear_history()
            logging.info("User cleared the calculation history.")
            print("History cleared.")
        elif user_input.lower() == 'undo':
            undo = history_manager.undo_last()
            if undo:
                logging.info("User undid the last operation: %s", undo)
                print(f"Undone: {undo}")
            else:
                logging.info("User attempted to undo, but no operations were available.")
                print("No operations to undo.")
        else:
            try:
                # Parse the input and handle single- or double-operand operations
                parts = user_input.split()
                if len(parts) == 2:
                    a, operation = parts
                    a = float(a)
                    result = calc.calculate_and_log(a, None, operation)
                    entry = f"{operation}({a}) = {result}"
                elif len(parts) == 3:
                    a, b, operation = parts
                    a = float(a)
                    b = float(b)
                    result = calc.calculate_and_log(a, b, operation)
                    entry = f"{a} {operation} {b} = {result}"
                else:
                    raise ValueError("Invalid input format")

                # Log and add the calculation to history
                logging.info("User performed calculation: %s", entry)
                history_manager.add_to_history(entry)
                print(f"Result: {result}")

            except ValueError as e:
                logging.error("ValueError occurred: %s", e)
                print(f"Error: {e}")
            except Exception as e:
                logging.exception("An unexpected error occurred with input: %s", user_input)
                print(f"Invalid input or operation: {e}")

if __name__ == "__main__":
    repl()
