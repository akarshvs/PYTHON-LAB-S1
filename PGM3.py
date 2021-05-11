#3. Write a Python program to find the factorial of a number.

n = int(input('NUM :'))
fact = 1
if n < 0:
    print('NO FACTORIAL')
elif n == 0:
    print('FACTORIAL: 1')
else:
    for i in range(2,n+1):
        fact*=i
    print('FACTORIAL: ',fact)
