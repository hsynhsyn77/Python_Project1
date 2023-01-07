"""
class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""


class DataScience(Employees):
    def __init__(self):
        self.Programming = ""


veribilimci1 = DataScience()


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""


mar1 = Marketing()


class Employees_Yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Adress = Adress


ali = Employees_Yeni("g","b","c")
print(ali.FirstName)
print(ali.LastName)
print(ali.Adress) """


# inheritance (kalıtım)
# Person => name, lastname,  age, eat(), run(), drink
# student (person), teacher (person)
# Animal => Dog(Animal), Cat(Animal)
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am a eating")


class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")
    # override
    def who_am_i(self):
        print("I am a student")
    def sayHello(self):
        print("Hello I am a student")
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1 = Person("kaan gökhan", "şirikçi")
s1 = Student("simay elif", "şirikçi", 1234)
t1 = Teacher("hüseyin", "şirikçi", "Python")

t1.who_am_i()

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
s1.eat()
p1.eat()
s1.sayHello()
