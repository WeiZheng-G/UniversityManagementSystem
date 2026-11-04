## Introduction
This is a coursework project of DataScience&Python.

This project includes:
- Project requirements document
- Python implementation code
- Project documentation

## Project requirements document
[Project requirement pdf](./doc/University_Management_System_Midterm_Project.pdf)

## Dataset
Mannually input #TODO Random generator
- ### factors:
    - Student ID
    - name
    - year (e.g. 2026)
    - department
    - moduleCOde
    - moduleTitie
    - moduleTutor

## Requirement
- Python
- pandas ``pip install pandas``

## Implementation
- **<main.py>**: main processor
- **<studentmanagement.py>**:

    Functions of :
    - Student and module records: register, display, search, update
    - Enrolment management: modules list, enrol
- **<student.json>**: Dataset file, used for load and save

## Usage
Run ``python main.py``

Enter ``<command>``:

- ``list``: Display student list
- ``register``: Enter information to register
- ``update``: Update exist student records
- ``search``: Search student info using student id
- ``modules``: List available modules
- ``enrol``: Enrol student on module using student ID and module code
- ``exit`` to exit program, autosave