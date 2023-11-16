from math import *
from bisection import Bisector

# Print program information and copyright notice
print(
    """
    Bisection  Copyright (C) 2022-2023  Francesco Marras & Luca Porzio
    This program comes with ABSOLUTELY NO WARRANTY; for details see https://www.gnu.org/licenses/gpl-3.0.html.
    This is free software, and you are welcome to redistribute it under certain conditions; see https://www.gnu.org/licenses/gpl-3.0.html for details.
    """
)

# Inform the user about the limitation of the algorithm
print(
    "This algorithm works only with continuous functions. There are no checks about continuity, so this job must be done by the user."
)

# Get the input function from the user
f = input("f(x) = ")

# Replace "^" with "**" for correct exponentiation
f = f.replace("^", "**")

# Check if the input function contains the variable "x"
if "x" in f:
    # If yes, get the interval [a, b] from the user
    a = float(input("a = "))
    b = float(input("b = "))

    # Create an instance of the Bisector class with the input function
    bisector = Bisector(f)

    # Use the bisection method to find the root in the given interval
    bisector.find(a, b)
else:
    # If the input function does not contain "x", try simple calculation
    try:
        # Evaluate the expression and print the result
        print(f'Simple calculation: {eval(f)}')
    except ZeroDivisionError as e:
        # Handle division by zero error
        print(f'Math error: {e}')

# Wait for the user to press enter before exiting the program
input("Press enter to continue...")