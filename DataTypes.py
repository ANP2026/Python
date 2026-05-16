name = "Abhi"
age = 12
is_student = True
weight = 92.3

print("type of name", type(name))
print("type of age", type(age))
print("type of is_student", type(is_student))
print("type of weight", type(weight))

print("After type casting...")
weight = int(weight)
age = float(age)
print(age, weight)
print("type of age", type(age))
print("type of weight", type(weight))