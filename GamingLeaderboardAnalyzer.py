import pandas as pd
print("Part 1: Panda Series")
scores=[98500,87200,76400,65100,54800]
players=pd.Series(scores, index=["Nightwolf", "StarBlaze", "PixelKing", "CyberFox", "IronStorm"])
print(players)
print()
print("Part 2: Pandas data frame")
data={
    "Player": ["Nightwolf", "StarBlaze", "PixelKing", "CyberFox", "IronStorm"],
    "Level": [42,38,35,30,27],
    "Score": [98500,87200,76400,65100,54800],
    "Wins": [210,185,162,140,118]}
df=pd.DataFrame(data)
print(df)
print("Row 0, top player:", df.loc[0])
print("Row 2&3", df.loc[2:3])
dataset=pd.read_csv("leaderboard.csv")
print("First five rows", dataset.head())
print("Last 3 rows", dataset.tail(3))
print()
print("Data set info", dataset.info())