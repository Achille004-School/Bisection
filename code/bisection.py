import sys
from math import *


class Bisector:
    def __init__(self, f: str):
        # Initialize the Bisector object with the given mathematical function as a string.
        self.FUNCTION = f

    # Calculates the value of the function for a given x.
    def calc(self, x: float):
        try:
            return eval(self.FUNCTION)
        except ZeroDivisionError as e:
            # Handle division by zero error by exiting the program.
            print(f'Math error: {e}')
            sys.exit()

    # Calculates the middle point between two given points a and b.
    def middlePoint(self, a: float, b: float):
        return (a + b) / 2

    # Finds a root of the function within the interval [a, b] using the bisection method.
    def find(self, a: float, b: float):
        # Check if the initial points are roots
        if self.calc(a) == 0:
            print(f'Zero of the function: {a}')
            return
        if self.calc(b) == 0:
            print(f'Zero of the function: {b}')
            return

        # Check if the signs of the function values at points a and b are different, indicating a potential root.
        if self.calc(a) * self.calc(b) > 0:
            # Print an error message if the signs of the function values at points a and b are not different.
            print("Invalid values for proceeding with the algorithm.")
            return

        i = 0
        prev_interval = None

        while True:
            i += 1

            # Calculate the middle point of the interval and its value in f.
            mid = self.middlePoint(a, b)
            mid_val = self.calc(mid)

            if mid_val == 0:
                # If the f-value of the middle point between a and b is 0 then it is the root of the function.
                print(f'Zero of the function: {mid}')
                break
            elif (self.calc(a) * mid_val) > 0:
                # If the sign of f(a) is the same as f(mid), so the root is not in the range [a, mid_val],
                # update the interval by setting a to the midpoint, restricting the interval to [mid_val, b].
                a = mid
            elif (self.calc(b) * mid_val) > 0:
                # If the sign of f(b) is the same as f(mid), so the root is not in the range [mid_val, b],
                # update the interval by setting b to the midpoint, restricting the interval to [a, mid_val].
                b = mid
            else:
                # Exit the loop if both f(a) and f(b) has the same sign as f(mid).
                print("Cannot continue.")
                break

            current_interval = (a, b)

            if prev_interval == current_interval:
                # Print the interval containing the root if there is no change in the interval.
                print(f"Zero of the function between: {a} and {b}")
                break
            else:
                # Print the current attempt and the interval.
                print(f"Attempt {i}: a={a} b={b}")
                prev_interval = current_interval
