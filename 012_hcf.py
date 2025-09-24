print("Please enter the first number: ")
first_num = int(input())

print("Please enter the second number: ")
second_num = int(input())

if first_num > second_num:
    larger_num = first_num
    smaller_num = second_num
else:
    larger_num = second_num
    smaller_num = first_num

hcf = 1
for i in range(smaller_num, 1, -1):
    if first_num%i==0 and second_num%i==0:
        hcf = i
        break

print(f"HCF of {first_num} and {second_num} = {hcf}")