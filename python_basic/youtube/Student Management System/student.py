# student.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

class Student(Person):
    _id_counter = 1
    
    def __init__(self, name, age):
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.age = age
        self.grades = {}
        self.enrolled_courses = []
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id}, grades={self.grades}, enrolled_courses={self.enrolled_courses})"
    
    def __repr__(self):
        return self.__str__()   
    
    def Add_Grade(self, course, grade):
        self.grades[course] = grade 

    def enroll_in_course(self, course_name):
        self.enrolled_courses.append(course_name)