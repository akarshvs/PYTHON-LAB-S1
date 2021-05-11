# 21. Write Python code to Find gcd of 2 numbers using function.
def fact(n):
    fact = set()
    for i in range(1,n+1):
        if n % i == 0:
            fact.add(i)
    return fact 

n1 = int(input('NUM1: '))
n2 = int(input('NUM2: '))

cfact = set.intersection(fact(n1),fact(n2))
cfact = sorted(cfact)
print('GCD OF {} AND {} IS: {}'.format(n1,n2,cfact[-1]))
