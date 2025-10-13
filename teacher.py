from person import Person
from dbActions import dataBaseManager
class Teacher(Person):
    def __init__(self, firstName, lastName, birthYear, ID, subject):
        super().__init__(firstName, lastName, birthYear, ID)
        self._subject = subject
    


    def readData(self):
        self._firstName, self._lastName, self._birthYear = super().readData()
        self._subject = input("please enter your subject: ")
        return self._firstName, self._lastName, self._birthYear, self._subject

    
    def add(self):
        dataBaseManager(f"INSERT INTO Teachers (FirstName , LastName , BirthYear , Subject) VALUES ('{self._firstName}' , '{self._lastName}' , '{self._birthYear}' , '{self._subject}')")

    def edit(self):
        dataBaseManager(f"UPDATE Teachers set FirstName = '{self._firstName}' , LastName = '{self._lastName}' , BirthYear = '{self._birthYear}' , Subject = '{self._subject}' WHERE id = '{self._ID}'")

    def delete(self):
        dataBaseManager(f"DELETE FROM Teachers WHERE id = {self._ID}")
        