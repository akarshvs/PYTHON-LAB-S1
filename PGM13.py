# 13. Accept a list of words and return length of longest word.

n = int(input('SIZE: '))
lis = []
for i in range(n): 
    lis.append(input('WORD {}: '.format(i+1)))
lword = ''

for j in range(len(lis)):
    lword = lis[j] if len(lis[j]) > len(lword) else lword

print('LONGEST WORD:', lword, ',LENGTH:',len(lword))