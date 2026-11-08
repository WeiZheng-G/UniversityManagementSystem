from src.StudentInfo import Student
from src.Enrol import Enrol
from src.Attendance import Attend_Mark
from src.dashboard import Dashboard
from IPython.display import display
import pandas as pd

## initial
def initialization():
    #Dataset Student loading
    students = pd.read_json('./data/student.json')
    students_new = students.copy()
    students_new["Attendance"] = students_new["Attendance"].astype("object")
    # Create object
    student = Student(students_new)
    enrol = Enrol(student)
    attend = Attend_Mark(student)
    dashboard = Dashboard(student)
    return student, enrol, attend, dashboard

## User interactor
def interactor():
    student, enrol, attend, dashboard = initialization()
    # Usage
    prompt:str = ""
    print("-----------------------------------")
    print("Please check README.md usage field")
    print("-----------------------------------")

    # Main process_
    while (1) :
        prompt = input("$$: ")
        match prompt:
            case "list":
                display(student.display())
            case "register":
                print("Enter student information")
                id:int = int(input("Student ID: "))
                name:str = input("name: ")
                year:int = int(input("year: "))
                student.register(id, name, year)
            case "update":
                id:int = int(input("Student ID: "))
                print("Enter update information, <Enter> for unchange")
                name = input("name: ")
                year:int = int(input("year: "))
                student.update(id, name, year)
            case "search":
                id:int = int(input("Student ID: "))
                student.search(id)
            case "modules":
                student.modules()
            case "enrol":
                id:int = int(input("Student ID: "))
                moduleCode:str = input("moduleCode: ")
                enrol.enrol(id,moduleCode)
            case "attend":
                id:int = int(input("Student ID: "))
                print(attend.Attend(id))
            case "mark":
                id:int = int(input("Student ID: "))
                print(attend.Mark(id))
            case "rule":
                attend_thresholds:int = int(input("attend_thresholds: "))
                mark_thresholds:int = int(input("mark_thresholds: "))
                print(attend.rules(attend_thresholds,mark_thresholds))
            case "stat":
                dashboard.stat()
            case "missing":
                display(dashboard.missing())
            case "duplicate":
                display(dashboard.duplicate())
            # Exception command
            case "exit":
                break
            case "save":
                student.data.to_json('./data/student.json', indent=4)
                print("Data saved.")
                break
            case _:
                print("Unknow command, enter again")

## main process
interactor()
print("Program exited.")
