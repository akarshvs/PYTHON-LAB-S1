"""
15. Write a Python program to Add ‘ing’ at the end of a given string.
If it already ends with ‘ing’, then add ‘ly’.
"""
string = input('ENTER STRING: ')
print(string[:-3] + 'ly' if string[-3:] == 'ing' else string + 'ing')
