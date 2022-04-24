import sys
from math import pi
from math import e
from bisezione import Bisezione

print('Developed by Francesco Marras and Luca Porzio:')
f = input('Function > ')
f = f.replace('^', '**')

if 'x' in f:
    a = float(input('a: '))
    b = float(input('b: '))
    bisett = Bisezione(f)
    bisett.find(a, b)
else:
    try:
        print('Simple calculation: ' + str(eval(f)))
    except(ZeroDivisionError) as e:
        print('Math error: ' + str(e))

a = input('Press enter to continue...')
