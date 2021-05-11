# 12. From a list of integers, create a list removing even numbers.

n = int(input('SIZE: '))
lis = []
for i in range(n): 
    lis.append(int(input('{}: '.format(i+1))))
k = 0
for j in range(len(lis)):
    if lis[k] % 2 == 0:
        lis.remove(lis[k])
        k-=1
    k+=1
print('OUTPUT: ', end='')
print(*lis,sep=', ')
