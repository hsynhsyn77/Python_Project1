import os
import datetime

#result=dir(os)


result=os.name
result=os.getcwd() #bu paketin hangi dosyada olduğunu gösterir
# klasör oluşturma
# os.mkdir("newdirectory")
# os.rename(......) # oluşturduğumuz dosynın adını değiştir
# os.chdir(....) oluşturduğumuz klasörün yerini değiştiririz

# os.mkdirs(....) klasör içine klasör oluşturma
"""
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
"""

#result=os.stat("_date_.py")
#result=result.st_size/1244
#result=datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarih
#result=datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
#result=datetime.datetime.fromtimestamp(result.st_mtime)  #değiştirilme tarihi

# os.system(.......) # var olan bir dosyayı açabiiriz


# path

# result=os.path.abspath("_os_Module.py")# dosyanın konumunu alırız
result=os.path.dirname(os.path.abspath("arguments.py"))
result=os.path.exists("arguments.py")

print(result)
