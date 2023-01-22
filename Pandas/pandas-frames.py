import pandas as pd

list = [["Ahmet", 50], ["Ali", 60], ["Kaan", 70], ["Simay", 80]]
dict = {"name": ["Ahmet", "Ali", "Kaan", "Simay"], "Grade": [50, 60, 70, 80]}
dict_list = [
                {"name": "Ahmet", "Grade": 50},
                {"name": "Ali", "Grade": 60},
                {"name": "Kaan", "Grade": 70},
                {"name": "Simay", "Grade": 80}
            ]

# df=pd.DataFrame()
# df=pd.DataFrame([1,2,3,4])
# df=pd.DataFrame(list,index=[1,2,3,4],columns=["name","grade"],dtype=float)
# df=pd.DataFrame(dict)
# df = pd.DataFrame(dict, index=["212", "232", "236", "415"])
# df=pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index=["212", "232", "236", "415"])
print(df)

# s1 = pd.Series([3, 2, 0, 1])
# s2 = pd.Series([0, 3, 7, 2])
#            kolan ismi  kolon ismi
# data = dict(apples=s1,  orange=s2)
#
# df = pd.DataFrame(data)
#
# print(df)
