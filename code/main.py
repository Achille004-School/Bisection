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
