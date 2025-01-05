# Python: Handling ZeroDivisionError and Non-numeric Input in Average Calculation

This repository contains examples demonstrating a common coding error in Python involving division by zero and how to handle it gracefully.  The `bug.py` file shows code that can raise a `ZeroDivisionError` if the input list is empty or contains only zeros, and the `bugSolution.py` file provides a corrected version.

## Problem:

The original code (`bug.py`) calculates the average of a list of numbers. However, it does not handle the cases where the input list is empty or contains only zeros, leading to a `ZeroDivisionError`.

## Solution:

The improved code (`bugSolution.py`) addresses this issue by explicitly checking for these cases before performing the division.  It also handles potential `TypeError` exceptions if the input list contains non-numeric elements.

This example highlights the importance of comprehensive error handling in Python to prevent unexpected crashes and ensure robust code.