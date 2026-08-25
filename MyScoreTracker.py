import matplotlib.pyplot as plt
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
scores=[70,85,60,90,75]
plt.plot(days, scores)
plt.show()
plt.plot(days, scores)
plt.title("My Quiz ScoreTracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0,100)
plt.show()
plt.bar(days, scores, color="orange")
plt.title("My Quiz ScoreTracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.ylim(0,100)
plt.show()