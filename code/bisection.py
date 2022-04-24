# Bisection: Finds zero of the funcion using bisection algorythm.
# Copyright (C) 2022  Francesco Marras and Luca Porzio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.html.

from math import *
import sys

class Bisector():
    def __init__(self, f):
        self.f = f

    # calculates from x to f(x)
    def calc(self, x):
        try:
            return eval(self.f)
        except(ZeroDivisionError) as e:
            print('Math error: ' + str(e))
            sys.exit()

    # calculates middle point of a and b
    def middlePoint(self, a, b):
        return (a+b)/2

    def find(self, a, b):
        if self.calc(a) * self.calc(b) < 0:
            i = 0
            prev = ''

            while True:
                i += 1
                mid = self.middlePoint(a, b)
                midVal = self.calc(mid)

                if midVal == 0:
                    print('Zero of the function: ' + str(mid))
                    break
                elif (self.calc(a)*midVal) > 0:
                    a = mid
                elif (self.calc(b)*midVal) > 0:
                    b = mid
                else:
                    print('Cannot continue.')
                    break

                current = ': a=' + str(a) + ' b=' + str(b)

                if prev == current:
                    print('Zero of the function between: ' +
                          str(a) + ' and ' + str(b))
                    break
                else:
                    print('Attempt ' + str(i) + current)
                    prev = current
        else:
            print('Invalid values for proceeding with the algorythm.')
