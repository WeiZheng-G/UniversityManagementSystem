# Student Object
class Student:
    def __init__(self, dataset:object):
        self.data = dataset.set_index("id",drop=False)

    # Register
    def register(self,id:int, name:str, year:int):
        if (self._check(id)):
            print("Error: Register failed due to same id existing")
        else:
            self.data.loc[-1] = [id, name ,year ,"" ,"" ,"" ,"" ,["No", "No", "No", "No", "No"],0]
            self.data = self.data.set_index("id",drop=False)
            self.data = self.data.sort_index()
            print("Register successful.")

    # Display lists
    def display(self):
        if self.data.empty:
            return "No student yet."
        else:
            return self.data[["id","name","year","department","moduleCode", "moduleTitle","moduleTutor"]].to_string(index=False)

    # Update
    def update(self, id:int, name:str, year:int):
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

    # id check, internal use
    def _check(self, id:int)->bool:
        # Small dataset, linear search
        for exist_id in self.data["id"]:
            if (id == exist_id):
                return True
        return False