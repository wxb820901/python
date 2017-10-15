print('-----------------if elif else---------------------')
condition1 = True
condition2 = True
if condition1:
    print("1 True")
elif condition2:
    print("2 True")
else:
    print("else")
print('-----------------for---------------------')
for n in range(2, 4):
    print(n)
print('-----------------for break---------------------')
for n in range(2, 10):#[2:10)
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            print(n, 'is a prime number')
print('-----------------for continue---------------------')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
print('-----------------while pass---------------------')
while True:
    print("while True:")
    pass
    break
