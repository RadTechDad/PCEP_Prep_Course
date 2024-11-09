# Exercise 25 - Let's explore printing squares
###############################################################################

print('\n# -=[ Exercise 25 ]=- ############################################\n')

print("Program outputs the square of integers between the given range.")
range_start = int(input("Enter a start number: "))
range_end = int(input("Enter end number: "))

padding = 3
spacer = " " * padding
number_header = "Number"
number_header = spacer + number_header + spacer
number_header_length = len(number_header)

square_header = "Square"
square_header = spacer + square_header + spacer
square_header_length = len(square_header)

text_header = f"{number_header:<{number_header_length}}{square_header:<{square_header_length}}"
print(text_header)
print("-" * len(text_header))

for i in range(range_start, range_end + 1):
    square = i ** 2
    print(f"{spacer}{i:>{padding}} {square:>{number_header_length}}{spacer}")


# Exercise 27 - Let's explore asking for numbers
###############################################################################

print('\n# -=[ Exercise 27 ]=- ############################################\n')

# Ask the user for the number of students in the class and how many tests were
# administered. Then prompt the user for the student’s test scores. Print out the
# average score for each of the students.

students_in_class = int(input("How many students are in the class? "))
tests_per_student = int(input("How many tests per student? "))

class_list = []

for student in range(students_in_class):
    student_scores = []
    student_header = f"Student #{student + 1}"

    print()
    print(student_header)
    print("-" * len(student_header))

    for test in range(tests_per_student):
        score = float(input(f"Score for Test #{test + 1}: "))
        student_scores.append(score)

    # Calculate the average score for the student
    average_score = sum(student_scores) / len(student_scores)
    print(f"The average score for Student #{student_header}: {average_score:.1f}")

    class_list.append
   
