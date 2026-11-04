# Student Object
class Student:
    def __init__(self, dataset:object):
        self.data = dataset.set_index("id",drop=False)

    # Register
    def register(self,id:int, name:str, year:str, department:str="", moduleCode:str="", moduleTitle:str="", moduleTutor=""):
        if (self._check(id)):
            print("Error: Register failed due to same id existing")
        else:
            self.data.loc[-1] = [id,name,year,department,moduleCode, moduleTitle, moduleTutor]
            self.data = self.data.set_index("id",drop=False)
            self.data = self.data.sort_index()
            print("Register successful.")

    # Display lists
    def display(self):
        print(self.data[["id","name","year","department","moduleCode", "moduleTitle","moduleTutor"]].to_string(index=False))

    # Update
    def update(self, id:int, name:str, year:str):
        if (self._check(id)):
            columns = ("id", "name", "year")
            values = (id, name, year)
            for column, value in zip(columns, values):
                if value != "":
                    self.data.loc[self.data["id"]==id, column] = value     
            print("Update successful.")
        else:
            print("Error: Update failed due to missing student")

    # Search
    def search(self, id:int):
        if (self._check(id)):
            print(self.data.loc[id])
        else:
            print(f"No matching student: {id}")

    # Available modules
    def modules(self):
        print("available modules:\n" \
        "001. Science school - Math - Yan\n" \
        "002. Computing school - CS - Ben\n" \
        "003. Sports school - PE - Sam")

    # Enrol
    def enrol(self, id:int, moduleCode:str):
        if (self._check(id)):
            match moduleCode:
                case "001":
                    department = "Science school"
                    moduleTitle = "Math"
                    moduleTutor = "Yan"
                case "002":
                    department = "Computing school"
                    moduleTitle = "CS"
                    moduleTutor = "Ben"
                case "003":
                    department = "Sports school"
                    moduleTitle = "PE"
                    moduleTutor = "Sam"
                case _:
                    print("enrol failed: module not exist")
                    return False
            self.data.loc[self.data["id"]==id, "department"] = department
            self.data.loc[self.data["id"]==id, "moduleCode"] = moduleCode
            self.data.loc[self.data["id"]==id, "moduleTitle"] = moduleTitle
            self.data.loc[self.data["id"]==id, "moduleTutor"] = moduleTutor
            print("Enrol succeessful")
        else:
            print("Enrol failed: missing student")

    # id check, internal use
    def _check(self, id:int)->bool:
        # Small dataset, linear search
        for exist_id in self.data["id"]:
            if (id == exist_id):
                return True
        return False