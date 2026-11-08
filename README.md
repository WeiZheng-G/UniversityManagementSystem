## Introduction
This is a coursework project of DataScience&Python.

This project includes:
- Project requirements document
- Python implementation code & structures
- Project documentation

## Project requirements document
[Project requirement pdf](doc/University_Management_System_Midterm_Project.pdf)

## Dataset

Use generator generates finctional dataset randomly.

- ### Attributes:
    - Student ID
    - name
    - year (e.g. 2026)
    - department
    - moduleCOde
    - moduleTitie
    - moduleTutor
    - Attendance
    - Mark

## Requirement
- Python
- pandas ``pip install pandas``
- matplotlib ``pip install matplotlib``
- Numpy ``pip insatll numpy``

## Usage
install ``git clone https://github.com/WeiZheng-G/UniversityManagementSystem.git`` and ``cd UniversityManagementSystem``

Run ``python generator.py`` to generate random dataset

Run ``python main.py``

Enter ``<command>``:

- ``list``: Display student list
- ``register``: Enter information to register
- ``update``: Update exist student records
- ``search``: Search student info using student id
- ``modules``: List available modules
- ``enrol``: Enrol student on module using student ID and module code
- ``attend``: check student's attendance
- ``mark``: check student's mark
- ``rule``: change attendance&mark thresholds
- ``stat``: Plot bar&scatter&line graphs of mark verses year
- ``missing``: check dataset missing
- ``duplicate``: check dataset duplicating
- ``save`` to exit program with save
- ``exit`` to exit program without save

## Layout
```
.
├── data
│   └── student.json
├── doc
│   ├── structure.png
│   ├── structure.puml
│   └── University_Management_System_Midterm_Project.pdf
├── generator.py
├── main.py
├── README.md
└── src
    ├── Attendance.py
    ├── dashboard.py
    ├── Enrol.py
    └── StudentInfo.py
```

## Implementation
![structure](doc/structure.png)