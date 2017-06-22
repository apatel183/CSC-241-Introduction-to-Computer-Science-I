###hw1.py####
###Arpan Patel####

##### IDLE exercises########

'''''
>>> s1= '&'
>>> s2= '#'

a.
>>> 2*s1+s2
'&&#'

b.
>>> 2*s2+s1
'##&'

c. >>> (2*s1+s2)*2
'&&#&&#'

d. >>> 10*s1
'&&&&&&&&&&'

e. >>> (2*s1+2*s2)*3
'&&##&&##&&##'

f. >>> (5*s1+5*s2)*3
'&&&&&#####&&&&&#####&&&&&#####'

'''''



##### Programming problems ######
import math 

def total():

    price = eval (input("Enter a price: "))
    quantity = eval (input("Enter a quantity: "))
    if price > 0 and quantity > 0:
        print( "The total price is: $",price*quantity)
    elif price <=0 or quantity <=0:
        print("Error: both numbers must be greater than zero.")

#OutPut
        '''
>>> total()
Enter a price: 13.25
Enter a quantity: 6
The total price is: $ 79.5
>>> total()
Enter a price: 13.25
Enter a quantity: -6
Error: both numbers must be greater than zero.
>>> total()
Enter a price: 0.0
Enter a quantity: 4
Error: both numbers must be greater than zero.
>>> total()
Enter a price: -23.55
Enter a quantity: 3
Error: both numbers must be greater than zero.
>>> total()
Enter a price: -3.50
Enter a quantity: -4
Error: both numbers must be greater than zero.
>>> total()
Enter a price: 0
Enter a quantity: 0
Error: both numbers must be greater than zero.
>>>
'''
            

def posNegZero():
    number= eval (input("Enter a number: "))
    if number <0:
        print("You entered a negative number.")
    elif number==0:
        print("You entered zero.")
    elif number >0:
        print("You entered a positive number.")

#Output
'''
>>> posNegZero()
Enter a number: -2.3
You entered a negative number.
>>> posNegZero()
Enter a number: 0.0
You entered zero.
>>> posNegZero()
Enter a number: 23.55
You entered a positive number.
>>>
'''

def square():
    
    userInputNumber = input("Enter an integer: ")
    isPerfectSquare = math.sqrt(float(userInputNumber)).is_integer()
    if isPerfectSquare:
        print(str(userInputNumber) + " is " +  str(int(math.sqrt(float(userInputNumber))))+ " squared.")
    else:
       print(str(userInputNumber)+ " is not a perfect square.")

#Output
'''
>>> square()
Enter an integer: 9
9 is 3 squared.
>>> square()
Enter an integer: 12
12 is not a perfect square.
>>> square()
Enter an integer: 0
0 is 0 squared.
>>> square()
Enter an integer: 7
7 is not a perfect square.
>>>
'''
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py') ) 

        
    
    
        


