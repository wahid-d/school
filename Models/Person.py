import uuid

class Person:
    def __init__(self, fname, lname, bdate, phone, email):
        self.id = str(uuid.uuid4())
        self.firstname = fname
        self.lastname = lname
        self.birthdate = bdate
        self.phone = phone
        self.email = email
    
    def __str__(self) -> str:
        return f"""
        ID: {self.id}
        First Name: {self.firstname}
        Last Name: {self.lastname}
        Birthdate: {self.birthdate}
        Phone: {self.phone}
        Email: {self.email}
        """