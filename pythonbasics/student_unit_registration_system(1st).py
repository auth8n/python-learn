class Student:
    def __init__(self, student_id: str, name: str, age: int, email: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.courses = []

    def register_course(self, course):
        if course in self.courses:
                return False
        self.courses.append(course)
        return True

    def drop_course(self, course):
        if course in self.courses:
                self.courses.remove(course)
                return "Course dropped."
        return "Student is not registered for this course."

    def get_course_count(self):
        return len(self.courses)

    def __str__(self):
        return f"Student(ID={self.student_id}, Name={self.name}, Age={self.age}, Email={self.email}, Courses={self.get_course_count()})"

class GraduateStudent(Student):
    def __init__(self, student_id: str, name: str, age: int, email: str, research_topic: str):
        super().__init__(student_id, name, age, email)
        self.research_topic = research_topic

    def __str__(self):
        return f"GraduateStudent(ID={self.student_id}, Name={self.name}, Age={self.age}, Email={self.email}, Courses={self.get_course_count()}, Research={self.research_topic})"

class RegistrationSystem:
    def __init__(self):
        self.registered_students = []

    def register_student(self, student):
        for existing_student in self.registered_students:
            if existing_student.student_id == student.student_id:
                return "Cannot register an already existing student."
        self.registered_students.append(student)

    def find_student(self, student_id):
        for existing_student in self.registered_students:
            if existing_student.student_id == student_id:
                return existing_student   
        return None

    def display_students(self):
        for student in self.registered_students:
            print(student)

    def remove_student(self, student_id):
        for existing_student in self.registered_students:
            if student_id == existing_student.student_id:
                self.registered_students.remove(existing_student)
                return existing_student
        return False

    def get_total_students(self):
        return len(self.registered_students)

    def get_students_by_course(self, course):
        students_list = []
        for existing_student in self.registered_students:
            if course in existing_student.courses:
                    students_list.append(existing_student)
        return students_list

student1 = Student(
    "ANU001", 
    "John Doe", 
    21,
    "john@example.com"
)

student2 = Student(
    "ANU002",
    "Mary Jane",
    22,
    "mary@example.com"
)

graduate1 = GraduateStudent(
    "ANU003", 
    "David Kim",
    25,
    "david@example.com",
    "Machine Learning"
)

student1.register_course("Python")
student1.register_course("Database Systems")
student1.register_course("Python")

student2.register_course("Networking")

graduate1.register_course("Artificial Intelligence")
graduate1.register_course("Machine Learning")

system = RegistrationSystem()

system.register_student(student1)
system.register_student(student2)
system.register_student(graduate1)

system.display_students()

found_student = system.find_student("ANU001")

if found_student:
    print("\nStudent found:")
    print(found_student)

removed_student = system.remove_student("ANU001")
if removed_student:
    print("\nRemoved student: ")
    print(removed_student)

python_students = system.get_students_by_course("Python")
if python_students:
    print("\nStudents registered for Python: ")
    for student in python_students:
        print(student)
else: 
    print("\nNo students are taking the specified course.")

total_number_students = system.get_total_students()
print("\nTotal number of students: ", total_number_students)



