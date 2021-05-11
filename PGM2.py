# 2. Write a Python program to find the largest among three numbers.
num1 = int(input("NUMBER 1: "))
num2 = int(input("NUMBER 2: "))
num3 = int(input("NUMBER 3: "))

if(num1 > num2 and num1 > num3):
    G = num1
elif(num2 > num3 and num2 > num1):
    G = num2
else:
    G = num3
print("GREATEST",G)