import array as arr
a=arr.array("i", [1, 4, 5, 2, 5, 8, 5, 2, 6, 8])
import statistics
mean=statistics.mean(a)
median=statistics.median(a)
print("Mean of", a, "is", mean)
print("Median of", a, "is", median)