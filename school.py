from storage import Storage
from Models.Student import Student
from Models.Teacher import Teacher


class School:

    def __init__(self):
        self.__storage = Storage('school.db')

    def addStudent(self, student:Student):
        return self.__storage.insertStudent(student)
    
    def addTeacher(self, teacher:Teacher):
        return self.__storage.insertTeacher(teacher)

    def allStudents(self):
        return self.__storage.getAllStudents()['data']
    
    def allTeachers(self):
        return self.__storage.getAllTeachers()['data']
    
    def search(self, query):
        result = []
        
        result.extend([student for student in self.students if self.__queryStudent(student, query)])
        result.extend([teacher for teacher in self.teachers if self.__queryTeacher(teacher, query)])

        return result
    
    def __queryStudent(self, s:Student, query):
        if s.firstname == query or s.lastname == query or s.phone == query or s.birthdate == query or s.email == query or s.id == query:
            return True
        else:
            return False

    def __queryTeacher(self, s:Teacher, query):
        if s.firstname == query or s.lastname == query or s.phone == query or s.birthdate == query or s.email == query or s.id == query:
            return True
        else:
            return False
    

    