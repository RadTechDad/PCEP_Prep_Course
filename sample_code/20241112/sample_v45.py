print(range(10))
print(list(range(10)))

for x in range(10):
    print(x, end=", ")

numbers = [ 100, 40, 30]
for index in range(len(numbers)):
    print(f"Index: {index}, numbers[index]: {numbers[index]}")