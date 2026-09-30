subjects = {
    "Python" : 85,
    "Maths" : 72,
    "Engineering" : 68,
    "Physics" : 91
}

subject_names = set(subjects.keys())

name = input("Enter the name of the Student : ")

print("--------- RESULT ----------")
print("Student : ", name)
print("Marks obtained in each subject ")
for subject in subjects:
    print(subject, subjects[subject])
total_marks = sum(subjects.values())
average_marks = total_marks/len(subjects)
print("Total marks : " ,total_marks)
print("Average : " ,average_marks)

if average_marks >= 85:
        result = "Excellent"
elif average_marks >= 60:
        result = "Good"
elif average_marks >= 40:
        result = "Pass"
else:
        result = "Fail"
print("Result: " ,result)

highest_marks = max(subjects.values())
lowest_marks = min(subjects.values())
print("Highest mark : ",highest_marks)
print("Lowest mark : ", lowest_marks)
print("Subjects : " ,subject_names)

