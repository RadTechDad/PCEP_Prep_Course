fruits = ['apple', 'banana', 'cherry']

print(f"Fruits: {fruits}, length: {len(fruits)}")

fruits += ["orange", "mango", "grapes"]

# += is like extend 
print(f"(After +=) Fruits: {fruits}, length: {len(fruits)}")

fruits = ['apple', 'banana', 'cherry']

print(f"Fruits: {fruits}, length: {len(fruits)}")

# += to simulate append of a list (we added another layer  of [])
fruits += [   ["orange", "mango", "grapes"]   ]

# Like append
print(f"(After +=) Fruits: {fruits}, length: {len(fruits)}")
