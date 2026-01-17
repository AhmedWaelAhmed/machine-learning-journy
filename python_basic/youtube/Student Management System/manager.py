# manager.py
from student import Student
from course import Course

class SystemManager:
    def __init__(self):
        self.Students = {}
        self.Courses = {}
    
    def add_student(self, name, age):
        # Fix: Passed age to Student constructor
        student = Student(name, age)
        self.Students[student.student_id] = student
        print(f"Student {student.name} added with ID {student.student_id}.")
        
    def remove_student(self, student_id):
        if student_id in self.Students:
            del self.Students[student_id]
            print(f"Student with ID {student_id} removed.")
        else:
            print(f"Student with ID {student_id} not found.")
            
    def add_course(self, course_name):
        course = Course(course_name)
        self.Courses[course.course_id] = course
        print(f"Course {course.course_name} added with ID {course.course_id}.")
        
    def remove_course(self, course_id):
        if course_id in self.Courses:
            del self.Courses[course_id]
            print(f"Course with ID {course_id} removed.")
        else:
            print(f"Course with ID {course_id} not found.")
            
    def enroll_student_in_course(self, student_id, course_id):
        if student_id in self.Students and course_id in self.Courses:
            student = self.Students[student_id]
            course = self.Courses[course_id]
            # Enrolling in the course object
            course.enroll_student(student)
            # Optional: Update the student record as well to keep them in sync
            student.enroll_in_course(course.course_name)
        else:
            print("Invalid student ID or course ID.")
            
    def search_courses(self, search_name):
        result = []
        for course in self.Courses.values():
            if search_name.lower() in course.course_name.lower():
                result.append(course.course_name)
        return result
        
    def search_students(self, search_name):
        result = []
        for student in self.Students.values():
            if search_name.lower() in student.name.lower():
                result.append(student.name)
        return result
        
    def record_grade(self, student_id, course_name, grade):
        if student_id in self.Students:
            student = self.Students[student_id]
            student.Add_Grade(course_name, grade)
            print(f"Recorded grade {grade} for student {student.name} in course {course_name}.")
        else:
            print(f"Student with ID {student_id} not found.")
            
    def get_all_students(self):
        return list(self.Students.values())
        
    def get_all_courses(self):
        return list(self.Courses.values())