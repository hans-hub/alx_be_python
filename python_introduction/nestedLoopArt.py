# Define the height of the pyramid
rows = 5

# Initialize row counter
i = 1

# Outer loop for each row
while i <= rows:
    # Print spaces
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1

    # Print asterisks
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    # Move to the next line
    print()
    i += 1