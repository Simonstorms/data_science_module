import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv('admission_data.csv')

# df2 = df[df["Major"] != "Other"].copy()
df2.loc[:, "acc"] = df2["Admission"].replace({"Accepted": "1", "Rejected": "0"}).astype(int)


# print(df2.groupby("Major")["acc"].mean()*100)
s = df2.groupby(["Major","Gender"])["acc"].mean().unstack().plot.bar()
print(s)
plt.show()

