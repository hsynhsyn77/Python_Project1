import pandas as pd
import numpy as np

# data
numbers = [20, 30, 40, 50]
letters = ["a", "b", "c", "d", 20]
scalar = 5
dict = {"a": 10, "b": 20, "c": 30, "d": 40}
random_numbers = np.random.randint(10, 100, 6)

# pandas_series = pd.Series()
# pandas_series1 = pd.Series(numbers)
# pandas_series2 = pd.Series(letters)
# pandas_series3 = pd.Series(5, [0, 1, 2, 3])
# pandas_series1 = pd.Series(numbers, ["a", "b", "c", "d"])
# pandas_series4 = pd.Series(dict)
# pandas_series5 = pd.Series(random_numbers)

pandas_series1 = pd.Series([20, 30, 40, 51], ["a", "b", "c", "d"])

# result = pandas_series1[0]
# result = pandas_series1[-1]
# result = pandas_series1[:2]
# result = pandas_series1[-2:]  # 40,50
# result = pandas_series1["a"]  # 20
# result = pandas_series1["d"]  # 50
# result = pandas_series1[['a', 'c']]
result = pandas_series1.ndim
result = pandas_series1.dtype
result = pandas_series1.shape
result = pandas_series1.sum()
result = pandas_series1.max()
result = pandas_series1.min()
result = pandas_series1 + pandas_series1
result = pandas_series1 + 50
result = np.sqrt(pandas_series1)

result = pandas_series1 >= 50
result = pandas_series1 % 2 == 0

# print(pandas_series1)
# print(pandas_series2)
# print(pandas_series3)
# print(pandas_series4)
# print(pandas_series5)
# print(pandas_series1)
# print(result)
# print(pandas_series1[pandas_series1 % 2 == 0])

hyundai2013 = pd.Series([20, 30, 40, 10], ["i30", "sonata", "i20","tucson"])
hyundai2012 = pd.Series([40, 30, 20, 10], ["i30", "sonata", "ix35","i10"])

total = hyundai2013 + hyundai2012
print(total["ix35"])
print(total["i30"])

