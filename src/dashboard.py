import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


class Dashboard:
    def __init__(self, obj: object):
        self.obj = obj

    # counts, mean/median marks, plot
    def stat(self):
        try:
            # cleaning
            cleaning_data = self.obj.data.copy().dropna().drop_duplicates(subset=["id"])
            print(cleaning_data["Mark"].describe().round(2))

            fig, axis = plt.subplots(1, 3, figsize=(7, 4))
            mean_years = cleaning_data.groupby("year")["Mark"].mean()
            # Bar chart
            mean_years.plot(
                kind="bar", color="#4477AA", rot=0, figsize=(7, 4), ax=axis[0]
            )
            axis[0].set(
                title="Average marks of each years", xlabel="YEARS", ylabel="MARK"
            )
            axis[0].set_ylim(bottom=0)
            # Scatter plot
            cleaning_data.plot(
                kind="scatter",
                x="year",
                y="Mark",
                color="#4477AA",
                figsize=(7, 4),
                ax=axis[1],
            )
            axis[1].set(
                title="Every marks of each years", xlabel="YEARS", ylabel="MARK"
            )
            axis[1].set_ylim(bottom=0)
            # Line plot
            mean_years.plot(
                kind="line", marker="o", color="#4477AA", figsize=(7, 4), ax=axis[2]
            )
            axis[2].set(
                title="Average marks of each years", xlabel="YEARS", ylabel="MARK"
            )
            axis[2].set_ylim(bottom=0)

            # Integer year labels for scatter and line charts
            years = sorted(cleaning_data["year"].unique())
            axis[1].set_xticks(years)
            axis[2].set_xticks(years)

            plt.tight_layout()
            plt.show()
        except:
            print("Missing or depulicated value exists.")

    def missing(self):
        missing = self.obj.data.isnull()
        if missing.values.any():
            return self.obj.data[missing.any(axis=1)]
        else:
            return "No missing value"

    def duplicate(self):
        duplicated = self.obj.data.drop(columns=["Attendance"]).duplicated()
        if duplicated.any():
            return self.obj.data[duplicated]
        else:
            return "No duplicated value"

    def correlation(self):
        alpha = 0.05
        cleaning_data = self.obj.data.copy().dropna().drop_duplicates(subset=["id"])
        # Pearson correlation between attendance vs marks
        dataset = cleaning_data.loc[
            cleaning_data["moduleCode"] == "CS",
            ["Attendance", "Mark"]
        ]
        attendance_count = dataset["Attendance"].apply(
            lambda x: (np.array(x) == "Yes").sum()
        )
        attendance_rate = attendance_count / 10
        result = stats.pearsonr(
            attendance_rate,
            dataset["Mark"]
        )
        print(f"Pearson r: {result.statistic:.3f}")
        print(f"P-value: {result.pvalue:.3g}")
        print(f"Alpha: {alpha}")
        decision_text = (
            "Reject H0: There is no linear correlation between student attendance rate and marks in this dataset"
            if result.pvalue <= alpha
            else "Fail to reject H0: There is no linear correlation between student attendance rate and marks in this dataset"
        )
        print(decision_text)

    def chi(self):
        alpha = 0.05
        cleaning_data = self.obj.data.copy().dropna().drop_duplicates(subset=["id"])
        attendance_rate = [
            student.count("Yes") / len(student)
            for student in cleaning_data["Attendance"]
        ]
        attendance_category = [
            "High" if rate >= 0.75 else "Low"
            for rate in attendance_rate
        ]
        observed_dataset = pd.DataFrame({
            "Attendance": attendance_category,
            "Label": cleaning_data["Label"]
        })
        observed_dataset_cross = pd.crosstab(observed_dataset["Attendance"],observed_dataset["Label"])
        chi = stats.chi2_contingency(
            observed_dataset_cross
        )
        chi_critical = stats.chi2.ppf(1 - alpha, 1)
        print(f"chi statistic: {chi.statistic:.3f}")
        print(f"chi critical value: {chi_critical:.3f}")
        print(f"Alpha: 0.05")
        print(f"p-value: {chi.pvalue:.3f}")
        decision_text = (
            "Reject H0: Attendance category and pass/fail label are independent"
            if chi.pvalue <= alpha
            else "Fail to reject H0: Attendance category and pass/fail label are independent"
        )
        print(decision_text)