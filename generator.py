import pandas as pd
import numpy as np


def generator_dataset(n:int, seed=2026, include_issues=True):
    rng = np.random.default_rng(seed)
    id = [i for i in range(1, n + 1)]
    name = rng.choice(["Wei", "Xu", "Fang"], size=n, p=[0.33, 0.34, 0.33])
    year = rng.integers(2021, 2026, size=n)
    department = rng.choice(
        ["Computing school", "Science school", "Sports school"],
        size=n,
        p=[0.15, 0.70, 0.15],
    )
    moduleCode = rng.choice(["MH", "CS", "PE"], size=n, p=[0.15, 0.70, 0.15])
    moduleTitle = rng.choice(
        ["Mathematics", "ComputerScience", "Football"], size=n, p=[0.15, 0.70, 0.15]
    )
    moduleTutor = rng.choice(["Yan", "Ben", "Sam"], size=n, p=[0.15, 0.70, 0.15])
    Attendance = rng.choice(["Yes", "No"], size=(n, 10), p=[0.75, 0.25])
    attendance_rate = (Attendance == "Yes").mean(axis=1)
    base_mark = rng.normal(40, 10, size=n)
    Mark = base_mark + attendance_rate * 40
    Mark = np.clip(Mark, 0, 100).astype(int)
    result = pd.DataFrame(
        {
            "id": id,
            "name": name,
            "year": year,
            "department": department,
            "moduleCode": moduleCode,
            "moduleTitle": moduleTitle,
            "moduleTutor": moduleTutor,
            "Attendance": Attendance.tolist(),
            "Mark": Mark,
        }
    )
    if include_issues:
        result.loc[rng.choice(n, 10, replace=False), "year"] = np.nan
        result.loc[rng.choice(n, 3, replace=False), "name"] = None
        result.loc[rng.choice(n, 2, replace=False), "Mark"] = np.nan
        result.loc[rng.choice(n, 5, replace=False), "Attendance"] = None
        result = pd.concat([result, result.iloc[[1, 5, 9]].copy()], ignore_index=True)
    return result


result = generator_dataset(80)
result.to_json("./data/student.json", indent=4)
