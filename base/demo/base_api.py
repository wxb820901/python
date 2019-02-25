import sys

x = 5
y = "John"
print(x)  #5
print(y)  #John
print("-------------------1-----------------------")
x = 4 # x is of type int
x = "Sally" # x is now of type str   //TypeError: unsupported operand type(s) for //: 'NoneType' and 'int'
print(x)
print("-------------------2-----------------------")
x = "awesome"
print("Python is " + x)
print("-------------------3-----------------------")
x = "Python is "
y = "awesome"
z =  x + y
print(z)
print("-------------------4-----------------------")
x = 5
y = 10
print(x + y)
print("--------------------5----------------------")
x = 5
y = "John"
#print(x + y)#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("--------------------6----------------------")
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
print("--------------------7---------------------")
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
print("--------------------8----------------------")
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
print("--------------------9----------------------")
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print("--------------------10----------------------")
x = 3+5j
y = 5j
z = -5j
print(x); print(type(x))
print(y); print(type(y))
print(z); print(type(z))
print("--------------------11----------------------")
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print("--------------------12----------------------")
a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))  # returns ['Hello', ' World!']
print("--------------------13----------------------")
print('--------------------14operator------------------')
answer = 1+1
print('1+1='+ str(answer))
answer = 50 - 5*6
print('50 - 5*6='+ str(answer))
answer = 8 / 5
print('8 / 5='+ str(answer))
answer = 1+1
print('1+1='+ str(answer))

answer = 17 / 3
print('17 / 3='+ str(answer))
answer = 17 // 3
print('17 // 3='+ str(answer))
answer = 17 % 3
print('17 % 3='+ str(answer))
answer = 5 * 3 + 2
print('5 * 3 + 2='+ str(answer))
answer = 5 ** 2
print(' 5 ** 2='+ str(answer))
answer = 2 ** 7
print(' 2 ** 7='+ str(answer))
