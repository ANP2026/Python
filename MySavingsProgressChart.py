import matplotlib.pyplot as plt
days=["M", "T", "W", "TH", "F"]
prices=[70,85,69,90,75]
plt.plot(days, prices)
plt.show()
plt.plot(days, prices)
plt.title("My Savings PRogress Chart")
plt.xlabel("Days of the week")
plt.ylabel("MONEy")
plt.show()
plt.bar(days, prices, color="orange")
plt.show()