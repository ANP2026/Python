
#Two pointer swap
scores=[10,20,30,40,50]
start=0
end=len(scores)-1
while start<end:
    scores[start], scores[end]=scores[end], scores[start]
    start+=1
    end-=1
print("Swapped", scores)
print()
#Reversing Groups
scores=[1,2,3,4,5,6,7,8]
n=3
i=0
while i<len(scores):
    start,end=i,min(i+(n-1), len(scores)-1)
    while start<end:
        scores[start], scores[end]=scores[end], scores[start]
        start+=1
        end-=1
    i+=n
print("Reversed in group of 3", scores)
print()
#Left rotate by n
scores=[10,20,30,40,50]
for _ in range(2):
    temp=scores[0]
    for i in range(1, len(scores)):
        scores[i-1]=scores[i]
    scores[-1]=temp
print("Rotated left by 2", scores)
print()
#leaders of array
scores=[16,27,4,3,5,2]
maxright=scores[-1]
leaders=[maxright]
for i in range(len(scores)-2, -1, -1):
    if scores[i]>maxright:
        maxright=scores[i]
        leaders.append(scores[i])
leaders.reverse()
print("Score: ", scores)
print("Leaders:", leaders)