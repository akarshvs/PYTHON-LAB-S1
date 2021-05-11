# 17. b) Print out all colors from color-list1 not contained in color-list2.

lis1 = ['red','black','blue','green','cyan']
lis2 = ['orange','red','crimson','green']

op = [color for color in lis1 if color not in lis2]

print('COLOR IN LIST 2 BUT NOT IN LIST 1')
print(*op,sep = ',')