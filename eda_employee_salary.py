import pandas as pd
df = pd.read_csv("employee_salary.csv")


df.to_csv("employee_salary.csv", index=False)
df = pd.read_csv("employee_salary.csv")
print("First 5 Records")
print(df.head())
print("\nLast 5 Records")
print(df.tail())
print("\nDataset Shape")
print(df.shape)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])


print("Column Names")
print(df.columns)
print("\nData Types")
print(df.dtypes)
print("\nDataset Information")
df.info()
print("\nDescriptive Statistics")
print(df.describe())


df.loc[2, "Salary"] = None
df.loc[5, "Age"] = None
print("Missing Values")
print(df.isnull().sum())
print("\nPercentage of Missing Values")
print((df.isnull().sum() / len(df)) * 100)
print("\nColumn with Highest Missing Values")
print(df.isnull().sum().idxmax())
print("\nDataset Size Before Cleaning:", df.shape)
df = df.dropna()
print("Dataset Size After Cleaning:", df.shape)