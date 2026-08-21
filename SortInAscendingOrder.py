import numpy as np
data_type=[("name", "S15"), ("Class" ,int), ("Height", float)]
studentdetail=[("bob", 2, 5.3), ("Billy", 6, 4.9), ("Cheese", 1, 9.4)]
students=np.array(studentdetail, dtype=data_type)
print("Original array:", students)
print("Sort by height:", np.sort(students, order="Height"))