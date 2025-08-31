import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 95, 100],
}
df = pd.DataFrame(data)

# Look at the first few rows
# print(df.head())

# Shape of data (rows, columns)
# print(df.shape)

# Info about columns and types
# print(df.info())

# Basic statistics (mean, std, min, max)
# print(df.describe())


# Single column (returns a Series)
# print(df["Age"])

# Multiple columns (returns a DataFrame)
# print(df[["Name", "Score"]])

# First row by label
df.loc[0]

# First row by index
df.iloc[0]

# Specific row & column
df.loc[0, "Name"]     # "Alice"
df.iloc[0, 1]         # 25

# print(df.loc[0:2,"Score"])
# People older than 30
df[df["Age"] > 30]

# People with Score >= 90
df[df["Score"] >= 90]

# Combine conditions with & (AND), | (OR)
df[(df["Age"] > 25) & (df["Score"] >= 90)]

# print(df[(df["Age"]<30) | (df["Score"]==100)])

data1 = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Age": [25, None, 35, 40, None],
    "Score": [85, 90, None, 100, 95],
}

df1=pd.DataFrame(data1)
# print(df1.isna()) # true false table
# print(df1.isna().sum())

# drop missing data

# print(df1)
# print(df1.dropna(subset="Score")) it removes the row with null value in Score

# print(df1.dropna())


# print(df1.fillna(0))
# print(df1["Score"].fillna(0))
# print(df1["Score"].fillna(df1["Score"].mean()))

df1["Age_after_10_yrs"]= df["Age"]+10


# apply

def grade(score):
    if(score>90):
       return "A"
    else:
        return "B"

df1["Grade"] = df1["Score"].apply(grade)
df1["Name_Length"] = df1["Name"].apply(lambda x:len(x))
# print(df1["Age"].fillna(1,inplace=True))

# this cuts age into groups of 1 to 10 , 11 to 20 , and 21 to 60
df1["Age_Group"] = pd.cut(df1["Age"],bins=[0,10,20,60],labels=["kid","young","Old"])
print(df1)