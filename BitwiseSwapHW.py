a=72
b=2
print("Before swap:a=", a, "b=",b)
a=a+b
b=a-b
a=a-b
print("After swap:a=", a, "b=",b)
a=72
b=2
print()
print("Before XOR swap:a=", a, "b=",b)
a^=b
b^=a
a^=b
print("After XOR swap:a=", a, "b=",b)
print("Left Shift:")
print("8<<1=", 8<<1)
print("8<<2=", 8<<2)
print("8<<3=", 8<<3)
print("8<<4=", 8<<4)
print("8<<5=", 8<<5)
print("8<<6=", 8<<6)
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
print("24/3=", divide(24,3))
print("144/12=", divide(144,12))
print("-24/2=", divide(-24,2))
print("12/-6=", divide(12,-6))