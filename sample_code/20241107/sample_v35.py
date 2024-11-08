# Sum of values between 50 and 100
startValue = 50
endValue = 100

# Accumulator Pattern

# Accumulating our partial results
result = 0

# Run the calculation
for currentValue in range(startValue, endValue):
    print(f"Adding {currentValue} to {result} which will give us {result + currentValue}")
    result += currentValue

# Display - Outside the patern
print(f"Result: {result}")