from Models.Student import Student
from Helpers import helpers
from school import School

from pprint import pprint

najottalim = School()

def testWithRandomData():
    for i in range(10):
        najottalim.addStudent(helpers.getRandomStudent())
        najottalim.addTeacher(helpers.getRandomTeacher())

    for student in najottalim.allStudents():
        print(student)

    for teacher in najottalim.allTeachers():
        print(teacher)

    for person in najottalim.search('1/1/2008 1:30 PM'):
        print(person)

def printMenu():
    print("This is LMS for Najot Ta'lim")
    print("Select the operation number:\n\n")
    print('1. Print all Students')
    print('2. Print all Teachers')
    print('3. Add student')
    print('4. Add Teacher')
    print('5. Search')
    print('6. Exit\n\n:| ', end='')

def mainLoop():
    while True:

        printMenu()

        option:int = 0
        try:
            option = int(input())
        except ValueError:
            print('Wrong option selected. Try again!')
        
        # if option == 1:
        #     print(najottalim.allStudents())
        # elif option == 2:
        #     print(najottalim.allTeachers())
        # elif option == 3:
            
# mainLoop()
# testWithRandomData()

eshmat = Student('Eshmat', 'Toshmatov', '19960228', '+998950126172', 'eshmat@mail.ru', 79)
# print(najottalim.addStudent(eshmat))
pprint(najottalim.allStudents())