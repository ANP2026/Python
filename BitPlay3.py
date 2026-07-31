a=56
b=12

print("Before a=", a)
print("Before b=", b)
a=a+b
b=a-b
a=a-b
print("\nAfter a=",a)
print("After b=",b)

a=56
b=12
print()
print("Before XOR swap:a=", a, "b=",b)
a^=b
b^=a
a^=b
print("After XOR swap:a=", a, "b=",b)

print("\nLeft Shift:")
print("3<<1=", 3<<1)
print("3<<2=", 3<<2)
print("3<<3=", 3<<3)
print("3<<4=", 3<<4)
print("3<<5=", 3<<5)
print("3<<6=", 3<<6)

def divide(a, b):
    negative=(a<0)^(b<0)
    a=abs(a)
    b=abs(b)
    count=0
    while a>=b:
        a-=b
        count+=1
    if negative:
        count = -count
    return count
print("Divide without /")
print("50/2=", divide(50,2))
print("72/3=", divide(72,3))
print("-50/2=", divide(-50,2))
print("50/-2=", divide(50,-2))