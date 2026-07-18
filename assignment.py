import pandas as pd
df = pd.read_csv('bcancer.csv')

print("First five rows of the dataset:")
print(df.head())

print("Last five rows of the dataset:")
print(df.tail())

print("\nList of columns:  ", df.shape)
print(df.shape[0])
print(df.shape[1])

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))

print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

print("\nRandom Sample:")
print(df.sample(3))

print("\nAfter Dropping Missing Values:")
print(df.dropna())

print("\nMethods and Attributes:")
print(dir(df))