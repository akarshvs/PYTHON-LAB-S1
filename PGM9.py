"""
9. Count the occurrences of each word in a line of text.
"""
s = input('TEXT: ')
w = s.split()
res = {}
for i in w:
    res[i] = s.count(i) 
print("COUNT: ")
for j in res:
    print( j + ": " + str(res[j]))