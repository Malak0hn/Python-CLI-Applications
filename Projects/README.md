# Python CLI Applications

A collection of lightweight command-line applications developed in Python. This repository demonstrates core programming fundamentals, structured data management, error handling, and modular function design.

---

## Repository Structure

```text

├── 01-expense-tracker/
│   └── expense.py
├── 02-grade-analyzer/
│   └── grade.py
├── 03-guessing-game/
│   └── guess.py
├── 04-inventory-system/
│   └── inventory.py
└── 05-cli-calculators/
    ├── menu.py
    └── menu_list.py

```

---

## Projects Overview

| Project Directory | File | Description |
| --- | --- | --- |
| **01-expense-tracker** | `expense.py` | Tracks spending across categories, compares expenses against user-defined budget limits, and generates financial summaries. |
| **02-grade-analyzer** | `grade.py` | Accepts student scores, calculates class averages, identifies highest/lowest marks, and maps scores to letter grades. |
| **03-guessing-game** | `guess.py` | Interactive CLI game utilizing the `random` module with proximity hints and attempt counters. |
| **04-inventory-system** | `inventory.py` | Manages stock items, accumulates category expenditure, and generates itemized reports. |
| **05-cli-calculators** | `menu.py` / `menu_list.py` | Command-line calculators for two-operand math (`menu.py`) and dynamic list-based operations (`menu_list.py`). |

---

## Core Concepts Covered

* **Data Structures**: Utilization of dictionaries, nested lists, and set operations (`set()`).
* **Error & Exception Handling**: Input validation using `try-except` blocks to handle `ValueError` and `ZeroDivisionError`.
* **Modular Program Design**: Function separation (`main()`, helper methods) and execution guards (`if __name__ == "__main__":`).
* **Built-in Modules**: Use of standard modules like `random` and `math`.

---

## Usage Instructions

### Prerequisites

* Python 3.x installed on your system.

### Running a Project

1. Clone the repository:
```bash
git clone [https://github.com/YourUsername/repository-name.git](https://github.com/YourUsername/repository-name.git)

```


2. Navigate into the specific project directory:
```bash
cd 01-expense-tracker

```


3. Execute the script:
```bash
python expense.py
