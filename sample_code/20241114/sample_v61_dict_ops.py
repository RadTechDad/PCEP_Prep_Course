dictionary = {
    "apple" : "A red fruit.",
    "banana" : "A yellow fruit.",
}

# Add a new key-value pair
#           Key        Value
dictionary["mango"] = "A tropical fruit."

print(dictionary)

# Update an existing key-value pair
#            Key      Value
dictionary["apple"] = "A fruit that is red."

# When we want to retreive element that may or may not exist
# And we don't want an error if the element does not exist
result = dictionary.get("apple")
print(result)

result = dictionary["apple"]
print(result)


result = dictionary.get("grape") # Grape doesn't exist -> None
print(result)

print(list(dictionary.items()))


# Will cause an error if the key does not exist
# print(dictionary["grape"] ) # -> Will cause an error