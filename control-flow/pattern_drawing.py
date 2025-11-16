rows = int(input("Enter the size of the pattern: "))

# Outer loop implemented with while; inner loop uses for
i = 0
while i < rows:
    # Print one row: inner for-loop prints 'rows' asterisks
    for j in range(rows):
        print("*", end="")
    print()  # move to next line after the row
    i += 1