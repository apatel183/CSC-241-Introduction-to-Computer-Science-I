####hw4.py#### 
####Arpan Patel####

##Problem 1 Partition##

def partition(letter,lst):
    letters=list('ABCDFGHIJKLMNOPQRSTUVWXYZ')
    for word in letter:
        if word=='':
            continue
        elif letters.index(word[0].upper()) >= letters.index(lst.upper()):
            print(word)

#Output
'''
>>> startsWith('a',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
apricot
>>> startsWith('A',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
apricot
>>> startsWith('App',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
>>> startsWith('orang',['apple','ApPle','orange','Apple','kiwi','apricot'])
orange
>>> startsWith('ORANG',['apple','ApPle','orange','Apple','kiwi','apricot'])
orange
>>> startsWith('an',['apple','ApPle','orange','Apple','kiwi','apricot'])
>>> startsWith('ppl',['apple','ApPle','orange','Apple','kiwi','apricot'])
>>>
'''

##Problem 2 Points##
 
def points(x1,y1,x2,y2):
    distance=((y2-y1)**2+(x2-x1)**2)**(1/2)
    if x1==x2:
        print('The slope is infinity and the distance is ' +  str(distance))

    else:
        slope=(y2-y1)/(x2-x1)
        print('The slope is ' + str(slope) +  ' and the distance is ' +str(distance))
#Output
'''
>>> points(0,0,1,1)
The slope is 1.0 and the distance is 1.4142135623730951
>>> points(0,0,0,1)
The slope is infinity and the distance is 1.0
>>> points(3,4,5,6)
The slope is 1.0 and the distance is 2.8284271247461903
>>> points(-12.3,55,99.4,-3.6)
The slope is -0.5246195165622203 and the distance is 126.13821784058946
>>>
'''

##Problem 3 numVowels##

def numVowels(filename):
    v=0
    infile=open(filename)
    content=infile.read()
    infile.close()
    content=content.upper()
    for letter in content:
            if letter=='A':
                v+=1
            if letter=='E':
                v+=1
            if letter=='I':
                v+=1
            if letter=='O':
                v+=1
            if letter=='U':
                v+=1
    return v

#Output
'''
>>> points(0,0,1,1)
The slope is 1.0 and the distance is 1.4142135623730951
>>> points(0,0,0,1)
The slope is infinity and the distance is 1.0
>>> points(3,4,5,6)
The slope is 1.0 and the distance is 2.8284271247461903
>>> points(-12.3,55,99.4,-3.6)
The slope is -0.5246195165622203 and the distance is 126.13821784058946
>>>
'''

##Problem 4 numLen##


def numLen(string,nlength):
    answer=0
    string=string.split()
    for word in string:
        if len(word)==nlength:
            answer+=1
    return answer

#Output
'''
>>> points(0,0,1,1)
The slope is 1.0 and the distance is 1.4142135623730951
>>> points(0,0,0,1)
The slope is infinity and the distance is 1.0
>>> points(3,4,5,6)
The slope is 1.0 and the distance is 2.8284271247461903
>>> points(-12.3,55,99.4,-3.6)
The slope is -0.5246195165622203 and the distance is 126.13821784058946
>>>
'''
                
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw4TEST.py') )
