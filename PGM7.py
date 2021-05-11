"""
7. Get a string from an input string where all occurrences of first character replaced
with ‘$’, except first character.
[eg: onion ->oni$n]
"""
s = input('STRING: ')
f = s[:1]
s = s[:1] + s[1:].replace(f,'$') 
print(s)