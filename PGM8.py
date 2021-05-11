"""
8. Create a string from given string where first and last characters exchanged.
[eg: python - >nythop]

"""
s = input('STRING: ')
res = s[-1] + s[1:-1] + s[0] 
print("->",res)