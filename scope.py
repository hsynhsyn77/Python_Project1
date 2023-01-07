# global scope
x = "global x"

def function():
    # local scope
    # x = "local x"
    print(x)

function()
print(x)

##############################

# global name
name="Çınar"
def chamgeName(new_name):
    # local name
    global name
    name=new_name
    print(name)

chamgeName("ada")

print(name)

##############################

name="global string"

def greeting():
    name="Çınar"

    def hello():
        name="ada"
        print("hello "+name)
    hello()

greeting()

#############################

x=50
def test():
    global x
    print(f"x : {x}")
    x=100
    print(f"change x to {x}")

test()
print(x)