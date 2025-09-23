print("Please enter a number: ")
number = int(input())
number_first_copy = number

total_digits_in_number = 0
while number!=0:
    number = number // 10
    total_digits_in_number += 1

number = number_first_copy

sum = 0
while number!=0:
    last_digit = number % 10
    sum = sum + (last_digit ** total_digits_in_number)

    number = number // 10

if sum==number_first_copy:
    print(f"Number {number_first_copy} is ARMSTRONG NUMBER.")
else:
    print(f"Number {number_first_copy} is NOT ARMSTRONG NUMBER.")