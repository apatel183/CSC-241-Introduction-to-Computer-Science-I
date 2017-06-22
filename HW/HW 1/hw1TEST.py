13.25
6
13.25
-6
0.0
4
-23.55
3
-3.50
-4
0
0
-2.3
0.0
23.55
9
12
0
7

>>> from hw1 import *


>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('hw1TEST.py')

>>> total()
Enter a price: Enter a quantity: The total price is: $ 79.5
>>> total()
Enter a price: Enter a quantity: Error: both numbers must be greater than zero.
>>> total()
Enter a price: Enter a quantity: Error: both numbers must be greater than zero.
>>> total()
Enter a price: Enter a quantity: Error: both numbers must be greater than zero.
>>> total()
Enter a price: Enter a quantity: Error: both numbers must be greater than zero.
>>> total()
Enter a price: Enter a quantity: Error: both numbers must be greater than zero.
>>> 


>>> posNegZero()
Enter a number: You entered a negative number.
>>> posNegZero()
Enter a number: You entered zero.
>>> posNegZero()
Enter a number: You entered a positive number.
>>> 



>>> square()
Enter an integer: 9 is 3 squared.
>>> square()
Enter an integer: 12 is not a perfect square.
>>> square()
Enter an integer: 0 is 0 squared.
>>> square()
Enter an integer: 7 is not a perfect square.
>>> 


>>> sys.stdin = si  # return stdin
