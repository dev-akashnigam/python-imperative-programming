print("Please enter the number of rows required in the right angled triangle: ")
row_count = int(input())

for row in range(1, row_count+1, 1):
    for col in range(1, row+1, 1):
        print("*", end=" ")
    print()