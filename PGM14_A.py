"""
14. (a) Generate positive list of numbers from a given list of integers
"""
n = int(input('SIZE: '))
lis = []
for i in range(n): 
    lis.append(int(input('{}: '.format(i+1))))
op = []

for i in range(len(lis)):
    if lis[i] > 0:
        op.append(lis[i])
print(*op, sep = ', ')
