# moreRandom.py


# rps

'''
make this work:
>>> rps('R','P')
1 # player 2 wins
>>> rps('R','R')
0 # tie
>>> rps('R','S')
-1 # player 1 wins
'''

def rps(p1,p2):

    p1+p2
    if p1+p2 in ['RS','SP','PR']:  # in 'RSPR'
        return -1
    elif p1==p2:
        return 0
    else :
        return 1
'''
>>> rps('R','S')
-1
>>> [ (p1,p2,rps(p1,p2)) for p1 in 'RPS' for p2 in 'RPS']
[('R', 'R', 0), ('R', 'P', 1), ('R', 'S', -1), ('P', 'R', -1), ('P', 'P', 0), ('P', 'S', 1), ('S', 'R', 1), ('S', 'P', -1), ('S', 'S', 0)]
>>> [2*i for i in range(10)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
'''

# v2 - no if statements
def rps(p1,p2):
    '''
    d = {'RS':-1, 'SP':-1, 'PR':-1,
         'SR':1,  'PS':1,  'RP':1,
         'RR':0,  'SS':0,  'PP':0 }
    return d[p1+p2]
    '''
    # or just
    return {'RS':-1, 'SP':-1, 'PR':-1,
         'SR':1,  'PS':1,  'RP':1,
         'RR':0,  'SS':0,  'PP':0 }[p1+p2]

'''
>>> simul(1000) # play 1000 times
Player 1
>>> simul(1000) # play 1000 times
Player 2
>>> simul(1000) # play 1000 times
Tie
'''

import random
def simul(n):

    total = 0
    for i in range(n):
        p1=random.choice('RPS')
        p2=random.choice('RPS')
        total+=rps(p1,p2)
    if total>0:
        return 'Player 2'
    elif total<0:
        return 'Player 1'
    else:
        return 'Tie'

'''
make this work:
>>> encode('apple',{'a':'x', 'e':'y'})
'xpply'
'''

def encode( s, d):
    ''' encode string s using dictiontary d as
substitution cipher '''
    outS = ''
    for c in s:
        if c in d:
            outS += d[c]
        else:
            outS += c
    return outS

msg='''
>>> aitmjx xwan
Xwl Flc mo Texwmc, qe Xai Tlxljn

Qlksxaosu an qlxxlj xwkc srue.
Lztuayax an qlxxlj xwkc aituayax.
Naitul an qlxxlj xwkc ymitulz.
Ymitulz an qlxxlj xwkc ymituaykxlh.
Oukx an qlxxlj xwkc clnxlh.
Ntkjnl an qlxxlj xwkc hlcnl.
Jlkhkqauaxe ymscxn.
Ntlyaku yknln kjlc'x ntlyaku lcmsrw xm qjlkb xwl jsuln.
Kuxwmsrw tjkyxaykuaxe qlkxn tsjaxe.
Ljjmjn nwmsuh cldlj tknn naulcxue.
Sculnn lztuayaxue naulcylh.
Ac xwl okyl mo kiqarsaxe, jlosnl xwl xlitxkxamc xm rslnn.
Xwljl nwmsuh ql mcl-- kch tjloljkque mcue mcl --mqdamsn vke xm hm ax.
Kuxwmsrw xwkx vke ike cmx ql mqdamsn kx oajnx sculnn ems'jl Hsxyw.
Cmv an qlxxlj xwkc cldlj.
Kuxwmsrw cldlj an moxlc qlxxlj xwkc *jarwx* cmv.
Ao xwl aitulilcxkxamc an wkjh xm lztukac, ax'n k qkh ahlk.
Ao xwl aitulilcxkxamc an lkne xm lztukac, ax ike ql k rmmh ahlk.
Ckilntkyln kjl mcl wmcbacr rjlkx ahlk -- ulx'n hm imjl mo xwmnl!
'''

msg = msg.upper()

cipher = {'L':'e', 'X':'t', 'K':'a', 'W':'h',
          'C':'n', 'J':'r', 'Q':'b', 'A':'i',
          'N':'s', 'M':'o', 'S':'u', 'R':'g',
          'H':'d'}

print( encode( msg,cipher))








    
    


# substitution cipher



