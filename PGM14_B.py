"""
14. (b) Form a list of vowels selected from a given word
"""
v = 'aeiou'
s = input('WORD: ')
op = []
for i in s:
    if i in v:
        op.append(i)
print(*op,sep = ', ')