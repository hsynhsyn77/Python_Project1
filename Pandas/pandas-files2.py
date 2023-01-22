import sqlite3

import pandas as pd

df=pd.read_csv("all_seasons.csv")
# df=pd.read_json("sample.json")
# df=pd.read_excel("sample.xlsx")

# connection=sqlite3.Connection("sampla.db")
# df=pd.read_sql_query("SELECT * FROM students",connection)

print(df)