13
13
6
3
3
9

# hw6TEST.py

>>> from hw6 import *
>>> import random

##### game #####


above lines are user inputs to be used for code
that requires user input

code below directs input to be received from above
should not cause an error

>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('hw6TEST.py')

>>> random.seed(5)
>>> game(1)
9 + 4 = ?
Enter answer: Correct
You got 1 correct answers out of 1.
>>> game(2)
5 + 8 = ?
Enter answer: Correct
0 + 7 = ?
Enter answer: Incorrect
You got 1 correct answers out of 2.
>>> game(3)
3 + 0 = ?
Enter answer: Correct
2 + 1 = ?
Enter answer: Correct
5 + 7 = ?
Enter answer: Incorrect
You got 2 correct answers out of 3.

put stdin back to original, again, shouldnt cause error
>>> sys.stdin = si  # return stdin



##### craps #####
>>> random.seed(1)
>>> craps()
2 5
1
>>> random.seed(2)
>>> craps()
1 1
0
>>> random.seed(9)
>>> craps()
4 5
3 3
2 2
6 1
0
>>> random.seed(7)
>>> craps()
3 2
4 6
1 1
5 1
3 5
1 5
2 1
1 4
1
>>> 

##### quietCraps #####

>>> random.seed(1)
>>> quietCraps()
1
>>> random.seed(2)
>>> quietCraps()
0
>>> random.seed(9)
>>> quietCraps()
0
>>> random.seed(7)
>>> quietCraps()
1
>>> [ (i,random.seed(i),quietCraps()) for i in range(10,20)]
[(10, None, 1), (11, None, 1), (12, None, 1), (13, None, 1), (14, None, 0), (15, None, 0), (16, None, 1), (17, None, 0), (18, None, 0), (19, None, 1)]
>>> 

##### testCraps #####


>>> random.seed(5)
>>> testCraps(10)
0.3
>>> random.seed(5)
>>> testCraps(100)
0.44
>>> random.seed(5)
>>> testCraps(1000)
0.497

>>> import inspect
>>> 'if' in inspect.getsource(testCraps)  # testCraps should call quietCraps, not repeat its logic
False
>>> 'rand' in inspect.getsource(testCraps) # testCraps should call quietCraps, not repeat its logic
False
>>> [ (i,random.seed(10),testCraps(10**i)) for i in range(4)]
[(0, None, 1.0), (1, None, 0.5), (2, None, 0.58), (3, None, 0.52)]
