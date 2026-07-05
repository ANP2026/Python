notes = [
    "Coding: Learn about functions",
    "\nMaths: How to calculate area for a cylinder",
    "\nEnglish: Learn about clauses and phrases",
    "\nScience: Learn about geology",
    "\nSocial Studies: Memorize the 50 states"
]

file = open("all-notes.txt", "w")
file.writelines(notes)
file.close()

num = int(input("How many characters would you like to preview from your notes?"))
file = open("all-notes.txt", "r")
print(file.read(num))
file.close()

file = open("all-notes.txt", "r")
lines = file.readlines()
file.close()
 
print("Total lines in file:", len(lines))
 
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
 
i = 1
file = open("all-notes.txt", "r")
for line in file:
    print(line.strip())
file.close()

word = input("Choose a word to filter out lines that start with that word")
file = open("all-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Filtered out:", line.strip())
    else:
        print("Kept", line.strip())
file.close()

out = open("organized-notes.txt", "w")
for line in lines:
   out.write(line)
out.close() 