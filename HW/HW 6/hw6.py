###ARPAN PATEL###
###HW6.PY####

import random
#Question 1#

def game(n):
    total=0
    for i in range(n):
        dice1 = random.randrange(0,10)
        dice2 = random.randrange(0,10)
        print (dice1,'+', dice2,'=','?')
        correct = eval(input('Enter answer: '))
        if correct == dice1 + dice2:
            total+=1
            print ('Correct')
        else:
            print ('Incorrect')

    print('You got' " " + str(total) + " " 'correct answers out of ' + str(n)+ '.')

#Output
'''
>>> random.seed(5)
>>> game(1)
9 + 4 = ?
Enter answer: 13
Correct
You got 1 correct answers out of 1.
>>> game(2)
5 + 8 = ?
Enter answer: 13
Correct
0 + 7 = ?
Enter answer: 6
Incorrect
You got 1 correct answers out of 2.
>>> game(3)
3 + 0 = ?
Enter answer: 3
Correct
2 + 1 = ?
Enter answer: 3
Correct
5 + 7 = ?
Enter answer: 9
Incorrect
You got 2 correct answers out of 3.
>>>
'''

#Question 2#
    
def craps():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    print(dice1, dice2)
    if dice1 + dice2 in (7,11):
        return 1
    elif dice1 + dice2 in (2,3,12):
        return 0
    else:
        newroll = dice1 + dice2
    while True:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        print(dice1,dice2)
        if dice1 + dice2 == newroll:
            return 1
        if dice1 + dice2 == 7:
            return 0
#Output
'''
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
'''
#Question 3#
        
def quietCraps():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    #print(dice1, dice2)
    if dice1 + dice2 in (7,11):
        return 1
    elif dice1 + dice2 in (2,3,12):
        return 0
    else :
        newroll = dice1 + dice2
    while True:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        #print(dice1,dice2)
        if dice1 + dice2 == newroll:
            return 1
        if dice1 + dice2 == 7:
            return 0

#Output
'''
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
'''
#Question 4#
        
def testCraps(x):
    total=0
    for i in range(x):
        total+=quietCraps()
    return total/x
#Output
'''
>>> random.seed(5)
>>> testCraps(10)
0.3
>>> random.seed(5)
>>> testCraps(100)
0.44
>>> random.seed(5)
>>> testCraps(1000)
0.497
 '''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw6TEST.py') )
