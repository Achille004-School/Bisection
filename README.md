# Bisection
This program finds the zero of a user-given function in a user-defined interval [a; b] using the bisection algorithm.  

Note that, due to floating-point imprecision, the algorithm may return slightly incorrect values because it cannot yet determine whether it is intended as such or should be rounded.  
(e.g., 2.7755575615628914e-17 as the result of f(x)="e^x-1" with a=9 and b=-10, which should be 0.0 instead).

## Bisection Algorithm
For the mathematical explanation of the algorithm, see [Wikipedia page](https://en.wikipedia.org/wiki/Bisection_method).