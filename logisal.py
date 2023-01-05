x = 6
hak = 5
devam = "e"
result = 5 < x < 10

"""and"""
result = (x > 5) and (x < 10)  # True , True
result = (hak > 0) and (devam == "e")

"""or"""
result = (x > 0) and (x % 2 == 0)
# True, False => True
# True, True => True
# False, False=< False

"""not"""
result = not (x > 0)

# x,5-10 arasında olan çift sayı  mı

((x > 5) and (x < 5)) and (x % 2 == 0) # iç koşullar

print(result)
