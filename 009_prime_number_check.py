import math

print("Please enter a number: ")
number = int(input())

if number<=1:
    print(f"Number {number} is NOT PRIME.")
elif number==2:
    print(f"Number {number} is PRIME.")
elif number%2==0:
    print(f"Number {number} is NOT PRIME.")
else:
    sqrt_number = math.isqrt(number)
    is_prime = True
    for i in range(3, sqrt_number+1, 2):
        if number%i==0:
            is_prime = False
            break
    if is_prime:
        print(f"Number {number} is PRIME.")
    else:
        print(f"Number {number} is NOT PRIME.")

