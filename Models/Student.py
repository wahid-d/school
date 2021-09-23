from Models.Person import Person

class Student(Person):
    def __init__(self, fname, lname, bdate, phone, email, score):
        self.score = score
        self.grade = self.__getGrade(score)
        super().__init__(fname, lname, bdate, phone, email)
    
    def __getGrade(self, score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"""
        {super().__str__()}
        Score: {self.score}
        Grade: {self.grade}
        """

