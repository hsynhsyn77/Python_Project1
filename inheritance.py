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
print(ali.Adress)
