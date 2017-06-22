# pythonIntro.py - our first class

IDLE:

two modes - mix them
    interactive shell  - on right
    file editor - on left

Keyboard shortcuts in shell:
    alt-p, alt-n: prev, next command
    ctrl-n : new file
    enter on a prev command, reloads it

##### interactive shell #####

use Python as a calculator, in order of precedence
can generate expressions using these operators

    ()
    **
    *,/,// (div), % (mod)
    + -
    

>>> 2+3
5
>>> 2/3
0.6666666666666666
>>> 2*3.4
6.8
>>> sin(3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sin(3)
NameError: name 'sin' is not defined
>>> abs(-3)
3
>>> max(3,4.5)
4.5
>>> 2.0**5
32.0
>>> 2**1/2
1.0
>>> 2**(1/2)
1.4142135623730951
>>> (-2)**(1/2)
(8.659560562354934e-17+1.4142135623730951j)
>>> 8/5
1.6
>>> 8//5
1
>>> 24//5
4
>>> 8%5
3
>>> 24%5
4
>>> # 132 minutes = 2 hours, 12 minutes
>>> 132//60
2
>>> 132%60
12
>>> 

##### variables #####

variables remember values and give them names

name = expression

    expression is calculated
    result is stored in variable name

    if you refer to name in an expression
    its value is used

variables
    case sensitive
    can be reused
    dont care what (type) they hold
    vars() - list current variables
    cant refer to a variable before assignment

>>> 2+3
5
>>> x=2+3
>>> x
5
>>> x*4
20
>>> y=x*100
>>> y
500
>>> 
>>> 
>>> x*100=y
SyntaxError: can't assign to operator
>>> 
>>> x
5
>>> y
500
>>> X
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    X
NameError: name 'X' is not defined
>>> z
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> vars()
{'__name__': '__main__', 'x': 5, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__package__': None, '__doc__': None, '__builtins__': <module 'builtins' (built-in)>, '__spec__': None, 'y': 500}
>>> 5*x
25
>>> z
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> z = 'hello'
>>> vars()
{'z': 'hello', '__name__': '__main__', 'x': 5, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__package__': None, '__doc__': None, '__builtins__': <module 'builtins' (built-in)>, '__spec__': None, 'y': 500}
>>> z
'hello'
>>> 3*z
'hellohellohello'
>>> 
f
>>> f = 32
>>> f-32*5/9
14.222222222222221
>>> (f-32)*5/9
0.0
>>> c=(f-32)*5/9
>>> c
0.0
>>> f=212
>>> c
0.0
>>> c=(f-32)*5/9
>>> c
100.0
>>> 
>>> 
>>> x
5
>>> x=7.7
>>> x
7.7
>>> x = 'hello'
>>> x
'hello'
>>> 

##### boolean expressions #####

Boolean expressions are math (!)
expressions which have a result of True or False

>>> 2<3
True
>>> 4.0 > 5
False
>>> 2<2
False
>>> 2<=2
True
>>> 2=2
SyntaxError: can't assign to literal
>>> 2==2
True
>>> x=98
>>> x!=98
False
>>> 
>>> # test whether x is even
>>> x%2==0
True
>>> x=99
>>> x%2==0
False
>>> # x is even or divisible by 3
>>> x%3==0
True
>>> x%2==0 or x%3==0
True
>>> x=7
>>> x%2==0 or x%3==0
False
>>> # divisible by both 2 and 3
>>> x%2==0 and x%3==0
False
>>> x=2
>>> x%2==0 and x%3==0
False
>>> x=6
>>> x%2==0 and x%3==0
True
>>> # see whether x is one of 2,3,4
>>> # this doesnt work
>>> x
6
>>> x==2 or 3 or 4
3
>>> x==2 or x==3 or x==4
False
>>> x = 4
>>> x==2 or x==3 or x==4
True
>>> 

##### str #####

three ways to make a str(ing):
    ''
    ""
    ''''''

operations
    +
    str*int, int*str
    

>>> word = apple
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    word = apple
NameError: name 'apple' is not defined
>>> word = 'apple'
>>> word
'apple'
>>> sentence = "this is fred's sentence"
>>> sentence
"this is fred's sentence"
>>> sentence = 'this is fred\'s sentence'
>>> sentence
"this is fred's sentence"
>>> lines=''' this is a paragraph
that runs
onto multiple lines
isn't that great
'''
>>> lines
" this is a paragraph\nthat runs\nonto multiple lines\nisn't that great\n"
>>> print( lines )
 this is a paragraph
that runs
onto multiple lines
isn't that great

>>> word+sentence
"applethis is fred's sentence"
>>> 5*word
'appleappleappleappleapple'
>>> -5*word
''
>>> '22'+5
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    '22'+5
TypeError: Can't convert 'int' object to str implicitly
>>> '22'+'5
SyntaxError: EOL while scanning string literal
>>> '22'+'5'
'225'
>>> '22'+str(5)
'225'
>>> int('22')+5
27
>>> int('apple')+5
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int('apple')+5
ValueError: invalid literal for int() with base 10: 'apple'
>>> 




























