def linear(n):
    if n==0:
        return
    print(n, end=" ")
    linear(n-1)
print("\nLinear Recursion")
linear(9)

def tail(n):
    if n==0:
        return
    print(n, end=" ")
    tail(n-1)
print("\nTail Recursion")
tail(4)

def head(n):
    if n==0:
        return
    head(n-1)
    print(n, end=" ")
print("\nHead Recursion")
head(5)

def in_de(n):
    if n==0:
        return
    print(n, end=" ")
    in_de(n-1)
    print(n, end=" ")
print("\nIncreasing Decreasing Recursion")
in_de(17)

def tree(n):
    if n==0:
        return
    print(n, end=" ")
    tree(n-1)
    tree(n-1)
print("\nTree recursion")
tree(3)