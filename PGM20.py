# 20. Generate Fibonacci series of N terms using function.
def fibo(N):
    i,j=0,1
    print('Fibonacci sequence: ',end='')
    for k in range(n):
        j,i = i,j+i
        print(j,end=' ')

n = int(input('How many terms? '))
fibo(n)