from dbActions import dataBaseManager
class Person:
    def __init__(self,firstName,lastName,birthYear,ID):
        self._fistName = firstName
        self._lastName = lastName
        self._birthYear = birthYear
        self._ID = ID
    
    def readData(self):
        self._fistName = input("please enter first name: ")
        self._lastName = input("please enter last name: ")
        self._birthYear = input("pleasse enter birth year: ")
        return self._fistName , self._lastName , self._birthYear
    
    def readID(self):
        self.ID = input( "please, enter ID")
        return self._ID
    
            



    






        
    
