a, b=7, 7

print("====ODD HUNT====")
print("a^a = ", a^a)
print("a^0 = ", a^0)
print("Equal(a^b) = ", a^b==0)

arr = [3, 5, 3, 5, 9]
result = 0
for n in arr:
    result^=n
print("XOR of array=",result, "->", bin(result)[2:])

print("One-odd cancellation")
num=[3,5,3,5,9,9,7]
res=0
for i in num:
    res^=i
print("XOR of one-odd occuring=", res, "->", bin(res)[2:])

print("Two-odd cancellation")
number=[3,5,3,5,9,9,7,7,5,11]
r=0
for j in number:
    r^=j
print("XOR of two-odd occuring=", r,"->" ,bin(r)[2:])

setbit=r&-r
x,y=0,0
for n in number:
    if n&setbit:
        x^=n
    else:
        y^=n
print("two-odd occuring=", x, y)






















