class CourseRegistration:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_code:int, course_name:str):
        self.courses[course_code] = {
            "name": course_name,
            "students": []
        }

    def register_student(self, course_code:int, student_name:str):
        if course_code in self.courses:
            students = self.courses[course_code]["students"]
            if student_name in students:
                students.append(student_name)

    def drop_student(self, course_code: int, student_name:str):
        if course_code in self.courses:
            students = self.courses[course_code]["students"]
            if student_name in students:
                students.remove(student_name)

    def get_course(self, course_code:int):
        return self.courses.get(course_code)

courses = CourseRegistration()

courses.add_course(100, "Networking")
courses.add_course(101, "Design")
courses.add_course(102, "Architecture")


courses.register_student(100, "Adrian")
courses.register_student(100, "Nicole")
courses.register_student(101, "Drake")

print(courses.get_course(100))