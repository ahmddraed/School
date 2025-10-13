from person import Person
from dbActions import dataBaseManager
class Employee(Person):
    def __init__(self, firstName, lastName, birthYear, ID, department):
        super().__init__(firstName, lastName, birthYear, ID)
        self._department = department


    def readData(self):
        self._firstName, self._lastName, self._birthYear = super().readData()
        self._department = input("please enter your department: ")
        return self._firstName, self._lastName, self._birthYear, self._department

    
    def add(self):
        dataBaseManager(f"INSERT INTO Employees (FirstName , LastName , BirthYear , Department) VALUES ('{self._firstName}' , '{self._lastName}' , '{self._birthYear}' , '{self._department}')")
    
    def edit(self):
        dataBaseManager(f"UPDATE Employees set FirstName = '{self._firstName}' , LastName = '{self._lastName}' , BirthYear = '{self._birthYear}' , department = '{self._department}' WHERE id = '{self._ID}'")

    def delete(self):
        dataBaseManager(f"DELETE FROM Employees WHERE id = {self._ID}")