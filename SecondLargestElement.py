import array as arr
def sec(a, asize):
    largest=secondlargest=-2147483648
    for i in range(asize):
        if (a[i]>largest):
            secondlargest=largest
            largest=a[i]
        elif (a[i]>secondlargest and a[i]!=largest):
            secondlargest=a[i]
    print("Second largest is", secondlargest)
a=[12,832,5574,443,77,268,373,4,73,83,4,7,3]
asize=len(a)
sec(a, asize)
