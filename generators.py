#def cube():
#    for i in range(10):  # kaç haneli liste yapacak onu yazarız.
#        yield i ** 3
#
#
#for i in cube():
#    print(i)

generator=[i**3 for i in range(5)]
print(generator)

for i in generator:
    print(i)

