# Exercise 3
########################################################################
print('\n# -=[ Exercise 3 ]=- ############################################\n')

string1 = input("Please enter the first message: ")
string2 = input("Please enter the second message: ")

if string1 == string2:
    print("The phrases are the same.")
else:
    print("The phrases are different.")



# Exercise 9
########################################################################
print('\n# -=[ Exercise 9 ]=- ############################################\n')

score1 = int(input("Enter Test #1: "))
score2 = int(input("Enter Test #2: "))
score3 = int(input("Enter Test #3: "))

avg_score = (score1 + score2 + score3) / 3

print(f"The avg is {avg_score:.1f}")

if avg_score >= 99:
    print("A+ Great Job!")
elif avg_score >= 90:
    print("A")
elif avg_score >= 80:
    print("B")
elif avg_score >= 70:
    print("C")
elif avg_score >= 60:
    print("D")
else:
    print("F")

# Exercise 12
########################################################################
print('\n# -=[ Exercise 12 ]=- ############################################\n')

import math

PI = math.pi

dimension = float(input("Enter the side/diameter length: "))

def calculate_circle_area(dimension):
    return PI * ((dimension / 2) ** 2)

area_of_circle = calculate_circle_area(dimension)


def calcluate_triangle_area(dimension):
    return (math.sqrt(3) / 4) * (dimension ** 2)

area_of_triangle = calcluate_triangle_area(dimension)


def calculate_square_area(dimension):
    return dimension ** 2

area_of_square = calculate_square_area(dimension)


print(f"Area of the Circle is: {area_of_circle:.15f}")
print(f"Area of the Triangle is: {area_of_triangle:.15f}")
print(f"Area of the Square is: {area_of_square:.15f}")


# Exercise 17
########################################################################
print('\n# -=[ Exercise 17 ]=- ############################################\n')

military_time = int(input("Enter the Military Time value: "))

if military_time < 0 or military_time > 24:
    print("Not a valid time")

def xor(a, b):
    return bool(a) != bool(b)

if xor((0 <= military_time <= 7), (19 <= military_time <= 24)):
    print("Night Time")
else:
    print("Day Time")
