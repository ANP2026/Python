def find_gcd(a, b):
    """Find the Greatest Common Divisor of two numbers"""
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """Find the Least Common Multiple of two numbers"""
    lcm = (a * b) // find_gcd(a, b)
    return lcm

# Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display LCM
result = find_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {result}")
