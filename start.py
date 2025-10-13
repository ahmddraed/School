import sqlite3
def addStudent():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"INSERT INTO Students (FirstName , LastName , BirthYear , ClassRoom) VALUES ('{firstName}' , '{lastName}' , '{birthYear}' , '{classRoom}')")
    con.commit()

def editStudent():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"UPDATE Students set FirstName = '{firstName}' , LastName = '{lastName}' , BirthYear = '{birthYear}' , ClassRoom = '{classRoom}' WHERE id = '{ID}'")
    con.commit()

def deleteStudent():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"DELETE FROM Students WHERE id = {ID}")
    con.commit()

def addTeacher():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"INSERT INTO Teachers (FirstName , LastName , BirthYear , Subject) VALUES ('{firstName}' , '{lastName}' , '{birthYear}' , '{subject}')")
    con.commit()

def editTeacher():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"UPDATE Teachers set FirstName = '{firstName}' , LastName = '{lastName}' , BirthYear = '{birthYear}' , Subject = '{subject}' WHERE id = '{ID}'")
    con.commit()

def deleteTeacher():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"DELETE FROM Teachers WHERE id = {ID}")
    con.commit()

def addEmployee():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"INSERT INTO Employees (FirstName , LastName , BirthYear , Department) VALUES ('{firstName}' , '{lastName}' , '{birthYear}' , '{department}')")
    con.commit()

def editEmployee():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"UPDATE Employees set FirstName = '{firstName}' , LastName = '{lastName}' , BirthYear = '{birthYear}' , department = '{department}' WHERE id = '{ID}'")
    con.commit()

def deleteEmployee():
    con = sqlite3.Connection("MySchool.db")
    con.execute(f"DELETE FROM Employees WHERE id = {ID}")
    con.commit()
while True:
    print('1) student actions')
    print('2) teacher actions')
    print('3) employee actions ')
    print('4) exit')
    selection = input('please, enter your choice: ')
    if selection == '1' :
        while True:
            print('student actions...')
            print('1) Add a student ')
            print('2) Edit a student ')
            print('3) Remove a student ')
            print('4) back to main menu ')
            selection = input('Enter your choice: ')
            if selection == '1':
                firstName = input("please enter student's first name: ")
                lastName = input("please enter student's last name: ")
                birthYear = input("pleasse enter student's birth year: ")
                classRoom = input("please enter student's classroom: ") 
                addStudent()
                print("student added successfully!")

            elif selection == '2':
                ID = input("enter the student's id: ")
                firstName = input("please enter the new student's first name: ")
                lastName = input("please enter the new student's last name: ")
                birthYear = input("pleasse enter the new student's birth year: ") 
                classRoom = input ("please enter the new student's classroom: ")
                editStudent()
                print('student has been updated successfully!')

            elif selection == '3':
                ID = input("enter the student's id: ")
                deleteStudent()
                print(f"the student with id {ID} has been deleted!")

            elif selection == '4':
                break

    elif selection == '2':
        while True:
            print ("Teacher actions...")
            print ("1) add a teacher")
            print ("2) edit a teacher")
            print("3) remove a teacher")
            print("4) back to main menu")
            selection = input ("enter your choice: ")

            if selection == '1':
                firstName = input("please enter teacher's first name: ")
                lastName = input("please enter teacher's last name: ")
                birthYear = input("pleasse enter teacher's birth year: ")
                subject = input("please enter teacher's subject: ") 
                addTeacher()
                print("teacher has been added successfully!")
            
            elif selection == '2':
                ID = input("enter the teacher's id: ")
                firstName = input("please enter the new teacher's first name: ")
                lastName = input("please enter the new teacher's last name: ")
                birthYear = input("pleasse enter the new teacher's birth year: ") 
                subject = input ("please enter the new teacher's subject: ")
                editTeacher()
                print("teacher has been updated successfully!")
            
            elif selection == '3':
                ID = input("enter the teacher's id: ")
                deleteTeacher()
                print(f"the teacher with id {ID} has been deleted!")
            
            elif selection == '4' :
                break

    elif selection == '3':
        while True:
            print ("Employees actions...")
            print ("1) add a Employee")
            print ("2) edit a Employee")
            print("3) remove Employee")
            print("4) back to main menu")
            selection = input ("enter your choice: ")

            if selection == '1' :
                firstName = input("please enter Employee's first name: ")
                lastName = input("please enter Employee's last name: ")
                birthYear = input("pleasse enter Employeer's birth year: ")
                department = input("please enter Employee's departement: ") 
                addEmployee()
                print("Employee has been added successfully!")
            
            elif selection == '2':
                ID = input("enter the employee's id: ")
                firstName = input("please enter the new Employee's first name: ")
                lastName = input("please enter the new Employee's last name: ")
                birthYear = input("pleasse enter the new Employee's birth year: ") 
                department = input ("please enter the new Employee's subject: ")
                editEmployee()
                print("employee has been updated successfully!")
            
            elif selection == '3':
                ID = input("enter the employee's id: ")
                deleteEmployee()
                print(f"the employee with id {ID} has been deleted!")
            
            elif selection == '4':
                break
            
    elif selection == '4':
        print("goodbye!")
        break



        





