# elifAccumulate.py

'''
schedule:
    Tues 10/6 - normal
    Thurs 10/8 - double class - 8:30-11:40
    Tues 10/13 - lab
    Thurs 10/15 - midterm - 9:15-11:40


midterm:
    in class, on computer (all programs)
    doctest
    HARDCOPY NOTES - 4 singled sided pages OR
       2 double-sided pages, print these before
       you come!!   no internet access!!  turn in
       with your exam
    book, through chapter 5.2
    to study - practice writing code
    partial credit will be awarded - something is way
       better than nothing
    make sure you are running python 3
    BE ON TIME!

'''

# hw2

'''
>>> firstChars(['apple','pear','','kiwi'])
a
p
k
>>> firstChars([])
the paramater is empty
>>>
'''

def firstChars( lst ):

    if len(lst)==0:   # if lst=[]:
        print('empty')
    else:  # iterate, loop
        for word in lst:
            if word != '':   # if len(word)>0:
                print( word[0] )
        


# hw q's


##### elif #####
'''
run EXACTLY ONE indented block, the first
whose condition is met, or if none met,
run the else block

if condition:
    statements
elif condition:
    statements
...
else:
    statements
'''

'''
make this work:
>>> grade(93.2)
'A'
>>> grade(87.4)
'B'
...
'''

def grade( score ):

    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'

##### accumulator pattern #####

'''
compute an accumulated value/stat
through iteration

each iteration comjputes a partial
"running" value for the portion of
data already seen

useful for:
    count, sum
    max, min
    list of items
    list of indices
    string

4 step process:
0) set up iteration to visit all items of interest
   (print version 1st)
1) before loop - initialize running val
2) inside loop - accumulate/modify running val
3) after loop - return running val

'''

'''
make this work:
>>> total( [22,33,55,88,11] )
???
'''

def total( numlst ):

    #1
    runningTotal=0
    #0
    for num in numlst:
        #2
        #runningTotal = runningTotal + num
        runningTotal += num
        # print(num,runningTotal)
    #3
    return runningTotal

'''
>>> # op= shorthand
>>> x=7
>>> x=x+3
>>> x
10
>>> x+=3
>>> x
13
>>> x-=2
>>> x
11
>>> x+=5
>>> x
16
>>> x//=2
>>> x
8
>>> x*=3
>>> x
24
>>> x+=x
>>> x
48
>>> x%=5
>>> x
3
>>> 

C/C++/Java, not in Python

these are all the same:
c=c+1
c+=1
c++

Also, c--

'''

'''
make this work:
>>> evens([2,4,5,6,7,8])
[2,4,6,8]
>>> evens([1,3,5])
[]
'''

def evens(numlst):

    #1
    answer = []
    #0
    for num in numlst:
        if num%2==0:
            #2
            answer.append(num)
            #print( num )
    return answer  #3

'''
>>> extractVowels('Hello, how are you?')
'eooAou'
'''

def extractVowels( s ):

    ans = ''
    for c in s:
        if c in 'aeiouAEIOU':
            ans+=c
    return ans



























