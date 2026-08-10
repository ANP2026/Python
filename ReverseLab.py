print("==========REVERSE LAB=========")
print()
#Digit Scanner
n=int(input("Enter a number:"))
temp=n
while temp>0:
    print("Last digit:" ,temp%10, "| remaining:", temp//10)
    temp=temp//10
print()
#Number Flipper
def flipnum(num):
    if num//10==0:
        return num
    last=num%10
    rest=flipnum(num//10)
    return last*pow(10, len(str(rest))) + rest
n2=int(input("Enter a number to be flipped: "))
print(n2, "flipped= ", flipnum(n2))
print()
#Name Flipper
def flipper(s):
    if len(s)==1:
        return s
    return flipper(s[1:])+s[0]
name=input("Enter your name")
print(name, "flipped = ", flipper(name))
print()
#pow4?
def ispow4(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%4==0:
        return ispow4(n//4)
    return False
print("16 ->", ispow4(16), "12 ->", ispow4(12))
guess=int(input("Guess your own number"))
print(guess, "->", ispow4(guess))
