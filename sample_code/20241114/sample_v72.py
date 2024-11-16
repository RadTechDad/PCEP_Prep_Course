# result = 0
# result += 1
# result += 2
# result += 3
# result += 4
# result += 5
# print(result)

# sum(5) = 5 + 4 + 3 + 2 + 1 = 15   
# sum(4) = 4 + 3 + 2 + 1 = 10
# sum(3) = 3 + 2 + 1 = 6
# sum(2) = 2 + 1 = 3
# sum(1) = 1

# sum(5) = 5 + sum(4)
# sum(4) = 4 + sum(3)
# sum(3) = 3 + sum(2)
# sum(2) = 2 + sum(1)
# sum(1) = 1 # Base Case 

# Call Stack
# sum(1) -> 1 
# sum(2) -> 2 + 1 => 3
# sum(3) -> 3 + 3 => 6
# sum(4) -> 4 + 6 => 10
# sum(5) -> 5 + 10 => 15

def recursive_sum(n):
    if n == 1: # Base Case
        print(f"N={n} Returning 1")
        return 1
    print(f"N={n} Calling recursive_sum({n-1})")
    partialResult = recursive_sum(n-1)
    print(f"N={n} Returning {n} + {partialResult} => {n + partialResult}")
    return n + partialResult

# Outside the function
user_input = int(input("Please enter a number to get the sum for: "))
print(recursive_sum(user_input))