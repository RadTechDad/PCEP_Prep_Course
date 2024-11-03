# Exercise 1
############################################

print('\n# -=[ Exercise 1 ]=- ############################################\n')

# Message 1
print("Hello World")
print()
# Message 2
print("Welcome to the Land of Python!\nMay your journey be insightful and enlightening!")



# Exercise 2
############################################

print('\n\n\n# -=[ Exercise 2 ]=- ############################################\n')

papers_submitted = int(input("How many papers were submitted? "))
number_of_students = int(input("How many students are in the class? "))

if number_of_students == 0:
    print("No students in the class. Exiting program.")
    exit()

avg_papers_per_student = papers_submitted / number_of_students

print("The average number of papers submitted per student is", avg_papers_per_student)



# Exercise 6
############################################

print('\n\n\n# -=[ Exercise 6 ]=- ############################################\n')

number_of_hours = int(input("Enter the number of hours: "))
number_of_minutes = int(input("Enter the number of minutes: "))

hour_minutes = number_of_hours * 60
total_minutes = hour_minutes + number_of_minutes

total_hours = total_minutes // 60
total_minutes = total_minutes % 60

print("Total hours:", total_hours)
print("Total minutes:", total_minutes)

