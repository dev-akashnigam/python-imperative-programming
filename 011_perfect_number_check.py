print("Please enter a number: ")
number = int(input())

half_of_number = number // 2
sum_of_divisors = 0

for i in range(1, half_of_number+1, 1):
    if number%i==0:
        sum_of_divisors += i

if sum_of_divisors==number:
    print(f"Number: {number} is a PERFECT NUMBER.")
else:
    print(f"Number: {number} is NOT PERFECT NUMBER.")