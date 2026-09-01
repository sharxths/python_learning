import datetime
current_time = datetime.date.today()

name = input("Enter your name : ")
age = int(input("Enter your age : "))
college = input("Enter name of the college : ")
branch = input("Enter the branch you are studying in : ")
CGPA = float(input("Enter the CGPA scored : "))
code = input("Enter your favourite programming language : ")

print("Name : ",name)
print("Age :", age)
print(college)
print("Branch : ", branch)
print("CGPA : ",CGPA)
print(" code : ", code)
print(code.lower() == "python" )
print(current_time)

print(name.upper())
print(name.lower())
print(name[0])
print(name[-1])
print(len(name))

skills =[]
s1 = input("python topic you have learnt1 : ")
skills.append(s1)
s2 = input("python topic you have learnt2 : ")
skills.append(s2)
s3 = input("python topic you have learnt3 : ")
skills.append(s3)
s4 = input("python topic you have learnt4 : ")
skills.append(s4)
s5 = input("python topic you have learnt5 : ")
skills.append(s5)

print(skills)
skills.append("OOPS")
skills.insert(7, "c++")

skills.sort()
print(skills)
print(len(skills))









