n = int(input("How many rows of stars do you want to print: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()