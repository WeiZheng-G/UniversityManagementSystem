from src.SAMR import Student

modules = {
    "code":[101,102,103],
    "title":["Math","English","PE"],
    "Tutor":["A","B","C"]
}

students = {
    "id":[1],
    "name":["Wei"],
    "year":[1998],
    "department":["Science"],
    "module":["Math"],
    "isEnrol":["No"]
}

# Create object
student = Student(students)

# Usage
prompt = ""
print("---------------------------------")
print("Command menu:\n" \
"1. Student and module records\n" \
"   1.1 <student_list>\n" \
"   1.2 <student_register>\n" \
"   1.3 <student_update>\n" \
"   1.4 <student_search>\n" \
"<exit>: Exit program")
print("---------------------------------")

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
            year = int(input("year: "))
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