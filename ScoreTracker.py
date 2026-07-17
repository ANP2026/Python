names = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
scores = [90, 75, 88, 62, 95]
n=len(scores)
print("======= Score Tracker(n=",n," players)======")
for i in range(n):
    print(i+1, ".", names[i], ":", scores[i], sep="")
print()
steps = 1
print("Score at index 0:", scores[0], "Steps =", steps, "Theta(1)-Tight bound")
print()

target = "Aarav"
steps = 0
for name in names:
    steps +=1
    if name == target:
        break
print("Search for", target, "steps =", steps, "Omega(1)-Best case, lower bound")
target = "Kabir"
steps = 0
for name in names:
    steps +=1
    if name == target:
        break
print("Search for", target, "steps =", steps, "O(n)=", n, "Worst case, upper bound")
print()

steps = 0
targetsum=150
print("Pairs with total score = ", targetsum, ":")
for i in range(n):
    for j in range(i+1, n):
        steps +=1
        if scores[i] + scores[j] == targetsum:
            print(" ", names[i], "+", names[j], "=", scores[i] + scores[j])
print("Total Comparison:", steps, "0(n**2)-Drop constant, Keep n**2,")
print()
print("Asymptotic Summary")
print("Theta(1): Index access- always one step tight bound")
print("Omega(1) best case-found in one step lower bound")
print("O(n): worst case- found after n=", n, "steps, upper bound")
print("O(n**2): pair check-n*(n-1)/2=", n*(n-1)//2, "comparisons")
print()
print("Drop constants. Keep the dominant term, that is asymptotic analysis")

