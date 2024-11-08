
counter = 0
while counter < 5:
    print("*", end="")
    counter += 1
    if counter == 2:
        print("!", end="")
        break
else:
    print("^", end="")

print("-", end="")


# counter  |   print("*")   |  counter += 1   | counter == 2  | break | print("!") |
# -------------------------------------------------------------------------------- 
#    0     |       *        |        1        |     False     | False |    
#    1     |       *        |        2        |     True      | True  |    !
# No Else --< break
# -

# Final Output: **!-


