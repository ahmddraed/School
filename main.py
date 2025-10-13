
from student import Student
from teacher import Teacher
from employee import Employee
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
                s = Student('', '' ,'', None ,'')
                s.readData()
                s.add()
                print("student added successfully!")

            elif selection == '2':
                s = Student('','','',None,'')
                s.readID()
                s.readData()
                s.edit()
                print('student has been updated successfully!')

            elif selection == '3':
                s = Student('','','',None,'')
                s.readID()
                s.delete()
                print(f"the student with id {s.ID} has been deleted!")

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
                t = Teacher('','','',None,'')
                t.readData()
                t.add()
                print("teacher has been added successfully!")

            elif selection == '2':
                t = Teacher('','','',None,'')
                t.readID()
                t.readData()
                t.edit()
                print("teacher has been updated successfully!")
            
            elif selection == '3':
                t = Teacher('','','',None,'')
                t.readID()
                t.delete()
                print(f"the teacher with id {t.ID} has been deleted!")
            
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
                e = Employee('','','',None,'')
                e.readData()
                e.add()
                print("Employee has been added successfully!")
            
            elif selection == '2':
                e = Employee('','','',None,'')
                e.readID()
                e.readData()
                e.edit()
                print("employee has been updated successfully!")
            
            elif selection == '3':
                e = Employee('','','',None,'')
                e.readID()
                e.delete()
                print(f"the employee with id {e.ID} has been deleted!")
            
            elif selection == '4':
                break
            
    elif selection == '4':
        print("goodbye!")
        break
