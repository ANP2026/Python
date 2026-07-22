smallest = int(input("Enter the smallest number: "))
largest  = int(input("Enter the largest number:"))

while(smallest):
    temp=smallest
    smallest = largest%smallest
    largest = temp

print("GCF is", largest)