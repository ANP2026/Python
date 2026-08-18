binary=[1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1]
streak=0
for i in binary:
    if i==0:
        streak=0
    else:
        streak+=1
    print(i, "->", streak)
streak=0
best=0
for j in binary:
    if j==0:
        streak=0
    else:
        streak+=1
        if streak>best:
            best=streak
print("Best streak:", best)
numbers=[1,0,23,0,43,60,2,0,0,3,346,0,26]
zero=0
for nonzero in range(len(numbers)):
    if numbers[nonzero] != 0:
        numbers[nonzero], numbers[zero] = numbers[zero], numbers[nonzero]
        zero += 1
