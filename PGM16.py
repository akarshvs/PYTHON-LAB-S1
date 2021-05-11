"""
16. Write a Python program to accept a filename from the user and print the extension of
that.
"""

fname = input('FILE NAME: ')
i = fname.index('.')
print(fname[i+1:])