# course.py

class Course:
    __idcounter = 1
    
    def __init__(self, course_name):
        self.course_id = Course.__idcounter
        Course.__idcounter += 1
        self.course_name = course_name
        self.enrolled_students = []
        
    def __str__(self):
        return f"Course(course_id={self.course_id}, course_name={self.course_name}, enrolled_students={len(self.enrolled_students)})"
    
    def __repr__(self):
        return self.__str__()
        
    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"Student {student.name} enrolled in course {self.course_name}.")
        else:
            print(f"Student {student.name} is already enrolled in course {self.course_name}.")
            
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"Student {student.name} removed from course {self.course_name}.")
        else:
            print(f"Student {student.name} is not enrolled in course {self.course_name}.")