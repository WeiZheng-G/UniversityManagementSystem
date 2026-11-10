## Introduction
This is a coursework project of DataScience&Python.

This project includes:
- Project requirements document
- Python implementation code & structures
- Fundings and limitations (fictional)

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
    - moduleTitle
    - moduleTutor
    - Attendance
    - Label
    - Mark

## Requirement
- Python
- pandas ``pip install pandas``
- matplotlib ``pip install matplotlib``
- Numpy ``pip insatll numpy``
- scipy ``pip install scipy``

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
- ``correlation``: investigate pearson correlation between attendance rates and marks
- ``chi``: investigate chi-squre statistic between attendance and label
- ``save`` to exit program with save
- ``exit`` to exit program without save

## Layout
```
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

4 directories, 11 files
```

## Implementation
![structure](doc/structure.png)

## Findings
- This coursework has implemented a practical model of foundamental EDA operations, including data inspection, cleaning and statistical analysis.
- Has implemented a simple Pearson correlation analysis, investigated the relationship between student attendance rates and marks.
    - null hypothesis: There is no linear correlation between student attendance rate and marks in this dataset
    - statistical significance threshold: 0.05
    - results of ``correlation``:
        - Pearson r: 0.3795293644986635 (moderate-strong correlation)
        - p-value: 0.015718690747166166 (which is smaller than 0.05)
        - Conclusion: Reject null hypothesis
    - Therefore, the result suggests that student attendances may be positively associated with marks.
- Has implemented a simple Chi-square statistic, investigated the relationship betwwen student attendances and labels.
    - null hypothesis: Attendance categories and pass/fail labels are independent
    - statistical significance threshold: 0.05
    - results of ``chi``:
        - chi statistic: 41.6017316017316
        - chi critical value: 3.841458820694124
        - p-value: 1.1189412127660878e-10 (which is smaller than 0.05)
        - Conclusion: Reject null hypothesis
    - Therefore, the result suggests an association between students' attendance catagories and pass/fail labels in this dataset.

## Limitations
- The dataset is intentionally generated with association between attendance and mark, association between attendance catagories and label in order to practise pearson/chi correlation analysis, do not suggest the real-world case. And also have no potential confounding factors.