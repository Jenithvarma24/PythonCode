# Program to determine a student's grade based on their score
# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

print("The student's grade is:", grade)
