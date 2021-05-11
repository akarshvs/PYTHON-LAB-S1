"""

5. Display the given pyramid
1
2 4
3 6 9
4 8 12 16

"""
for i in range(1,5):
    s = i
    for j in range(i):
        print(s,end =' ')
        s+=i
    print()
