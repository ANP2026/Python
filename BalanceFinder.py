#Slices and their sums
arr=[-4,6,2,0,0,0,1,1]
print("Full array:", arr)
print("Left of Index 2:", arr[:2])
print("Right of Index 2:", arr[3:])
print("Left Sum of Index 2:", sum(arr[:2]))
print("Right Sum of Index 2:", sum(arr[3:]))
#Balance at every index
print("Balance check")
for i in range(len(arr)):
    l=sum(arr[:i])
    r=sum(arr[i+1:])
    print("Index:", i, "->", "Left:", l ,"Right:", r)
#Equilibrium point
for j in range(len(arr)):
    if sum(arr[:j]) == sum(arr[j+1:]):
        print("Index:", j, "Elements:", arr[j])
#Growing sub array window
number=[3,6,2,2,56,1,0,9]
target=10
print("Growing sub array window start=1 target:", target)
curr=0
for k in range(1, len(number)):
    curr+=number[k]
    print("Number[1] to ",k,"=", number[1:k+1], "Sum=", curr)
    if curr>=target:
        break
#Find sub array with target sum
print("Searching all windows")
found=False
for f in range(len(number)):
    if found:
        break
    curr=0
    for d in range(f, len(number)):
        curr+=number[d]
        if curr==target:
            print("Found Indexes", f, "to", d, ":", number[f:d+1])
            found=True
            break
        if curr>target:
            break
if not found:
    print("No Sub array found")
