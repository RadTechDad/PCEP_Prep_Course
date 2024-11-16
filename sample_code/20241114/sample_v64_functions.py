
# def func_name(parameters):
# parameters are the receiver of the value
def sample_add(a, b=100): # Default Value for b of 100
    print(f"Adding {a} and {b} to get {a + b}")
    return a + b

# Arguments are the actual value
# Positional Argument Passing
# result = sample_add(1, 2)
# result = sample_add(1) # 1 for a and 100 for b (from the default value)

# Keyword Argument Passing
# result = sample_add(a=2, b=5)
# result = sample_add(b=5, a=2)
# result = sample_add(a=2) # 2 for a and 100 for b (from the default value)

# Hyprid Argument Passing
# Keyword always has to come after positional
result = sample_add(2, b=5) # 2 for a (posiitonally) and 5 for b is via keyword
print(f"Result: {result}")


# Error 
# result = sample_add(1, 2, 3) # Too many arguments
# result = sample_add() # Not enough arguments
# result = sample_add(b=2)  # Not enough arguments, a is missing 
# result = sample_add(b=5, 2) # Error - Keyword before positional
