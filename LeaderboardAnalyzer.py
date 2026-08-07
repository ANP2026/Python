scores=[340,120,410,120,85,270,190,55]
print("======Head tail pattern======")
print("Scores:", scores)
print("Head:", scores[0])
print("Tail:", scores[1:])
print("Head of Tail:", scores[1:][0])
print("Tail of Tail:", scores[1:][1:])

def show_string(a, depth=0):
    identation=" " * depth
    print(f"{identation}list: {a} -> len={len(a)}")
    if len(a)==1:
        print(f"{identation}Base Case reached only one score left: {a[0]}")
        return
    show_string(a[1:], depth+1)
print("Base case for the list:")
show_string([410,270,190,55])

def is_sorted(a):
    if len(a) <=1:
        return True
    return a[0] <= a[1] and is_sorted(a[1:])
print("Sorted check")
print("Scores=", scores)
print("Is sorted:", is_sorted(scores))

def total_score(a):
    if len(a)==1:
        return a[0]
    return a[0] + total_score(a[1:])
print("sum with recursion")
print("Scores=", scores)
print("Total team score:", total_score(scores))

def top_score(a):
    if len(a)==1:
        return a[0]
    return max(a[0], top_score(a[1:]))
print("Largest element")
print("Scores=", scores)
champion=top_score(scores)
print("Champions score:", champion)
print("Champion index:", scores.index(champion)+1) 