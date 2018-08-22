__author__ = 'stefan'
import math

digits = str(math.factorial(100))
print sum([int(i) for i in digits])