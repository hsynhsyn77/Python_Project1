import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["column1", "column2", "column3", "column4", "column5"])

result = df
result = df.columns
result = df.head()
result = df.head(10)
result = df.tail(10)  # son 10 sayı
result = df["column1"].head()  # ilk 5 kayıt gelir
result = df.column1.head()  # ilk 5 kayıt gelir
result = df[["column1", "column2"]].head()  # ilk 5 kayıt gelir
result = df[["column1", "column2"]].tail()
result = df[5:15][["column1", "column2"]].head()
result = df[5:15][["column1", "column2"]].tail()

result1 = df > 50
result2 = df[df > 50]
result3 = df[df % 2 == 0]
result4 = df["column1"] > 50
result5 = df[df["column1"] > 50][["column1", "column2"]]
result6 = df[(df["column1"] > 50) & (df["column2"] <= 70)]
result7 = df[(df["column1"] > 50) | (df["column2"] <= 70)]
result8 = df[(df["column1"] > 50) | (df["column2"] < 50)][["column1", "column2"]]
result9 = df.query(" column2 % 2==0")
result10 = df.query("column1>=50 | column1%2==0")[["column1", "column2"]]

print(result9)
