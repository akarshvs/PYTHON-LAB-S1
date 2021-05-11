"""
25. Write Python code  to count the number of vowels, uppercase and lowercase               
       characters in a text file “PyIntro.txt”.
"""
v = 'aeiou'
vc = lc = uc = 0

with open('PyIntro.txt') as file:
    for word in file:
        for char in word:
            if char.lower() in v:
                vc+=1
            if char.isupper():
                uc+=1
            if char.islower():
                lc+=1

print(f'COUNT: VOWELS - {vc}, UPPERCASE - {uc}, LOWERCASE - {lc}')



