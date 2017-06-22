####Arpan Patel#####
####lab8.py####

import random

def findMinRow(num):
    lst=[]
    if len(num)<1:
        return -1
    for i in num:
        lst.append(sum(i))
    new=min(lst)
    return lst.index(new)
'''
>>> findMinRow([])
-1
>>> findMinRow( [ [1,2,5],[2,2],[1,3],[7] ] )
1
>>> findMinRow( [ [1,2,5],[2,2],[1,3],[7],[99,99,-200] ] )
4
>>>
'''

###Question 2####
    
def anagram(letter1,letters2):
    Firstlist = list(letter1)
    Secondlist = list(letters2)
    Firstlist.sort()
    Secondlist.sort()
    if Firstlist == Secondlist:
        return True
    else:
        return False
#test
'''
>>> anagram('otto','toto')
True
>>> anagram('to','otto')
False
>>> anagram('dormitory','dirtyroom')
True
>>>
'''

###Question3#####
def mirror(wrd):
    mirr={'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o',
         'p':'q','q':'p','t':'t','u':'u','v':'v','w':'w','x':'x'}
    try:
        if len(wrd)==1:
            return mirr[wrd]
        for letter in wrd:
            if mirr[letter] in wrd:
                return "".join(mirr[letter] for letter in reversed(wrd))
    except KeyError:
        return 'INVALID'
#test
'''
>>> mirror('vow')
'wov'
>>> mirror('wood')
'boow'
>>> mirror('bed')
'INVALID'
>>> mirror('pout')
'tuoq'
>>> mirror( mirror('pout') )
'pout'
>>> [(c,mirror(c)) for c in 'abcdefghijklmnopqrstuvwxyz']
[('a', 'INVALID'), ('b', 'd'), ('c', 'INVALID'), ('d', 'b'), ('e', 'INVALID'), ('f', 'INVALID'), ('g', 'INVALID'), ('h', 'INVALID'), ('i', 'i'), ('j', 'INVALID'), ('k', 'INVALID'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'q'), ('q', 'p'), ('r', 'INVALID'), ('s', 'INVALID'), ('t', 't'), ('u', 'u'), ('v', 'v'), ('w', 'w'), ('x', 'x'), ('y', 'INVALID'), ('z', 'INVALID')]
>>>
'''

####Question4####
def numPicks():
    lst= []
    while len(set(lst)) == len(lst):
        number = lst.append(random.randint(0,9))
    return len(lst)

#test
'''
>>> random.seed(15)   
>>> numPicks()  # simulation: 3 0 8 0
4
>>> random.seed(11)
>>> numPicks()  # simulation: 7 8 7
3
>>> random.seed(0)
>>> numPicks()  # simulation: 6 6
2
'''
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py') ) 





##Kyle helped####
              
              
