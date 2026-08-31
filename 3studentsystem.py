import datetime
current_time = datetime.date.today()
name = input("Enter your name : ")
age = int(input("Enter your age : "))
college = input("Enter name of the college : ")
branch = input("Enter the branch you are studying in : ")
CGPA = float(input("Enter the CGPA scored : "))
code = input("Enter your favourite programming language : ")

print(name)
print(age)
print(college)
print(branch)
print(CGPA)
print(code)
print(code.lower() == "python" )
print(current_time)

print(name.upper())
print(name.lower())
print(name[0])
print(name[-1])
print(len(name))


