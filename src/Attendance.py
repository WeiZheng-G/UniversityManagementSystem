# Student Object
class Attend_Mark:
    def __init__(self, obj: object):
        self.obj = obj
        self.attend_thresholds = 75
        self.mark_thresholds = 40

    # Attendance
    def Attend(self, id: int):
        if self.obj._check(id):
            attendance = self.obj.data.loc[id, "Attendance"]
            percentage = attendance.count("Yes") / 10
            if percentage >= self.attend_thresholds:
                LABEL = "Safe"
            else:
                LABEL = "Alert"
            return f"Attend: {percentage}%\nWeekly: {attendance}\nAssess: {LABEL}"

        else:
            return "Failed: missing student"

    # Mark
    def Mark(self, id: int):
        if self.obj._check(id):
            mark = self.obj.data.loc[id, "Mark"]
            if mark >= self.mark_thresholds:
                LABEL = "PASS"
            else:
                LABEL = "FAIL"
            return f"Mark: {mark}\nAssess: {LABEL}"
        else:
            return "Failed: missing student"

    # Rules
    def rules(self, attend: int, mark: int):
        self.attend_thresholds = attend
        self.mark_thresholds = mark
        return f"Attend: {self.attend_thresholds}, Mark: {self.mark_thresholds}"
