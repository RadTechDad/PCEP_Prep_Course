fruits1 = {
    "apple" : "A red fruit.",
    "banana" : "A yellow fruit.",
}

fruits2 = {
    "kiwi" : "A green fruit.",
    "mango" : "A tropical fruit.",
    'apple' : 'A fruit that is red.'
}

# old updates from new
# old.update(new)
# For collisions, the new replaces the old
fruits1.update(fruits2)


print(fruits1)
print(fruits2)