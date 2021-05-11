#1. Accept an integer n and compute n+nn+nnn
num = int(input("NUM: "))
print("VALUE: ",(num + ((num * 10) + num) + ((num * 100) + (num * 10) + num)))