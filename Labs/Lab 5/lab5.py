###Arpan Patel###
###Lab5.py###

#Question 1#

def doubles(lst):
    for i in range(len(lst)-1):
        if lst[i]*2==lst[i+1]:
            print(lst[i+1],end= " ")
#test
'''
>>> doubles( [4,8,-12,-24,48,3,6,12,24,2])
8 -24 6 12 24 
>>> doubles([1,2,3,4,5])
2 
>>> doubles([])
>>>
'''

#Question 2#

def oddSpots(num):
    answer=[]
    for i in range(len(num)):
        if num[i]%2 !=0:
            answer.append(i)
    return answer
#test
'''
>>> doubles( [4,8,-12,-24,48,3,6,12,24,2])
8 -24 6 12 24 
>>> doubles([1,2,3,4,5])
2 
>>> doubles([])
>>>
'''

#Question 3#

def summands(tar,lst,lst1):
    ans =[]
    for num in lst:
       for i in lst1:
           if num + i == tar:
                ans.append((num,i))
    return ans

#test
'''
>>> summands( 5, [1,2,3],[1,2,3,5])
[(2, 3), (3, 2)]
>>> summands( 6, [1,2,3],[1,2,3,5])
[(1, 5), (3, 3)]
>>> summands( 12, [1,2,3],[1,2,3,5])
[]
>>> summands( 25, range(20), range(6) )
[]
>>> summands( 25, range(20), range(8) )
[(18, 7), (19, 6)]
'''
def tri(number):
    space=0
    for i in reversed(range(1,number+1)):
        print(" "*space,end='')
        for j in reversed(range(1,i+1)):
            print(j, end='')
        space+=1
        print('')
#test
'''
>>> tri(3)
321
 21
  1
>>> tri(4)
4321
 321
  21
   1

>>> tri(5)
54321
 4321
  321
   21
    1

>>> tri(7)
7654321
 654321
  54321
   4321
    321
     21
      1

'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab5TEST.py') )
    
