# 1  2  3  4  5  6
# 1  1  2  3  5  8
# Fib(1) = 1
# Fib(2) = 1

# Fib(5) = Fib(4) + Fib(3) = Fib(3) + Fib(2) + Fib(2) + Fib(1) = 3 + 1 + 1 + 1 = 5
# Fib(4) = Fib(3) + Fib(1) = Fib(2) + Fib(1) + Fib(1) = 1 + 1 + 1 =  3
# Fib(3) = Fib(2) + Fib(1) = 1 + 1 = 2 

# Fib(n) = Fib(n-1) + Fib(n-2)

#                                        Fib(5)
#                           Fib(4)                   +                   Fib(3)
#               Fib(3)          +        Fib(2)                     Fib(2) + Fib(1)
#       Fib(2) + Fib(1)                   1                              1 + 1
#         1 + 1

def recursive_fib(n):
    # Base Case 2 conditions
    if n == 1 or n == 2:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

fibonacci_results ={}

def recursive_fib_memoization(n):
    # Base Case 2 conditions
    if n == 1 or n == 2:
        return 1
    
    if n not in fibonacci_results:
        fibonacci_results[n] = recursive_fib_memoization(n-1) + recursive_fib_memoization(n-2)

    return fibonacci_results[n]


user_input = int(input("Please enter a number: "))
print(recursive_fib_memoization(user_input))