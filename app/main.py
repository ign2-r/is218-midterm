"""
Simple REPL interface for the calculator with logging.
"""
import os
import logging
from dotenv import load_dotenv
from app.calculator import Calculator

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration to log to a file instead of the console
log_file = os.getenv("LOG_FILE", "calculator.log")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    filename=log_file,
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def repl():
    """Simple REPL for user to interact with the calculator."""
    calc = Calculator()

    logging.info("Calculator REPL started.")
    print("Simple Calculator. Type 'exit' to quit. Type 'history' to view history. Type 'undo' to undo last.")
    
    while True:
        user_input = input("Enter operation (e.g., 1 1 add): ").strip()
        
        if user_input.lower() == 'exit':
            logging.info("User exited the REPL.")
            break
        elif user_input.lower() == 'history':
            history = calc.get_history()
            if history:
                logging.info("User requested history.")
                for entry in history:
                    print(entry)
            else:
                logging.info("User requested history, but no history is available.")
                print("No history available.")
        elif user_input.lower() == 'undo':
            undo = calc.undo_last()
            if undo:
                logging.info("User undid the last operation: %s", undo)
                print(f"Undone: {undo}")
            else:
                logging.info("User attempted to undo, but no operations were available.")
                print("No operations to undo.")
        else:
            try:
                # Parse the input and perform the calculation
                a, b, operation = user_input.split()
                a = float(a)
                b = float(b)
                result = calc.calculate_and_log(a, b, operation)
                
                # Log the successful calculation
                logging.info("User performed calculation: %s %s %s = %s", a, operation, b, result)
                print(f"Result: {result}")
            except ValueError as e:
                logging.error("ValueError occurred: %s", e)
                print(f"Error: {e}")
            except Exception as e:
                logging.exception("An unexpected error occurred with input: %s", user_input)
                print(f"Invalid input or operation: {e}")

if __name__ == "__main__":
    repl()
