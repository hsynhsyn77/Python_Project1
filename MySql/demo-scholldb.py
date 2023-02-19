# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id,StudentNumber,Name,Surname,Birthdate,Gender
import datetime

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.


import mysql.connector
from datetime import datetime
from connection import connection  # connection dosyasından alıyor bağlantıyı


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudent(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.connection.close()



#ahmet = Student("202", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E")
#ahmet.saveStudent()

ogrenciler = [
    ("401", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
    ("402", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("403", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("504", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
    ("605", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("706", "Ali", "Cenk", datetime(2003, 8, 25), "E")
 ]

Student.saveStudent(ogrenciler)