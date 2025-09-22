print("Please enter a number: ")
num = int(input())

original_number = num
reversed_number = 0

while original_number!=0:
    last_digit = original_number % 10
    reversed_number = reversed_number * 10 + last_digit

    original_number = original_number // 10

print(f"Reverse of number {num} = {reversed_number}")