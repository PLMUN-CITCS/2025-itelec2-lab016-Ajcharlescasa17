# Generate a 5x5 multiplication table
for i in range(1, 6):  # Outer loop for rows (1 to 5)
    for j in range(1, 6):  # Inner loop for columns (1 to 5)
        product = i * j  # Calculate the product
        print(f"{product:4}", end="")  # Print with formatting (width 4)
    print()  # Move to the next row after each inner loop iteration