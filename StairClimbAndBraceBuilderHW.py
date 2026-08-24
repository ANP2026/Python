def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twosteps=0
    if stairs>=2:
        twosteps=ways(stairs-2)
    onestep=ways(stairs-1)
    return twosteps+onestep
stairs=int(input("Enter number of stairs: "))
print("Number of ways to climb", ways(stairs))

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
n=int(input("Enter number of parenthesis combinations: "))
s=[""]*2*n
par(s, 0, 0, 0, n)
