fruits = ['apple', 'banana', 'cherry']
newFruits = ["orange", "mango", "grapes"]

print(f"Fruits: {fruits}, length: {len(fruits)}")

fruits.append(newFruits)

print(f"(After Append) Fruits: {fruits}, length: {len(fruits)}")

# Reset fruits
fruits = ['apple', 'banana', 'cherry']

fruits.extend(newFruits)

print(f"(After Exentd) Fruits: {fruits}, length: {len(fruits)}")
