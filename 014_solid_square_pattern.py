print("Please enter the number of rows required in the solid square pattern: ")
row_count = int(input())

col_count = row_count

for row in range(1, row_count+1, 1):
    for col in range(1, col_count+1, 1):
        print("*", end=" ")
    print()