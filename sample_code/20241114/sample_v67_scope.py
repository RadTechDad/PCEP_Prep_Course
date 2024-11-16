variable_1 = 100

# In-place Operation
def test():                      
    # Read-Only is fine as long as the global variable has already been created 
    # Created before the function is called
    print(f"variable_1: {variable_1}")
    print(f"variable_2: {variable_2}")

variable_2 = 70
test()                   
