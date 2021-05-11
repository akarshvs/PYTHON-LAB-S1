"""
24. Create a text file “PyIntro.txt” with contents:
 Python is a powerful general-purpose programming language.
 It is used in web development, data science, creating software prototypes, and so on. Fortunately for beginners, Python has simple easy-to-use syntax. 
This makes Python an excellent language to learn to program for beginners. 
"""

message ="""Python is a powerful general-purpose programming language.\n\n
It is used in web development, data science, creating software prototypes, and so on.\n
Fortunately for beginners, Python has simple easy-to-use syntax.\n\n 
This makes Python an excellent language to learn to program for beginners."""

with open('PyIntro.txt', 'w') as file:
    file.write(message)
    print('SUCCESS!')

