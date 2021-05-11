"""
17. a) Create a list of colors from comma-separated color names entered by user.
Display first and last colors
"""

lis = input('ENTER COLORS: ')

colors = lis.split(',')
colours = [] 

for color in colors:
    colours.append(color.strip())

print('LIST OF COLORS - ', colours)

print('FIRST: ', colours[0])

print('LAST: ', colours[-1])