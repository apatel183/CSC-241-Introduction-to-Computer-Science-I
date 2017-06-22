# hwsample.py

'''
in general:

    module/file should run without errors
    as submitted

    working code should not be commented

    IDLE exercises, test runs should be commented out
'''

'''
IDLE exercises

>>> a = 'hello'
>>> b = 'bye'
>>> 5*a+b
'hellohellohellohellohellobye'
>>> 5*(a+b)
'hellobyehellobyehellobyehellobyehellobye'
>>> 
'''

# for each program

# program 

'
f = eval(input('Enter a temperature in Fahrenheit: '))
if f<32:  #True
    print("It's cold!!!")
    print('Put a jacket on.')
else:     #False
    print("It's warm!!!")
print('Thanks, see you later.')

# test runs

'''
>>> ================================ RESTART ================================
>>> 
Enter a temperature in Fahrenheit: 23
It's cold!!!
Put a jacket on.
Thanks, see you later.
>>> ================================ RESTART ================================
>>> 
Enter a temperature in Fahrenheit: 40
It's warm!!!
Thanks, see you later.
>>> ================================ RESTART ================================
>>> 
Enter a temperature in Fahrenheit: 32
It's warm!!!
Thanks, see you later.
>>> 
'''
# program 2


n = eval( input('Enter an int: ') )
if n%2==1:   # could also:  n%2!=0,  n%2
    print(n,'is odd')
else:
    print(n,'is even')

# test runs
'''
>>> ================================ RESTART ================================
>>> 
Enter an int: 4
4 is even
>>> ================================ RESTART ================================
>>> 
Enter an int: 7
7 is odd
'''












