# 4. Display future leap years from current year to a final year entered by user.

cy = int(input("CURRENT YEAR: "))
fy = int(input("FINAL YEAR: "))

print('---LEAP YEARS---')
for year in range(cy,fy+1):
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
            print(year)
        