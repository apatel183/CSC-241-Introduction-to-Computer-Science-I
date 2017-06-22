frank
FRAnk
Sue
SUE
Frank
sue

# lab7TEST.py

>>> from lab7 import *


##### reverse #####

>>> pb = {'eric':'123-4567','sue':'999-9999','sally':'3333'}
>>> pb['sue']
'999-9999'
>>> reverse( pb )=={'999-9999': 'sue', '3333': 'sally', '123-4567': 'eric'}
True
>>> reverse( pb )['3333']
'sally'
>>> reverse( { i:2*i for i in range(10) } ) == {0: 0, 16: 8, 2: 1, 4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 18: 9, 14: 7}
True

##### letter2number #####


>>> letter2number('A-')
3.7
>>> letter2number('c+')
2.3
>>> letter2number('f')
0
>>> letter2number('e')
'unknown grade'
>>> [ letter2number( a+b) for a in 'bcd' for b in '+-']
[3.3, 2.7, 2.3, 1.7, 1.3, 0.7]


##### names #####

above lines are user inputs to be used for code
that requires user input

code below directs input to be received from above
should not cause an error

>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('lab7TEST.py')

>>> names()
Enter next name: Enter next name: Enter next name: Enter next name: Enter next name: Enter next name: Enter next name: There are 3 students named FRANK
There are 3 students named SUE


put stdin back to original, again, shouldnt cause error
>>> sys.stdin = si  # return stdin
