
# 5! = 5 * 4 * 3 * 2 * 1 = 120   
# 4! = 4 * 3 * 2 * 1 = 24
# 3! = 3 * 2 * 1 = 6
# 2! = 2 * 1 = 2
# 1! = 1  <- Base Case

# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

def recursive_factorial(n):
    if n == 1:
        return 1 
    return n * recursive_factorial(n-1)

user_input = int(input("Please enter a number to get the sum for: "))
print(recursive_factorial(user_input))

