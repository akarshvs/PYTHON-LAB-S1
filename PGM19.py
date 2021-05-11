# 19. Write Python code to Generate all factors of a number using function.
def factors(n):
    fact = []
    for i in range(1,n+1):
        if n % i == 0:
            fact.append(i)
    return fact 

n = int(input('NUM: '))
print('FACTORS OF',n,end=': ')
print(*factors(n),sep=',')