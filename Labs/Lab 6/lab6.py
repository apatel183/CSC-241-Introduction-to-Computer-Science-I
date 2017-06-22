###Arpan Patel###
###Lab6.py###

#Question 1#

def dromes(filename):
    ans= []
    #to return list of words without puntnation
    infile=open(filename)
    content=infile.read()
    infile.close()
    #content right now is a string of the contant
    table=str.maketrans('.,:!?:\n',7*' ')
    words= content.translate(table).split()
    for letter in words:
        if len(letter)> 1 and letter.upper()==letter.upper()[::-1]:
            ans.append(letter)
    return ans

#test
'''
>>> dromes('text1.txt')
['wow', 'Malayalam', 'wow', 'tattarrattat', 'wow', 'Senones', 'SIXAXIS', 'soosoos', 'Tacocat', 'Zerorez', 'wow', 'wow', 'wow', 'wow', 'wow', 'wow']
>>> dromes('text2.txt')
['wow', 'wow', 'wow', 'did', 'wow', 'wow', 'Kanak', 'kayak', 'kelek', 'level', 'Liril', 'wow']

'''

#Question 2#

def multiplesOf(n,lst):
    indices=[]
    for i in range(len(lst)):
        if lst[i]% n==0:
            indices.append(i)
    return indices
#test
'''
>>> multiplesOf( 3, [3,1,6,2,7,9,10,20,3] )
[0, 2, 5, 8]
>>> multiplesOf( 5, [3,1,6,2,7,9,10,20,5] )
[6, 7, 8]
>>> multiplesOf( 13, [3,1,6,2,7,9,10,20,5] )
[]
'''

#Question 3#

def mod(x,y):
    while x-y >= 0:
        x-= y
    return x

#test
'''
>>> multiplesOf( 3, [3,1,6,2,7,9,10,20,3] )
[0, 2, 5, 8]
>>> multiplesOf( 5, [3,1,6,2,7,9,10,20,5] )
[6, 7, 8]
>>> multiplesOf( 13, [3,1,6,2,7,9,10,20,5] )
[]
'''
#Question 4 #

def coins(dollars):
    ans=[]
    coins=[25,10,5,1]
    while dollars > 0:
        for coin in coins:
            if dollars - coin>=0:
                ans.append(coin)
                dollars -= coin
                break
    return ans

#test
'''
>>> coins(26)
[25, 1]
>>> coins(81)
[25, 25, 25, 5, 1]
>>> coins(234)
[25, 25, 25, 25, 25, 25, 25, 25, 25, 5, 1, 1, 1, 1]
>>> coins(22)
[10, 10, 1, 1]
>>> [ (i,coins(i)) for i in range(0,100,7)]
[(0, []), (7, [5, 1, 1]), (14, [10, 1, 1, 1, 1]), (21, [10, 10, 1]), (28, [25, 1, 1, 1]), (35, [25, 10]), (42, [25, 10, 5, 1, 1]), (49, [25, 10, 10, 1, 1, 1, 1]), (56, [25, 25, 5, 1]), (63, [25, 25, 10, 1, 1, 1]), (70, [25, 25, 10, 10]), (77, [25, 25, 25, 1, 1]), (84, [25, 25, 25, 5, 1, 1, 1, 1]), (91, [25, 25, 25, 10, 5, 1]), (98, [25, 25, 25, 10, 10, 1, 1, 1])]
>>>
'''
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab6TEST.py') )
    

