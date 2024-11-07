# GOAL: Ask the user for the month and the day, then say what day it will be in 10 days

month = input("Enter the month: ")
day_of_the_month = input("Enter the day of the month: ")

print("Today is", month,  day_of_the_month)
print("In 10 days, it will be", month, (int(day_of_the_month) + 10) % 30 )