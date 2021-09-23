import random
import string
from random import randint
from Models.Teacher import Teacher
from Models.Student import Student

class helpers:

    [classmethod]
    def randomString(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    
    [classmethod]
    def getRandomStudent():
        return Student(
            fname=helpers.randomString(10), 
            lname=helpers.randomString(10),
            bdate='1/1/2008 1:30 PM',
            phone=helpers.randomString(10),
            email=helpers.randomString(10),
            score=randint(1, 101))

    [classmethod]
    def getRandomTeacher():
        return Teacher(
            fname=helpers.randomString(10), 
            lname=helpers.randomString(10),
            bdate='1/1/2008 1:30 PM',
            phone=helpers.randomString(10),
            email=helpers.randomString(10),
            degree=helpers.randomString(5),
            subject=helpers.randomString(10))
