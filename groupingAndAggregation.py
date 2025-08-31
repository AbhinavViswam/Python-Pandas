import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Age": [25, 30, 35, 40, 28],
    "Score": [85, 90, 95, 100, 78],
    "Gender": ["F", "M", "M", "F", "M"],
}
df = pd.DataFrame(data)
# print(df)

# print("mean:",df["Score"].mean())
# print("Min:",df["Age"].min())
# print("Max:",df["Age"].max())

# print("Groupby")

# print(df.groupby("Gender")["Age"].mean())

# print(df.groupby(["Age","Gender"])["Score"].mean())
# multiple aggregation

# print(df.groupby("Gender")["Score"].agg(["mean","max","max"]))

print("pivot table")
pvot = pd.pivot_table(df,values="Score" ,index="Gender", aggfunc="mean")
# print(pvot)



data1 = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Frank"],
    "Age": [25, 30, 35, 40, 28, 35],
    "Score": [85, 90, 95, 100, 78, 88],
    "Gender": ["F", "M", "M", "F", "M", "M"],
    "Subject": ["Math", "Math", "Science", "Math", "Science", "Science"],
}
df1 = pd.DataFrame(data1)
print(df1)

print(pd.pivot_table(df1,index="Gender" ,values="Score",aggfunc="mean" ))
