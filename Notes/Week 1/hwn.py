# hwn.py

'''
IDLE exerciese
'''

def sayHello():
    print('Hello, how are you?')


def sayBye():
    print("Bye y'all!")


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hwnTEST.py') )
