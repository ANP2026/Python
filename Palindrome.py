user_input = input("Enter a number: ")

try:
    num = int(user_input)
except ValueError:
    print("Please enter a valid integer.")
else:
    if num < 0:
        print("Negative numbers are not considered palindrome numbers.")
    else:
        temp = num
        reversed_num = 0

        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        if reversed_num == num:
            print("This is a palindrome number")
        else:
            print("This isn't a palindrome number")
