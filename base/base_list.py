print('-----------------list---------------------')
squares = [1, 4, 9, 16, 25]
print("squares ===> "+str(squares))
print("squares + [36, 49, 64, 81, 100] ===> "+str(squares + [36, 49, 64, 81, 100]))
squares[2] = 0
print("squares[2] = 0 ===> "+str(squares))
squares.append(216)
print("squares.append(216) ===> "+str(squares))
squares.append(7 ** 3)
print("squares.append(7 ** 3) ===> "+str(squares))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(str(letters))
letters[2:5] = []
print("letters[2:5] = [] ===> "+str(letters))
a = ['a', 'b', 'c']
print("a = ['a', 'b', 'c']")
n = [1, 2, 3]
print("n = [1, 2, 3]")
x = [a, n]
print("x = [a, n] ===> "+str(x))
print("x[0] ===> "+str(x[0]))
print("x[0][1] ===> "+str(x[0][1]))
print('-----------------range---------------------')
print("range(5, 10) ===> "+str(range(5, 10)))
print("range(0, 10, 3) ===> "+str(range(0, 10, 3)))
print("range(-10, -100, -30) ===> "+str(range(-10, -100, -30)))
lll=list(range(5))
print("lll=list(range(5))) ===> "+str(lll))
