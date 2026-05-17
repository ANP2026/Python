num = float(input("Enter a number: "))

if num>50:
    print("This number is greater than 50")
    if num%2==0:
        print("And it is even too")
    else:
        print("And it is odd too")
else:
    print("This number is below 50")