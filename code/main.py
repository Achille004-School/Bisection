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

import sys
from math import pi
from math import e
from bisection import Bisector

print('''
Bisection  Copyright (C) 2022  Francesco Marras and Luca Porzio
This program comes with ABSOLUTELY NO WARRANTY; for details see https://www.gnu.org/licenses/gpl-3.0.html.
This is free software, and you are welcome to redistribute it under certain conditions; see https://www.gnu.org/licenses/gpl-3.0.html for details.
''')
f = input('Function > ')
f = f.replace('^', '**')

if 'x' in f:
    a = float(input('a: '))
    b = float(input('b: '))
    bisett = Bisector(f)
    bisett.find(a, b)
else:
    try:
        print('Simple calculation: ' + str(eval(f)))
    except(ZeroDivisionError) as e:
        print('Math error: ' + str(e))

a = input('Press enter to continue...')
