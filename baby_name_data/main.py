import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('yob/yob2021.txt', names=['Name', 'Gender', 'Quantity'], header=None)

# print("First ten rows: \n ", df.head(10))

# print("Number of rows and columns: \n ", df.shape)

# print("total number of babies: \n ", df["Name"].count())

# print("Total number of male babies:", (df["Gender"] == "M").sum(),
# "\nTotal number of female babies:", (df["Gender"] == "F").sum())

# print("Is my Name 'Simon' in the data:", (df["Name"] == "Simon").any())

# print(f"Percentage of Women: {((df["Gender"] == "F").sum() / df["Name"].count()) * 100:.2f}%",

# "Percentage of Man: {((df["Gender"] == "M").sum() / df["Name"].count()) * 100:.2f}%")

# print("top 5 girls names and top 5 boys names: \n", pd.concat([
#     df[df["Gender"] == "F"].head(5)["Name"],
#     df[df["Gender"] == "M"].head(5)["Name"]
# ]).reset_index(drop=True)
# )

# pd.concat([
#     df[df["Gender"] == "F"].head(5)["Name"],
#     df[df["Gender"] == "M"].head(5)["Name"]
# ]).reset_index(drop=True).to_excel("yob2021_excel.xlsx")

