#phone keypad combinations
#keypad mapping
keypad={
    "2":["a", "b", "c"],
    "3":["d", "e", "f"],
    "4":["g", "h", "i"],
    "5":["j", "k", "l"],
    "6":["m", "n", "o"],
    "7":["p", "q", "r", "s"],
    "8":["t", "u", "v"],
    "9":["w", "x", "y", "z"]
}
def comb(digits, current):
    if len(digits)==0:
        print(current)
        return
    firstdigit=digits[0]
    remaining=digits[1:]
    for letter in keypad[firstdigit]:
        comb(remaining, current+letter)
number=input("Enter digits: ")
print("All combinations\n")
comb(number, "")
count=1
for digit in number:
    count*=len(keypad[digit])
print("Total combination count", count)
