# whileLoops.py

###### hw q's #####

# poly

# plug in x into each
# monomial and accumulate sum

# step 1 - indexed iteration, print value of
#          monomial (term) evaluated at x
# step 2 - accumulate those values

##### while #####
'''
while cond:
    statements
statements

while:
    iteration when you don't know up front
    what you are iterating over (or how much
    you need to do)

    executes indented statements (body) as
    long as the condition is True

    like an if, but continues to recheck until False

    body can execute 0...infinite number of times

    condition shoudl become False at some point

>>> while 2<3:
	print('hello')

	
hello
hello
hello
...
'''

'''
make this work:
>>> pigLatin('apple')
'appleay'
>>> pigLatin('pear')
'earpay'
'''

# v1 - good idea, but failing strategy
def pigLatin(word):

    # not vowel
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    return word + 'ay'
        

# v1 - good idea, but failing strategy
def pigLatin(word):

    # not vowel
    while word[0] not in 'aeiou':
        word = word[1:] + word[0]
    return word + 'ay'
        


def f(n):
    i = 0
    while n>0:
        n //=10
        i+=1
    return i

'''
>>> f(123)
???
>>> f(123456)
???

f counts the number of digits in a number
'''

'''
make this work:
>>> sumUserNums()
Enter a num: 5
Enter a num: 3
Enter a num: .5
Enter a num:
8.5
'''

# in C/C++/Java not in Python
'''
do:
    body of loop
while condition
'''

#v1 - loop and a half pattern

def sumUserNums():

    total = 0
    x = input('Enter a num: ')   # x = '0'
    while x!='':
        total += eval(x)
        x = input('Enter a num: ')
    return total

        
# v2 - infinite loop pattern

def sumUserNums():
    total = 0
    while True:
        x = input('Enter a num: ')
        if x=='':
            return total
        total += eval(x)
    
# Fibonacci numbers - 1,1,2,3,5,8,13,21,34,...

'''
make this work:
>>> fib(33)
34 # smallest fib at least 33
>>> fib(10)
13
>>> fib(10)
13
>>> fib(6)
8
'''

def fib(n):
    ''' return smallest Fibonacci number
that is at least n'''
    curr,prev = 1,1
    while curr<n:
        curr, prev = curr + prev, curr # python only
        #print( curr,prev)
    return curr
            
    
# tuple assignment works in Python
'''
>>> # swap variables in other languages
>>> x=2
>>> y=3
>>> temp=x
>>> x=y
>>> y=temp
>>> x,y
(3, 2)
>>> # in Python
>>> x,y=y,x
>>> x,y
(2, 3)
>>> 
'''

'''
make this work:
>>> primeFac(72)
[2,2,2,3,3]
>>> primeFac(13)
[13]
>>> primeFac(100)
[2,2,5,5]
'''


def primeFac(n):

    factors = []
    candidate = 2
    while n>1: # not factored yet
        # if n is divisible by candidate
        if n%candidate==0:
            # divide it
            n//=candidate
            factors.append(candidate)
        # otherwise
        else:
            # increase candidate
            candidate+=1
    # give back the factors
    return factors



# similar to hw

'''
we will approximate 2/3 up to a given error, using

2/3 = 1/1 - 1/2 + 1/4 - 1/8 + 1/16 - ....

>>> approx2div3(.001)
.66?
'''


def approx2div3( error ):
    num=1
    denom=1
    prev=0
    curr=1
    while abs(curr-prev)>error:
       num*=-1
       denom*=2
       curr,prev = curr+num/denom,curr
       #print( curr )
    return curr


























