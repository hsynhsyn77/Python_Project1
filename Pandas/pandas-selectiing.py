import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index=["A", "B", "C"], columns=["column1", "column2", "column3"])

result = df
result = df["column1"]
result = type(df["column1"])
result = df[["column1", "column2"]]

# loc["row","column"] =>loc["row"] =>loc[":", "column"]
result = df.loc["A"],
result = type(df.loc["A"])
result = df.iloc[2]
result = df.loc[:, "column1"]
result = df.loc[:, ["column1", "column2"]]
result = df.loc[:, "column1":"column2"]
result = df.loc[:, :"column2"]
result = df.loc["A":"B", :"column2"]
result = df.loc[:"B", :"column2"]
result = df.loc["A", "column2"]
result = df.loc["C", "column1"]
result = df.loc[["A", "B"], ["column1", "column2"]]

df["column4"] = pd.Series(randn(3), ["A", "B", "C"])
df["column5"] = df["column1"] + df["column3"]

result = df.drop("column5", axis=1, inplace=True)

print(result)
print(df)
