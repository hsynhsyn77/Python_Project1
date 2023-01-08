import random

# result=dir(random)
# result=help(random)

result = random.random()  # 0.0 ile 1.0 arasında
result = random.random() * 100  # 0.0 ile 1.0 arasında
result = random.uniform(10, 100)
result = random.randint(1, 100)

greeting = "hello there"
names = ["kaan", "gökhan", "simay", "binnur", "hüseyin"]
# result=names[random.randint(0,len(names)-1)]

result = random.choices(names)
result = random.choices(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2)

print(result)
