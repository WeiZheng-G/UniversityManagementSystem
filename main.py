from src.SAMR import Student
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

# Main process
while prompt != "exit":
    prompt = input("Enter command: ")
    match prompt:
        case "student_list":
            student.display()
        case "student_register":
            print("Enter student information")
            id = int(input("Student ID: "))
            name = input("name: ")
            year = input("year: ")
            department = input("department: ")
            module = input("module: ")
            isEnrol = "No"
            student.register(id, name, year, department, module, isEnrol)
        case "student_update":
            id = int(input("Student ID: "))
            print("Enter update information, <Enter> for unchange")
            name = input("name: ")
            year = input("year: ")
            department = input("department: ")
            module = input("module: ")
            isEnrol = "No"
            student.update(id, name, year, department, module, isEnrol)
        case "student_search":
            id = int(input("Student ID: "))
            student.search(id)
        case "exit":
            print("Program exits.")
        case _:
            print("Unknow command, enter again")

# dataset update
student.data.to_json('./data/student.json', indent=4)
