import pandas as pd
import openpyxl

# creating a dataframe

df = pd.DataFrame({
    "name":["p1","p2"],
    "age":[22,22],
    "year":[2003,2003]
})

# print(df)
# print(df["name"])
# print(df.describe()) # it provides quick overview of numerical values in a dataframe

df1= pd.DataFrame([
    {"name":"p1", "age":22},
    {"name":"p2","age":22}
])

# print(df)
# print(df1["age"])

s = pd.Series([20,21,22],name="Age")
s1 = pd.Series(["person1","person2"],name="Name")
# print(s)
# print(s1)

data={
    "Animals":["Cat","Dog","goat","rabbit","Lion","tiger"],
    "Eats Flesh":["yes","yes","no","no","yes","yes"],
    "Age":[1,None,3,4,5,None]
}

df2 = pd.DataFrame(data)
# print(df2)

# df2.to_csv("./data2.csv")

t2 = pd.read_csv("./data.csv")
# print(t2["Fare"])

# t2.to_excel("exceldata.xlsx",sheet_name="titanic", index=False)

# t3 = pd.read_excel("./exceldata.xlsx")
# print(t3)

t4 = pd.read_csv("./data2.csv")
t4.to_excel("exceldata.xlsx",sheet_name="animals",index=False)

t5 = pd.read_excel("exceldata.xlsx")
# print(t5.info())

# print(t5["Animals"].shape)

#selecting only required series
animalage = df2[["Age","Animals"]]
# print(animalage)

age3 = df2[df2["Age"]>3]
# print(age3)

age24 = df2[df2["Age"].isin([2,4])]
age35 = df2[(df2["Age"] == 3) | (df2["Age"] ==5)]
# print(age35)

# not null
notnull = df2[df2["Age"].notna()]
# print(notnull)

aName = df2.loc[df2["Age"]>3 ,"Animals"]
# print(aName)

# using index

aName1 = df2.iloc[1:4]
# print(aName1)

print(df2.loc[df2["Eats Flesh"]=="yes","Animals"])