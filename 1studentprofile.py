import datetime
current_time = datetime.date.today()
Name = str(input("Enter the student name : ")) #string is used
Age = int(input("Enter the age of the student : ")) #int is used
Branch = str(input("Enter the branch of student enrolled in : ")) #string is used
College_name = str(input(" Enter the name of the college : ")) # string is used
CGPA = float(input("Enter the CGPA scored by student : "))#float is used

print("NAME: ",Name)
print("AGE :" ,Age)
print("BRANCH :" ,Branch)
print("COLLEGE :" ,College_name)
print("CGPA :" ,CGPA)
print("Profile created on : ", current_time)