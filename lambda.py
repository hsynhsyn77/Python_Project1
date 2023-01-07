#def squre(numb):return numb**3
squre=lambda num:num**2

numbers = [1, 3, 5, 9,10,4,8]
#result = list(map(lambda num: num ** 2, numbers))
#result=list(map(squre, numbers))
result=squre(3)
#for item in map(squre, numbers):
#    print(item)
print(result)
result=list(map(lambda num:num**2,numbers))
print(result)

def check_even(num):return  num%2==0
# veya 1 yazarsak tekler döner
result1=list(filter(check_even,numbers))
#check_even=lambda num:num%2==0
result2=list(filter(lambda  num:num%2==1,numbers))

result3=check_even(numbers[2])

print(result1)
print(result2)
print(result3)
