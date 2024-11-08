
# Advanced Python Calculator

This project is an advanced command-line calculator. It emphasizes professional software development practices, including the use of design patterns, logging, plugins, environment variables, and data management with Pandas.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [Architectural Decisions](#architectural-decisions)
  - [Design Patterns](#design-patterns)
  - [Logging Strategy](#logging-strategy)
  - [Environment Variables](#environment-variables)
  - [Pandas for Data Management](#pandas-for-data-management)
- [Plugins](#plugins)
- [Testing and Coverage](#testing-and-coverage)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ign2-r/is218-midterm.git
   cd is218-midterm
   ```

2. **Install dependencies**
   The project requires Python 3.7+ and packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory with environment variables for logging, history storage, and logging level configuration.

   ```plaintext
   ENVIRONMENT=development
   LOG_LEVEL=DEBUG
   HISTORY_FILE=history.csv
   LOG_FILE=calculator.log
   ```

4. **Run Tests**
   Run all tests using pytest:
   ```bash
   pytest --cov=app --cov-report=html
   ```
   This generates a coverage report viewable in the `htmlcov` directory.

## Usage Examples

1. **Basic Commands in REPL:**
   ```plaintext
   Simple Calculator. Type 'exit' to quit, 'history' to view history, 'save_history' to save, 'load_history' to load, 'clear_history' to clear.
   Enter operation (e.g., 5 3 add): 5 3 add
   Result: 8
   ```
   
2. **Plugins Example:**
   To use plugins like `sqrt`:
   ```plaintext
   Enter operation (e.g., sqrt 16): sqrt 16
   Result: 4.0
   ```
   
3. **History Commands:**
   ```plaintext
   Type 'history' to view saved calculations or 'clear_history' to delete all history.
   ```

## Architectural Decisions

This project is structured for modularity, extensibility, and maintainability. Below are the primary architectural decisions made:

### Design Patterns

The project uses several design patterns:
- **Facade Pattern** to simplify the interface for accessing history management and calculations.
- **Command Pattern** for encapsulating calculator operations, making it easier to add new operations.
- **Plugin System** allowing new operations to be dynamically loaded without modifying core code.

### Logging Strategy

The application uses a comprehensive logging strategy:
- **Log Levels**: Environment variable `LOG_LEVEL` controls the logging verbosity (e.g., DEBUG, INFO).
- **Error Handling**: Different log levels differentiate warnings, errors, and information messages.

### Environment Variables

Environment variables are used to manage configurable settings without hardcoding them:
- **LOG_LEVEL**: Controls logging verbosity.
- **HISTORY_FILE**: Specifies the file for saving calculation history.

### Pandas for Data Management

Pandas is utilized for flexible management of calculation history:
- **CSV Storage**: Allows saving and loading history for persistence.
- **Data Operations**: Pandas simplifies operations on stored history.

## Plugins

The plugin system enables dynamically loaded operations. Each plugin is structured to integrate easily with the main calculator without requiring changes to core code.

## Testing and Coverage

The project includes extensive unit tests for each module. Run tests using:
```bash
pytest --cov=app --cov-report=html
```
Coverage reports are generated in `htmlcov/`.
