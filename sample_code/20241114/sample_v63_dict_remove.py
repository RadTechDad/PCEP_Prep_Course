fruits1 = {
    "apple" : "A red fruit.",
    "banana" : "A yellow fruit.",
    "mango" : "A tropical fruit.",
}

# Remove a key-value pair
del fruits1["apple"]

print(f"Full fruits:", fruits1)

# Pop a key-value pair
# Removes the most recently added key-value pair
result = fruits1.popitem()
print(f"Removed element:", result)

print("Full fruits:", fruits1)