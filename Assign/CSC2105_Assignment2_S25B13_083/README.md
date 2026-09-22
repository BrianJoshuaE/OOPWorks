# CSC2105 OOP Assignment 2

**Student:** Elimu Brian Joshua  
**Registration number:** S25B13/083  
**Course:** CSC2105 Object Oriented Programming

## System

This submission implements a simplified Smart Campus Services System. Students have accounts with balances and daily spending limits. Successful deposits and service payments are recorded and can be read from a text file after the program is closed.

## Folder guide

- `Question1_UML/`: UML research, design explanation and Mermaid class diagram source.
- `Question2_Encapsulation/student_account.py`: classes, objects, class/instance attributes, public/protected/private attributes and name mangling.
- `Question3_Properties/controlled_account.py`: classic getter/setter, validation, properties and a read-only property.
- `Question4_Exceptions/reliable_account.py`: safe input handling, `try`, `except`, `else`, `finally`, `raise ValueError` and five test cases.
- `Question5_FileHandling/transactions.py`: persistent transaction records, missing-file handling and retrieval.
- `Question6_FinalSystem/main.py`: integrated final demonstration.

## How to run

From this folder, run:

```text
python Question2_Encapsulation/student_account.py
python Question3_Properties/controlled_account.py
python Question4_Exceptions/reliable_account.py
python Question5_FileHandling/transactions.py
python Question6_FinalSystem/main.py
```

The final program writes its demonstration records to `Question6_FinalSystem/transactions.txt`. The Question 5 program uses its own `transactions.txt` in the same folder.

## Submission checklist

The required UML exports should be placed in `Question1_UML/` as `UML_Research.pdf` and `Smart_Campus_UML.png`. The editable Mermaid source is already provided as `Smart_Campus_UML.mmd`; export it with Mermaid Live, draw.io, or another Mermaid-compatible tool before submission.

## Concepts demonstrated

Classes and objects, `__init__`, `self`, instance and class attributes, public/protected/private attributes, name mangling, getters and setters, `@property`, validation, read-only properties, exception handling, custom raised `ValueError`, file modes, writing, appending, reading, closing, and persistence.

## Sources used

1. Object Management Group, **OMG Unified Modeling Language (UML), Version 2.5.1**, https://www.omg.org/spec/UML/2.5.1
2. Python Software Foundation, **Classes**, https://docs.python.org/3/tutorial/classes.html
3. Python Software Foundation, **Built-in Functions: property**, https://docs.python.org/3/library/functions.html#property
4. Python Software Foundation, **Errors and Exceptions**, https://docs.python.org/3/tutorial/errors.html
5. Python Software Foundation, **Input and Output**, https://docs.python.org/3/tutorial/inputoutput.html

## Assumptions

- Money values are represented as non-negative numbers in Uganda shillings.
- A payment must be positive, must not exceed the account balance, and must not exceed the daily spending limit.
- A daily total is reset by calling `reset_daily_spending()`; no date service is required for this classroom demonstration.
- The transaction file is a simple human-readable pipe-separated text file.
