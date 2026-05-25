n = int(input("Enter the amount of numbers from the fibbonacci sequence you want to see: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a+b 
    a = b 
    b = c
