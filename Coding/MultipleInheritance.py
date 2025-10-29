class Student:
    school = "ABC Academy"

    def caller(self):
        print("This is a caller method")
        CourseStudent.info()
        CourseStudent.Local_info()

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):     
        x=10                 # Instance Method
        print(f"Name: {self.name}, Marks: {self.marks}")

    @classmethod
    def school_info(cls):   
        print(cls.school)             # Class Method
        print(f"School Name: {cls.school}")

    @staticmethod
    def greet():                         # Static Method
        print("Welcome to ItTechGenie Python Course!")

Student.greet()
Student.school_info()
 
class CourseStudent(Student):
    def __init__(self, name, marks, course, Student[]):
        super().__init__(name, marks)
        self.course = course
        self.students = Student[]

    @staticmethod
    def courseInfo():                         # Static Method
        print("Welcome to ABC Python Course!")

    @classmethod
    def Local_info(cls):   
        print(f"School Name from CourseStudent: {cls.school}")

student1 = CourseStudent("John", 85, "Python", ["John", "Alice", "Bob"])