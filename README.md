# Advanced Python Calculator

This project is an advanced Python calculator application, created for a software engineering course. The calculator integrates core software engineering concepts, including design patterns, exception handling, a plugin system, logging, and more. Video below for live demonstration.

[![Demonstration](https://img.youtube.com/vi/rJ3v046Aqis/0.jpg)](https://www.youtube.com/watch?v=rJ3v046Aqis)

## Table of Contents
- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Features](#features)
  - [Design Patterns](#design-patterns)
  - [Exception Handling (LBYL and EAFP)](#exception-handling-lbyl-and-eafp)
  - [Logging](#logging)
  - [Plugin System](#plugin-system)
- [Usage](#usage)

## Project Overview
This calculator provides basic arithmetic operations, history management, and a dynamically-loaded plugin system. It's structured to highlight clean code practices and software engineering principles.

## Setup and Installation
```bash
# Clone the repository
git clone https://github.com/ign2-r/is218-midterm.git
cd is218-midterm

# Set up virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the calculator
python3 -m app.main
```

## Features

### Design Patterns
1. **Factory Method**: Used to instantiate calculation operations, enhancing modularity.
   - [Factory Code](https://github.com/ign2-r/is218-midterm/blob/main/app/operations/__init__.py)
   
2. **Singleton Pattern**: Ensures only one instance of the `HistoryManager`.
   - [Singleton Code](https://github.com/ign2-r/is218-midterm/blob/main/app/historymanager/__init__.py)

3. **Command Pattern**: Implements operations (e.g., add, subtract) as commands in the calculator.
   - [Command Pattern Code](https://github.com/ign2-r/is218-midterm/blob/main/app/calculator/__init__.py)

4. **Facade Pattern**: Provides a simplified interface for accessing calculation and history.
   - [Facade Pattern Code](https://github.com/ign2-r/is218-midterm/blob/main/app/calculation/__init__.py)

### Exception Handling (LBYL and EAFP)
This project utilizes both **Look Before You Leap (LBYL)** and **Easier to Ask for Forgiveness than Permission (EAFP)** strategies for error handling:
- **LBYL**: Checks conditions before executing operations.
   - [Example Code](https://github.com/ign2-r/is218-midterm/blob/main/app/calculator/__init__.py#L34)
   
- **EAFP**: Catches and handles exceptions when they occur.
   - [Example Code](https://github.com/ign2-r/is218-midterm/blob/main/app/calculation/__init__.py#L40)

### Logging
Logging is implemented with varying levels (INFO, WARNING, ERROR) for debugging and monitoring:
- **INFO**: Records general operations.
- **WARNING**: Captures invalid operations.
- **ERROR**: Logs exceptions such as division by zero.

Logging Configuration:
- [Logging Setup Code](https://github.com/ign2-r/is218-midterm/blob/main/app/main.py#L20)

### Plugin System
The plugin system dynamically loads additional operations, allowing for modular functionality:
- **Example Plugin (Square Root)**: The `sqrt` function can be dynamically loaded and called.
  - [Plugin Code](https://github.com/ign2-r/is218-midterm/blob/main/plugins/sqrt.py)

## Usage
Run the application in a REPL interface, using operations like `add`, `subtract`, `multiply`, etc., and dynamically loaded plugins.
```bash
# Example usage
Enter operation (e.g., 2 3 add): 5
```
