import os

science_notes = [
    "Plants need sunlight and water\n","The Earth moves around the Sun\n","Water can change into ice and steam\n"]
 
maths_notes = [
    "Addition means finding the total\n","Subtraction means taking away\n","Multiplication is repeated addition\n"]
with open("science-notes.txt", "w") as f:
    f.writelines(science_notes)
with open("maths-notes.txt", "w") as f:
    f.writelines(maths_notes)
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words),"words ->",line.strip())
merged_file = "merged_notes.txt"
if os.path.exists(merged_file):
    print(merged_file, "already exists")
else:
    print(merged_file, "hasn't been made yet")
if os.path.exists(merged_file):
    os.remove(merged_file)
    print("Old Merged file removed")
else:
    print("No merged file to remove")
with open(merged_file, "w") as output:
    output.writelines(science_notes)
    output.writelines(maths_notes)
with open(merged_file, "r") as output:
    for line in output:
        print(line.strip())