print("Please enter the natural number till where sum is required: ")
num = int(input())

sum = 0
for i in range(1, num+1, 1):
    sum += i

print(f"Sum of first {num} natural numbers = {sum}")