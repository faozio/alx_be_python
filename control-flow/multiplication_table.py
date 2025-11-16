number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(number, number + 1):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{j} * {i} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row

