def linear(n):
    if n==0:
        return
    print(n, end=" ")
    linear(n-1)
print("Linear Recursion")
linear(5)
print()
def tail(n):
    if n==0:
        return
    print(n, end=" ")
    tail(n-1)
print("Tail Recursion")
tail(5)
print()
def head(n):
    if n==0:
        return
    head(n-1)
    print(n, end=" ")
print("Head Recursion")
head(5)
print()
def in_de(n):
    if n==0:
        return
    print(n, end=" ")
    in_de(n-1)
    print(n, end=" ")
print("Increasing Decreasing Recursion")
in_de(4)
print()
def tree(n):
    if n==0:
        return
    print(n, end=" ")
    tree(n-1)
    tree(n-1)
print("Tree recursion")
tree(3)
print()
print("Label calls doubles every time")