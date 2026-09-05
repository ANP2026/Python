import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("IMDB")
print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.describe(include="all"))
print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

df.select_dtypes(include=[np.number]).hist(figsize=(12, 8))
plt.show()
df.select_dtypes(include=[np.number]).plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False, figsize=(8, 8))
plt.show()
sns.countplot(data=df, x="Certificate")
plt.show()
sns.countplot(data=df, x="Genre")
plt.show()
sns.countplot(data=df, x="Director")
plt.show()
sns.countplot(data=df, x="Certificate", hue="Genre")
plt.show()
sns.countplot(data=df, x="Genre", hue="Certificate")
plt.show()
sns.countplot(data=df, x="Certificate", hue="Director")
plt.show()
