# tests.py
import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        # Fix: Added age (22) to the constructor
        self.student = Student("Ahmed", 22)
        
    def test_creation(self):
        self.assertEqual(self.student.name, "Ahmed")

    def test_add_grade(self):
        self.student.Add_Grade("math", 90)
        self.assertEqual(self.student.grades["math"], 90)
        
    def test_enroll_course(self):
        self.student.enroll_in_course("Data Engineer")
        self.assertIn("Data Engineer", self.student.enrolled_courses)

if __name__ == '__main__':
    unittest.main()