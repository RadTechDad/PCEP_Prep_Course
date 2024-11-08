print("Please Enter the 1st Exam Score: ", end="")
exam1 = int(input())

print("Please Enter the 2nd Exam Score: ", end="")
exam2 = int(input())

print("Please Enter the 3rd Exam Score: ", end="")
exam3 = int(input())

avg_exam_score = (exam1 + exam2 + exam3) / 3

print("Average Score", avg_exam_score)
print(f"Average Score {avg_exam_score}")

if avg_exam_score > 100:
    print("A+ -Over 100%!")
elif avg_exam_score >= 90:
    print("A -Great Job!")

