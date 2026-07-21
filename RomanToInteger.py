def romantointeger(romanint):
    romandict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    result=0
    for i in range(0, len(roman)-1):
        if romandict[romanint[i]] < romandict[romanint[i+1]]:
            result = result - romandict[romanint[i]]
        else:
            result = result + romandict[romanint[i]]
    return result + romandict[romanint[-1]]
roman=input("Input any Roman Numeral:")
print("The integer equivalent of", roman, "is", romantointeger(roman))