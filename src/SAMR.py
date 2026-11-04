# Student Object
class Student:
    def __init__(self, dataset:object):
        self.data = dataset.set_index("id",drop=False)

    # Register
    def register(self,id:int, name:str, year:str, department:str, module:str, isEnrol:str):
        if (self._check(id)):
            print("Error: Register failed due to same id existing")
        else:
            self.data.loc[-1] = [id,name,year,department,module,isEnrol]
            self.data = self.data.set_index("id",drop=False)
            self.data = self.data.sort_index()
            print("Register successful.")

    # Display lists
    def display(self):
        print(self.data.to_string(index=False))

    # Update
    def update(self, id:int, name:str, year:str, department:str, module:str, isEnrol:str):
        if (self._check(id)):
            columns = ("id", "name", "year", "department", "module", "isEnrol")
            values = (id, name, year, department, module, isEnrol)
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

    # duplication check, internal use
    def _check(self, id:int)->bool:
        # Small dataset, linear search
        for exist_id in self.data["id"]:
            if (id == exist_id):
                return True
        return False