#Part1 Streak counter with reset
binary=[0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
streak=0
for num in binary:
    if num==0:
        streak=0
    else:
        streak+=1
    print(num, "->", streak)
print()
#Part 2 Best Streak tracker
best=0
streak=0
for n in binary:
    if n==0:
        streak=0
    else:
        streak+=1
        if streak>best:
            best=streak
print("List:", binary)
print("Best streak:", best)
print()
#Part 3 Same Direction Two pointers
numbers=[1,0,4,0,0,3,6,7,23,0,0,3,6,7,3,447,3934672390]
print("Before:", numbers)
zero=0
for nonzero in range(len(numbers)):
    if numbers[nonzero]!=0:
        numbers[nonzero], numbers[zero]=numbers[zero], numbers[nonzero]
        zero+=1
print("After:", numbers)
print()
#Pointer Reserve
print("Pointer stopped at:", zero)
print("Nonzeros at front:", zero)
print("Zeros at end:", len(numbers)-zero)
print()