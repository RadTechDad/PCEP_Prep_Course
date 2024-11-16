variable_1 = 100

# In-place Operation
def test():
    global variable_1
    variable_1 = 200
    global variable_2
    variable_2 = 300                      
    

variable_2 = 70
print(f"before variable_1: {variable_1}")
print(f"before variable_2: {variable_2}")
test()                   
print(f"after variable_1: {variable_1}")
print(f"after variable_2: {variable_2}")