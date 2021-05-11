"""
10. Prompt the user for a list of integers. For all values greater than 100, store
‘over’ instead.
"""

n = int(input('SIZE: '))
lis = []
for i in range(n): 
    lis.append(int(input('{}: '.format(i+1))))

for i in range(len(lis)):
    if lis[i] > 100: 
        lis[i] = 'over'

print(*lis, sep = ', ')