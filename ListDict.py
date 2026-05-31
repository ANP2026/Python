classmates=["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print(classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[0:3])

classmates.append("Meera")
print("After adding Meera:", classmates)
classmates.pop(-2)
print("After removing Dev", classmates)
classmates.sort()
print("Sorted Alphabetically:", classmates)

teacher = {"name": "Mr.Sharma", "Subject": "Python", "experience": 5}
print(teacher)
print("Subject is:", teacher["Subject"])
print("Experience is:", teacher.get("experience", "Not Found"))
teacher["experience"]=6
teacher["email"]="sharma@gmail.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)

role_num=[1, 2, 3, 4, 5]
names=["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
student_directory=dict(zip(role_num, names))
print("Student directory:", student_directory)
print("The name of the student whose role number is three:", student_directory[3])