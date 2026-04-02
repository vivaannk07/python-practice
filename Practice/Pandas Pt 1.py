import pandas as pd
data = {
    "Name": ["A", "B", "C"],
    "Age": [25, 30, 35],
    "Marks":[80,90,70]
}
df = pd.DataFrame(data)

print("Full data ")
print(df)

print("\nFirst two rows: ")
print(df.head(2))

print("\nLast two rows: ")
print(df.tail(2))

print("\nName Column: ")
print(df["Name"])

print("\nMarks Column:")
print(df["Marks"])

df["Grade"] = df["Marks"].apply(lambda x:"A" if x> 85 else"B")

print("\nAfter Adding Grade: ")
print(df)

print("\nShape:", df.shape)
print("Columns:", df.columns)
print("Data types:\n", df.dtypes)

print("\nMarks> 75:")
print(df[df["Marks"] > 75])

print("\nSorted ascending: ")
print(df.sort_values("Marks"))

print("\nSorted descending: ")
print(df.sort_values("Marks", ascending=False))

df.loc[df["Name"]=="A", "Marks"] = 95
print("\nAfter updating Marks for A:")
print(df)

df = df.drop("Marks", axis=1)
print("\nAfter dropping Marks column:")
print(df)