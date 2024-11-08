
userTargetValue = int(input("Enter a number: "))

# Accumulator Pattern

# Accumulating our partial results
result = 0

# Run the calculation
targetValue = userTargetValue + 1

for currentValue in range(targetValue):
    result += currentValue

# Display - Outside the patern
print(f"Result: {result}")