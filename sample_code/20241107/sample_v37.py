userTargetValue = int(input("Enter a number: "))

# Accumulator Pattern

# Accumulating our partial results
result = 0

# Tracking our location
currentValue = 0

# Loop
while currentValue <= userTargetValue:
    result += currentValue

    # Increment the moving variable
    currentValue += 1

print(f"Result: {result}")
