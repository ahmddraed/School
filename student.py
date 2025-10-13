from person import Person
from dbActions import dataBaseManager
class Student(Person):
    def __init__(self, firstName, lastName, birthYear, ID, classRoom):
        super().__init__(firstName, lastName, birthYear, ID)
        self._classRoom = classRoom


    def readData(self):
        self._firstName, self._lastName, self._birthYear = super().readData()
        self._classRoom = input("please enter your class room: ")
        return self._firstName, self._lastName, self._birthYear, self._classRoom


    def add(self):
        dataBaseManager(f"INSERT INTO Students (FirstName , LastName , BirthYear , ClassRoom) VALUES ('{self._firstName}' , '{self._lastName}' , '{self._birthYear}' , '{self._classRoom}')")

    def edit(self):
        dataBaseManager(f"UPDATE Students set FirstName = '{self._firstName}' , LastName = '{self._lastName}' , BirthYear = '{self._birthYear}' , ClassRoom = '{self._classRoom}' WHERE id = '{self._ID}'")

    def delete(self):
        dataBaseManager(f"DELETE FROM Students WHERE id = {self._ID}")
