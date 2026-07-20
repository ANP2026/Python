scores = [12,25,33,41,50,67,72,85,91,98]
n = len(scores)
target = 98
print("======= Quiz Score Finder =======")
print("Scores:", scores, "Target", target)
print()
#linear search
steps=0
for i in range(n):
    steps+=1
    if scores[i] == target:
        print("Linear search: Index =", i, "Steps =", steps, "O(n)")
        break
print()
#binary search
low = 0
high = n-1
steps=0
while low <= high:
    mid = (low+high) // 2
    steps+=1
    if scores[mid] == target:
        print("Binary search: Index =", mid, "Steps =", steps, "O(log n)")
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print()
#recursion
def binary_search_recursive(scores, low, high, target, calls=0):
    calls += 1
    if low > high:
        return -1, calls
    mid = (low + high) // 2
    if scores[mid] == target:
        return mid, calls
    elif scores[mid] < target:
        return binary_search_recursive(scores, mid + 1, high, target, calls)
    else:
        return binary_search_recursive(scores, low, mid - 1, target, calls)
result, calls = binary_search_recursive(scores, 0, n - 1, target)
print("Recursive search: Index =", result, "Calls =", calls, "O(log n)")
print()

print("======== Space Complexity ==========")
print("O(1): constant, 1 step - Never grows")
print("O(log n): ", steps, "steps halving, grows slowly")
print("O(n)", n, "steps - linear, grows with n")
print("O(n^2): ", n*n, "steps quadratic - grows fast")