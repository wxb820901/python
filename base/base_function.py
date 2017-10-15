from  random import *
print('-----------------function---------------------')
'''
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a )
        a, b = b, a+b
    print


fib(2000)
f = fib
f(100)
'''

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

#print(fib2(100))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#print(ask_ok(1))

print('---------------------------------------------')

def getById(i):
    if i==1:
        print 'ok'
    elif i==2:
        print '2 ok'
    else:
        print 'not ok'
