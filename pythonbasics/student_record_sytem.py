class StudentRecords:
    def __init__(self):
        self.records = {}

    def add_student(self, id: int, name: str, course:str):
        if id in self.records:
            self.records[id].update({"name": name,
                                     "course": course})
        else:
            self.records[id] = {"name": name,
                                "course": course}

    def remove_student(self, id: int):
        if id in self.records:
            self.records.pop(id, None)

    def lookup_student(self, id: int):
        if id in self.records:
            return self.records[id]
        else:
            return None

    def list_students(self):
        result = ""
        for student in self.records:
            for key,  value in self.records[student].items():
                result += f"{key}: {value}\n"
        return result


students = StudentRecords()

students.add_student(100, "Collins", "Computer")
students.add_student(101, "Nereah", "Law")
students.add_student(102, "Vincent", "Law")

print(students.lookup_student(100))

students.remove_student(100)
print(students.list_students())



    