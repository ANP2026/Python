#Part 1 stock buy sell
prices=[100,180,260,310,40,535,695]
profit=0
for days in range(1, len(prices)):
    if prices[days]>prices[days-1]:
        profit+=prices[days]-prices[days-1]
print("Stock prices:", prices)
print("Max profit:", profit)
print()
#Part 2 rainwater thing
heights=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(heights)
left_tallest=[0]*n
left_tallest[0]=heights[0]
for i in range(1, n):
    left_tallest[i]=max(left_tallest[i-1], heights[i])
print("Heights:", heights)
print("Left tallest:", left_tallest)
print()
#right tallest path
right_tallest=[0]*n
right_tallest[n-1]=heights[n-1]
for i in range(n-2, -1,-1):
    right_tallest[i]=max(right_tallest[i+1], heights[i])
print("Right tallest:", right_tallest)
print()
#PARt 4 rainwater trpa
water=0
for i in range(n):
    water+=min(left_tallest[i], right_tallest[i]-heights[i])
print("Total water trapped:", water)
