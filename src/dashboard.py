import matplotlib.pyplot as plt
class dashboard:
    def __init__(self,obj:object):
        self.obj = obj

    # counts, mean/median marks, plot
    def stat(self):
        print(self.obj.data["Mark"].describe().round(2))

        fig, axis=plt.subplots(1, 3, figsize=(7,4))
        mean_years = self.obj.data.groupby("year")["Mark"].mean()
        # Bar chart
        mean_years.plot(kind="bar", color="#4477AA", rot=0, figsize=(7,4), ax=axis[0])
        axis[0].set(title="Average marks of each years",xlabel="YEARS",ylabel="MARK")
        axis[0].set_ylim(bottom=0)
        # Scatter plot
        self.obj.data.plot(kind="scatter", x="year", y="Mark", color="#4477AA",figsize=(7,4), ax=axis[1])
        axis[1].set(title="Every marks of each years",xlabel="YEARS",ylabel="MARK")
        axis[1].set_ylim(bottom=0)
        # Line plot
        mean_years.plot(kind="line", marker="o", color="#4477AA",figsize=(7,4), ax=axis[2])
        axis[2].set(title="Average marks of each years",xlabel="YEARS",ylabel="MARK")
        axis[2].set_ylim(bottom=0)

        # Integer year labels for scatter and line charts
        years = sorted(self.obj.data["year"].unique())
        axis[1].set_xticks(years)
        axis[2].set_xticks(years)

        plt.tight_layout()
        plt.show()

    def missing(self):
        if (self.obj.data.isnull().values.any()):
            return self.obj.data[self.obj.data.isnull().any(axis=1)]
        else:
            return "No missing value"

    def duplicate(self):
        if (self.obj.data.duplicated().any()):
            return self.obj.data[self.obj.data.duplicated()]
        else:
            return "No duplicated value"
