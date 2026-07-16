n=4
print("****Counting Game Points****")
print()
total = n*(n+1)/2
print("Formula way: total points", total, "Steps :1")

total = 0
steps = 0
for round_number in range(1, n+1):
    total += round_number
    steps += 1
print("Loop way: total", total, "Steps :", steps)

total = 0
steps = 0
for round_number in range(1, n+1):
    for point in range(1, round_number+1):
        total+=1
        steps+=1
print("Nested loop: total", total, "Steps :", steps)

n=10
nested_steps = 0
for round_number in range(1, n+1):
    for point in range(1, round_number+1):
        nested_steps+=1
print("Same answer but very different cost. This is time complexity")