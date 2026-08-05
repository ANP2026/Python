print("====DREAM RECURSION LAB====")
print("2 rules of Recursion")
print("1. Call yourself with a smaller problem each time")
print("2. Have a base case to stops the calls")
print()
def countup(n):
    if n > 10:
        return
    print(n, end=" ")
    countup(n + 1)
print("Couting 1-10 using recursion", countup(1))
def countdown(n):
    if n<1:
        return
    print(n, end=" ")
    countdown(n-1)
print("Counting down from n using recursion", countdown(10))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print("Factorial using recursion", factorial(5))
import sys
print("Python recursion limit", sys.getrecursionlimit(), "calls")
def nobasecase(n):
    print("Call", n, end=" ")
    nobasecase(n+1)
sys.setrecursionlimit(30)
try:
    nobasecase(1)
except RecursionError:
    print("Recursion error: Stack overflow no base case")