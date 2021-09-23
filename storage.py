from Models.Teacher import Teacher
from Models.Student import Student
from sqlite3 import *
import sqlite3

class Storage:

    def __init__(self, fileName) -> None:
        self.connection = sqlite3.connect(fileName)
        self.cursor = self.connection.cursor()
        
        try:
            self.__createStudentsTable()
            self.__createTeachersTable()
        except OperationalError as e:
            print(f'Information: {e}')

    def insertStudent(self, student:Student):
        command = f"""
        INSERT INTO 
        students(firstname, lastname, phone, email, birthdate, score) 
        values('{student.firstname}', '{student.lastname}', '{student.phone}', '{student.email}', '{student.birthdate}', {student.score})
        """
        return self.__executeCommand(command, True)

    def insertTeacher(self, teacher:Teacher):
        command = f"""
        INSERT INTO 
        students(firstname, lastname, phone, email, birthdate, subject, degree) 
        values('{teacher.firstname}', '{teacher.lastname}', '{teacher.phone}', '{teacher.email}', '{teacher.birthdate}', '{teacher.subject}', '{teacher.degree}')
        """
        return self.__executeCommand(command, True)
    
    def getAllStudents(self):
        command = """
        SELECT * from students;
        """
        return self.__executeCommand(command)

    def getAllTeachers(self):
        command = """
        SELECT * from teachers;
        """
        return self.__executeCommand(command)

    def search(self, query):
        command = """

        """

    def __createStudentsTable(self):
        command = """
        CREATE TABLE students(
            id char(64) primary key,
            firstname char(255),
            lastname char(255),
            phone char(20),
            email char(255),
            birthdate char(8),
            score integer
        );
        """

        self.cursor.execute(command)

    def __createTeachersTable(self):
        command = """
        CREATE TABLE teachers(
            id char(64) primary key,
            firstname char(255),
            lastname char(255),
            phone char(20),
            email char(255),
            birthdate char(8),
            subject char(64),
            degree char(20)
        );
        """

        self.cursor.execute(command)

    def __executeCommand(self, command:str, commit:bool=False):
        try:
            self.cursor.execute(command)
            if commit:
                self.connection.commit()
            
            return { 'isSuccess': True, 'data': self.cursor.fetchall(), 'error': None }
        except Exception as e:
            return { 'isSuccess': False, 'data': None, 'error': e }
