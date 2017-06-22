###Arpan Patel### 
###Lab7.py###


def reverse(dictionary):
    d={}
    for key in dictionary :
        d[dictionary[key]]=key
    return d
#test
'''
>>> pb = {'eric':'123-4567','sue':'999-9999','sally':'3333'}
>>> pb['sue']
'999-9999'
>>> reverse( pb )
{'999-9999': 'sue', '3333': 'sally', '123-4567': 'eric'}
>>> reverse( pb )['3333']
'sally'

''' 
def letter2number(grade):
    gra={'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1,'D-':0.7,'F':0}
    if grade.upper() not in gra:
        return 'unknown grade'
    return gra[grade.upper()]
#test
'''
>>> letter2number('A-')
3.7
>>> letter2number('c+')
2.3
>>> letter2number('f')
0
>>> letter2number('e')
'unknown grade'
'''
    
def names():
    d= {}
    name= 'start'
    while name != '':
        name= input('Enter next name: ').upper()
        if name in d:
            d[name]+=1
        else:
            d[name]=1
    del d['']
    students=list(d.keys())
    students.sort()
    for x in students:
        if d[x] > 1:
            print('There are', d[x], 'students named', x)
        else:
            print('There are', d[x], 'students named', x)

#test
'''
>>> names()
Enter next name: Frank
Enter next name: frank
Enter next name: Sue
Enter next name: sue
Enter next name: SUE
Enter next name: fraNK
Enter next name: 
There are 3 students named FRANK
There are 3 students named SUE
''' 
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab7TEST.py') )
    
