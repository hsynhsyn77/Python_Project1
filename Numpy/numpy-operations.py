import numpy as np

number1 = np.random.randint(10, 100, 6)
number2 = np.random.randint(10, 100, 6)

print(number1)
# print(number2)

result = number1 + number2
result = number1 + 10
result = number1 - number2
result = number1 - 10
result = number1 * number2
result = number1 * 10
result = number1 / number2
result = number1 / 10

result = np.sin(number1)
result = np.cos(number1)
result = np.sqrt(number1)
"""karakök"""
result = np.log(number1)
"""logoritma"""

mnumbers1 = number1.reshape(2, 3)
mnumbers2 = number1.reshape(2, 3)

# print(mnumbers1)
# print(mnumbers2)

result = np.vstack((mnumbers1, mnumbers2))
result = np.hstack((mnumbers1, mnumbers2))

result = number1 >= 50
""" her bir elemanlar 5 den büyük ler mi kontrol eder"""

result = number1 % 2 == 0
"""çiftmi tek mi"""
print(number1[result])
"""hangileri çift gösterir"""

print(result)
