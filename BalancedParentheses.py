#A recursive function that generates every valid combination n pairs of curly braces
#Rule-if l>r then place } vice versa
def par(s, l, r, p, n):
    if p==2*n:
        for ss in s:
            print(ss, end="")
        print("\n")
        return
    if l>r:
        s[p]="}"
        par(s, l, r+1, p+1, n)
    if l<n:
        s[p]="{"
        par(s, l+1, r, p+1, n)
n=int(input("Enter number of parenthesis: "))
s=[""]*2*n
print("\n")
par(s, 0, 0, 0, n)
