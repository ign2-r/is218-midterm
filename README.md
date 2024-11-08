
# Advanced Python Calculator

This repository contains an advanced Python-based calculator application developed for a software engineering course midterm project. 
The project demonstrates the integration of core software engineering principles including design patterns, error handling strategies, comprehensive logging, 
and a flexible plugin system for extending calculator functionalities.

## Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division, Modulo, and Power.
- **Dynamic Plugin System**: Supports additional operations through a plugin system, such as Square Root.
- **History Management**: Tracks calculation history, with options to save, load, clear, and undo operations.
- **Logging**: Comprehensive logging with configurable levels, severity differentiation, and support for both information and warnings.
- **Design Patterns**: Implements Factory Method, Command, and Strategy design patterns to support modular and extensible code.

## Usage Instructions
### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ign2-r/is218-midterm.git
   cd is218-midterm
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Calculator
Once the environment is set up and dependencies are installed, start the calculator by running:
```bash
python3 -m app.main
```

### Testing
To run tests with coverage and generate an HTML report:
```bash
pytest --cov=app --cov-report=html
```

## Key Architectural Components

### Design Patterns
- **Factory Method**: The plugin loader in the `Calculator` class uses the factory method to dynamically load plugins from the plugins directory. This pattern allows easy integration of new functionalities without altering core code.
- **Command Pattern**: Each calculation command (add, subtract, etc.) operates as a discrete, interchangeable unit, allowing flexibility in handling different operations.
- **Strategy Pattern**: Operations like addition, subtraction, etc., are encapsulated within the `BasicCalculation` class, enabling flexible strategies for each operation.

### Error Handling (LBYL and EAFP)
- **Look Before You Leap (LBYL)**: The calculator uses checks before performing actions such as division and modulo to prevent ZeroDivisionError, ensuring proactive error handling.
- **Easier to Ask for Forgiveness than Permission (EAFP)**: The code uses `try-except` blocks in cases where direct execution is simpler, such as when attempting to perform operations or loading plugins.

### Logging
- **Configurable Logging**: Set up through environment variables in `.env`, allowing control over the logging level (e.g., DEBUG, INFO, WARNING, ERROR).
- **Differentiated Severity**: Uses different log levels to differentiate between routine information (INFO), potential issues (WARNING), and errors (ERROR), allowing effective monitoring and debugging.
- **Warnings**: Logs invalid operations as warnings to help track incorrect user inputs or unsupported actions without interrupting program flow.

### Plugin System
The plugin system allows additional functionalities to be integrated without modifying core code. Each plugin (e.g., `sqrt`) is defined as a module with a specific operation. Plugins are dynamically loaded by the `Calculator` class, which searches the plugins directory and registers available operations.

**Example Plugin (`sqrt`)**:
```python
# Square root plugin
import math

def sqrt(a):
    return math.sqrt(a)

plugin = {
    "sqrt": sqrt
}
```
This plugin setup supports adding custom operations to the calculator without altering its core logic, exemplifying the open/closed principle.

## Project Structure
- `app/`: Core application code, including the `Calculator`, `HistoryManager`, and arithmetic operations.
- `plugins/`: Contains dynamically loaded plugins for additional calculator functionalities.
- `tests/`: Unit tests for verifying functionality and ensuring comprehensive test coverage.

## Author Information
This project was developed by Rockwell Dela Rosa as part of a midterm project for a software engineering course.
