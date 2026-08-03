items=["A", "B", "C"]
n=len(items)
total=2**n
print("=====POWER MAP=====")
print("Items:", items)
print("Elements:", n, "=", total)
print("")

print("Mask Table (n=", n, "):")
mask=0
while mask<total:
    bit2=(mask>>2)&1
    bit1=(mask>>1)&1
    bit0=mask&1
    print("Mask:", mask, "-> [C][B][A]=", bit2, bit1, bit0)
    mask+=1
print()

print("All Subsets bit probe")
mask=0
while mask<total:
    subset=[]
    j=0
    while j<n:
        probe=1<<j
        if (mask&probe)>0:
            subset.append(items[j])
        j+=1
    print("Mask:", mask, "->", subset)
    mask+=1
print()

def bitdiff(a,b):
    flips=0
    while a>0 or b>0:
        lasta=a&1
        lastb=b&1
        if lasta!=lastb:
            flips+=1
        a>>=1
        b>>=1
    return flips
print("Bit Difference Table")
print("Difference(12,15)", bitdiff(12,15), "(12=1100, 15=1111)")
print("Difference(21, 24)", bitdiff(21,24), "(21=10101, 24=11000)")
print("Difference(8, 8)", bitdiff(8,8), "(8=1000, 8=1000)")
