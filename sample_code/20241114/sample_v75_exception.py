
try:
    user_input = float(input("Please enter a number: "))
    print(f"The reciprocal of {user_input} is {1/user_input}")
except ValueError: 
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("0 has no reciprocal.")
except:
    print("An unexpected error occurred.")

# Erros we have seen:
# ZeroDivisionError - 0
# ValueError - Hello


# C++         Python
# try     --  try
# throw   --  raise
# catch   --  except


