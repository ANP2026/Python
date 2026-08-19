#PART 1: Slices of any array
numbers=[2,-5,3,4,-1,6,-3]
print("Full array:", numbers)
print("Some sub-arrays:")
print("[0:2]=", numbers[0:2], "sum=", sum(numbers[0:2]))
print("[2:6]=", numbers[2:6], "sum=", sum(numbers[2:6]))
print("[3:7]=", numbers[3:7], "sum=", sum(numbers[3:7]))
print()
#Part 2 The drag of negatives. Running some with reset
print("Running some traces")
running=0
for number in numbers:
    running+=number
    if running<0:
        print(f"{number} -> sum={running} <- negative reset to zero")
        running=0
    else:
        print(f"{number} -> sum={running}")
print()
#Part 3: Best so far. capture best before reset
running=0
best=0
for num in numbers:
    running+=num
    if running<0:
        running=0
    if running>best:
        best=running
print("Array:", numbers)
print("Max Sub array sum:", best)
print()
#Kadane on a harder array
hard=[1,2,4,-5,-22,0,25,2,9]
running=00
best=0
for n in hard:
    running+=n
    if running<0:
        running=0
    if running>best:
        best=running
        best==running
print("Array:", hard)
print("Max Sub array sum:", best)
print()