import re

result=dir(re)

# re module

str="Python 2programlama saat yapıyorum"

# re.findall()

result=re.findall("Python",str)

result=len(result)

#re.split()

result=re.split(" ",str)
result=re.split("t",str)
result=re.sub(" \s","-",str)

#re.search()

result=re.search("Python",str)

#result=result.span() # kaçıncı indexde

# result=result.start()
# result=result.end()
#result=result.group()
result=result.string


# regular expression
result=re.findall("[abc]",str)
result=re.findall("[yap]",str)
result=re.findall("[a-e]",str)
result=re.findall("[a-z]",str)
result=re.findall("[0-5]",str)

result=re.findall("[^0-9]",str)

result=re.findall("...",str)
result=re.findall("Py..on",str)

result=re.findall("^p",str)

result=re.findall("p$",str)

result=re.findall("Pyt?on",str)

result=re.findall("a{2}",str)

result=re.findall("a|r",str)

result=re.findall("a|b|cxz",str)

result=re.findall("\APython",str)

result=re.findall("yapıyorum\Z",str)

print(result)