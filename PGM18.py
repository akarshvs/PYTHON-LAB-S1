# 18. Write Python code to Merge two dictionaries.
#  Write Python code to Merge two dictionaries.

dic1 = {7: 'AKARSH', 1: 'ABHI' , 25: 'JOJO', 38: 'MIDHUN'}
dic2 = {7: 'AKARSH', 6: 'AJAY' , 25: 'JOJO', 8: 'AKHIL'}

dic1.update(dic2)
op = dic1
for i in op:
    print(i,op[i],sep=' - ')