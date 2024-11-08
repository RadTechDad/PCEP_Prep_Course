fruit_tuple = ('apple', 'banana', 'cherry')
print(f"type(fruit_tuple): {type(fruit_tuple)}, fruit_tuple: {fruit_tuple}")

# Parens, no comma -> str
fruits = ('apple' )
print(f"type(fruits): {type(fruits)}, fruits: {fruits}")

# Parens with comma -> tuple <- Recommended Parens + comma is best style
fruits = ('apple', )
print(f"type(fruits): {type(fruits)}, fruits: {fruits}")

# comma -> tuple
fruits = 'apple',
print(f"type(fruits): {type(fruits)}, fruits: {fruits}")

# Error - Tuple are immutable (cannot be changed)
fruits[1] = 'mango'