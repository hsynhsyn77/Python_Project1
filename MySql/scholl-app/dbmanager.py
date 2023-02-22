import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher


class DbManager:
    def __init__(self):
        self.connnection = connection
        self.cursor = self.connnection.cursor()

    def getStudentById(self, id):
        sql = "select * from Student where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:", err)


    def getStudentByclassId(self, classid):
        sql = "select * from Student where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender,self.classid)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)


    def editStudent(self, student: Student):
        pass

    def addTeacher(self, Teacher: Teacher):
        pass

    def editTeacher(self, Teacher: Teacher):
        pass


db = DbManager()

#student = db.getStudentById(7)
#print(student[0].name)
#print(student[0].surname)

students = db.getStudentByclassId(1)
print(students[0].name)
print(students[0].name)

