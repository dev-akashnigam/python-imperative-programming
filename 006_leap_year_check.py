print("Please enter the year: ")
year = int(input())

if year%100 == 0:
    if year%400 == 0:
        print(f"Year: {year} is a leap year")
    else:
        print(f"Year: {year} is NOT leap year")
else:
    if year%4 == 0:
        print(f"Year: {year} is a leap year")
    else:
        print(f"Year: {year} is NOT leap year")