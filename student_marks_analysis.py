import pandas as pd

# Creating student marks data
data = {
    "Name": ["Anu", "Rahul", "Priya", "Kiran", "Megha"],
    "Math": [85, 78, 92, 70, 88],
    "Science": [80, 75, 95, 65, 90],
    "English": [78, 82, 89, 72, 85]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate Total Marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculate Average Marks
df["Average"] = df["Total"] / 3

# Find Topper
topper = df.loc[df["Total"].idxmax()]

print("Student Data:\n")
print(df)

print("\nTopper of the Class:")
print(topper)
