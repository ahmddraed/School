import sqlite3
def dataBaseManager(query:str)->str:
    con = sqlite3.Connection("MySchool.db")
    q = con.execute(query)
    con.commit()
    return q










            

            


