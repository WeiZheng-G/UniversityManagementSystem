from src.studentmanagement import Student
import pandas as pd

#Dataset Student loading
students = pd.read_json('./data/student.json')

# Create object
student = Student(students)

# Usage
prompt = ""
print("-----------------------------------")
print("Please check README.md usage field")
print("-----------------------------------")

# Main process_
while prompt != "exit":
    prompt = input("$$: ")
    match prompt:
        case "list":
            student.display()
        case "register":
            print("Enter student information")
            id = int(input("Student ID: "))
            name = input("name: ")
            year = int(input("year: "))
            student.register(id, name, year)
        case "update":
            id = int(input("Student ID: "))
            print("Enter update information, <Enter> for unchange")
            name = input("name: ")
            year = int(input("year: "))
            student.update(id, name, year)
        case "search":
            id = int(input("Student ID: "))
            student.search(id)
        case "modules":
            student.modules()
        case "enrol":
            id = int(input("Student ID: "))
            moduleCode = input("moduleCode: ")
            student.enrol(id,moduleCode)
        # Exception command
        case "exit":
            print("Program exits.")
        case _:
            print("Unknow command, enter again")

# dataset update
student.data.to_json('./data/student.json', indent=4)
