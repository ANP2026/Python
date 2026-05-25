def sample_factorial(n):
    if n==1:
        return n
    else: 
        return n*sample_factorial(n-1)

num = int(input("Enter a number: "))
if num < 0:
    print("You can't factorial a negative number!")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {sample_factorial(num)}")