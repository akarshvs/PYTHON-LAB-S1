"""
11. Enter 2 lists of integers. Check

(a) Whether list are of same length
(b) whether list sums to same value

"""

lis1 = []
lis2 = []
option = 0
i = 1
print('--LIST 1--')
while True: 
    lis1.append(int(input('{}: '.format(i))))
    i+=1
    option = 0 if int(input('DO YOU WANT TO CONTINUE(1/0)?: ')) == 1 else 1
    if option:
        break
i = 1
print('\n--LIST 2--')
while True: 
    lis2.append(int(input('{}: '.format(i))))
    i+=1
    option = 0 if int(input('DO YOU WANT TO CONTINUE(1/0)?: ')) == 1 else 1
    if option:
        break
print('\n\n')
print({True:'SAME LENGTH!',False:'NOT SAME LENTGTH!'} [len(lis1) == len(lis2)])
print({True:'SAME SUM!',False:'NOT SAME SUM!'} [sum(lis1) == sum(lis2)])

