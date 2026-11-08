# Student Object
class Enrol:
    def __init__(self, obj:object):
        self.obj = obj

    # Available modules
    def modules(self):
        print("available modules:\n" \
        "Code: MH - Science school - Mathematics - Yan\n" \
        "Code: CS - Computing school - ComputerScience - Ben\n" \
        "Code: PE - Sports school - Football - Sam")

    # Enrol
    def enrol(self, id:int, moduleCode:str):
        if (self.obj._check(id)):
            match moduleCode:
                case "MH":
                    department = "Science school"
                    moduleTitle = "Mathematics"
                    moduleTutor = "Yan"
                case "CS":
                    department = "Computing school"
                    moduleTitle = "ComputerScience"
                    moduleTutor = "Ben"
                case "PE":
                    department = "Sports school"
                    moduleTitle = "Football"
                    moduleTutor = "Sam"
                case _:
                    print("enrol failed: module not exist")
                    return False
            self.obj.data.loc[self.obj.data["id"]==id, "department"] = department
            self.obj.data.loc[self.obj.data["id"]==id, "moduleCode"] = moduleCode
            self.obj.data.loc[self.obj.data["id"]==id, "moduleTitle"] = moduleTitle
            self.obj.data.loc[self.obj.data["id"]==id, "moduleTutor"] = moduleTutor
            print("Enrol succeessful")
        else:
            print("Enrol failed: missing student")