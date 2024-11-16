values = [ 5, 0, 10]
for value in values:
    print("*", end="")
    if value % 2 == 0:
        print("!", end="")
        break
    print("@", end="")
else: # <- runs if no break triggered (if it runs, it runs after loop completes)
    print("^", end="")

print("-", end="")
print()


# value   | print("*") |  value % 2 == 0  | print("!") | break |  print("@") |
# -------------------------------------------------------------|--------------
#   5     |    *       |       False      |            |       |      @      |
#   0     |    *       |       True       |     !      | True  |             |
# Break Triggered -> No Else
# -

# Final Output: *@*!-