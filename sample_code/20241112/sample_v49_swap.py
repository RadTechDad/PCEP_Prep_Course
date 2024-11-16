#             0       1        2       3         4            5       6
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Swap Apple <-> Fig
# 3 Variable /3 Line Swap

# Storing one of the two elements in a temporary variable
temp = fruits[0] # apple
# Which ever value we stored get overridden by its new value
fruits[0] = fruits[5] # fig
print(fruits)
# Replace the second value with the stored value
fruits[5] = temp # apple
print(fruits)

# Multi-Assign Swap - Restore Apple to 0 and Fig to 5
fruits[0], fruits[5] = fruits[5], fruits[0]
print(fruits)