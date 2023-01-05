website = "http://www.huseyinsirikci.com"
course = "Python Kursu: Baştan sona python proglama rehberiniz (40 saat)"

#    1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
lenght = len(website)
#    2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print(result)
#    3-'website içinden com karakterlerini alın.
result = website[26:29]
print(result)
result = website[lenght - 3:lenght]
print(result)
#    4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
print(result)
result = course[:15]
print(result)
result = course[-15:]
print(result)
#    5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print(result)
s = "12345" * 5
print(s[::5])
name, surname, age, job = "bora", "yılmaz", 44, "mühendis"
# 6- yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
result0 = "benim adım " + name + " " + surname + ", yaşım  " + str(age) + " ve mesleğim " + job
print(result0)
result1 = "benim adım {0}  {1}, Yaşım {2} ve mesleğim {3}".format(name, surname, age, job)
print(result1)
result2 = f"benim adım {name}  {surname}, Yaşım {age} ve mesleğim {job}"
print(result2)
# 'benim adım hüseyin şirikçi, Yaşım 44 ve mesleğim mühendis.'
# 7- 'Hello word' ifadesindeki w harfini 'W' ile değiştirn.
s = "hello word"
result = s[6]
print(result)
s = s[0:6] + "W" + s[-4]
s=s.replace("w","W")
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result="abc"*3
print(result)

result=course.count("a")
print(result)
result=course.count("a",0,20)
print(result)


