##########lab3.py#############
##########Arpan Patel#########

def print3Chars(itemlist):
    for word in itemlist:
        if len(word)<3:
            print(word)
        else:
            print (word[0]+word[1]+word[2])
    
'''
>>> print3Chars(['hello', 'goodbye', 'no', '', 'later'])
hel
goo
no

lat
>>> print3Chars(['a','b'])
a
b
>>> 
'''

def avgLst():
    num= eval (input ('Please enter a list: '))
    if num == []:
        print('n/a')
    else:
        total= sum(num)/len(num)
        return(total)
'''
>>> avgLst()
Please enter a list: [-12.3,77.2,99]
54.63333333333333
>>> avgLst()
Please enter a list: []
n/a
>>> avgLst()
Please enter a list: [3,7,22]
10.666666666666666
>>> [3,7,22]
[3, 7, 22]
>>> avgLst()
Please enter a list: [-12.3,77.2,99]
54.63333333333333
>>> avgLst()
Please enter a list: []
n/a
'''

      

def magnitude(numList):
    if numList== []:
        return ('n/a')
    elif abs(min(numList))>(max(numList)):
        return abs(min(numList))
    else:
        return max(numList)
'''
>>> magnitude([3,4,11,22])
22
>>> magnitude([3,-4,11,-22])
22
>>> magnitude([])
n/a
'''

def printevens(lstNums):
    if len(lstNums)<1:
       print('Sorry, that list is empty.')
    for num in lstNums:
        if num%2==0:
                print(num)

'''
>>> printevens([])
Sorry, that list empty
>>> printevens([3,4,11,22])
4
22
>>> printevens([3,5,11,19])
>>> printevens([])
Sorry, that list empty.
>>> 
'''

def printDivisors(number):
    for num in range(number,0,-1):
        if number % num==0:
            print (number//num)
        

'''
>>> printDivisors(12)
1
2
3
4
6
12
>>> printDivisors(17)
1
17
>>> 
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab3TEST.py') )

  
