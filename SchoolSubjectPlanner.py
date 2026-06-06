student = ("Aarush", "Grade 5", "Section C", 6)
print("Student details:", student)
student_name=student[0]
print("First two details: ", student[0:2])

monday_subjects = {"Math", "English", "Science", "History", "Gym", "Art"}
tuesday_subjects = {"Math", "English", "Science", "History", "Gym", "Music"}

print("Monday's subjects :", monday_subjects)
print("Tueday's subjects :", tuesday_subjects)

monday_subjects.add("Tech")
monday_subjects.discard("Art")
print("After changes to mondays schedule: ", monday_subjects)

all_subjects = monday_subjects.union(tuesday_subjects)
common = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
unique_to_each = monday_subjects.symmetric_difference(tuesday_subjects)

print("Subjects for both days", all_subjects)
print("Common subjects", common)
print("Subjects only on monday", only_monday)
print("Unique to each day subjects", unique_to_each)
