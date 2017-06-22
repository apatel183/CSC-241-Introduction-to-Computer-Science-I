###ARPAN PATEL###
###HW5###

def subStrings(lst):
    ans=[]
    for letters in range(len(lst)-1):
        if lst[letters+1] in lst[letters]:
            ans.append(lst[letters+1])
    return ans

#Output
'''
>>> subStrings(['apple','app','pp','orange','range','ra'])
['app', 'pp', 'range', 'ra']
>>> subStrings(['apple','app','pp','orange','range','pineapple'])
['app', 'pp', 'range']
>>> subStrings(['apple'])
[]
>>> subStrings([])
[]
>>>

''' 

def poly(lst,x):
    ans=0
    term=0
    power=0
    for num in lst:
        term=num * (x**power)
        ans += term
        power += 1
    return ans

#Output
'''
>>> poly(  [1,2,1], 2 )
9
>>> poly( [1,0,1,0,1], 2 )
21
>>> poly( [1,0,1,0,1], 3 )
91
'''
def collatz(number):
    ans = [number]
    while number > 1:
       if number % 2 == 0:
         number = int (number/2)
       else:
         number = (number*3)+1
       ans.append(number)
    return ans
#OutPut
'''
>>> collatz(10)
[10, 5, 16, 8, 4, 2, 1]
>>> collatz(22)
[22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
'''

def approxPi(x):
    num = 4
    denom = 1 
    prev = 0
    curr = 4
    while abs(curr-prev)>x:
        num*=-1
        denom+=2
        curr,prev= curr+num/denom,curr
    return curr

#Output
'''
>>> approxPi(.5)
3.3396825396825403
>>> approxPi(.05)
3.1659792728432157
>>> approxPi(.005)
3.144086415298761
>>> approxPi(.0005)
3.1418425911015158
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw5TEST.py') )
        
