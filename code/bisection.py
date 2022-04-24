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
