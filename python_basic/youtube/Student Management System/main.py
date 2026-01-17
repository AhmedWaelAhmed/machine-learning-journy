# main.py
from manager import SystemManager

def show_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Add Course")
    print("4. Remove Course")
    print("5. Enroll Student in Course")
    print("6. Search Courses")
    print("7. Search Students")
    print("8. Record Grade")
    print("9. View All Students")
    print("10. View All Courses")
    print("11. Exit")

def add_student_handler(manager):
    name = input("Enter student name: ")
    # Fix: Ask for age and handle errors
    try:
        age = int(input("Enter student age: "))
        manager.add_student(name, age)
    except ValueError:
        print("Invalid input! Age must be a number.")

def core():
    manager = SystemManager()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student_handler(manager)
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID to remove: "))
                manager.remove_student(student_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            course_name = input("Enter course name: ")
            manager.add_course(course_name)
        elif choice == '4':
            try:
                course_id = int(input("Enter course ID to remove: "))
                manager.remove_course(course_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            try:
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                manager.enroll_student_in_course(student_id, course_id)
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '6':
            search_name = input("Enter course name to search: ")
            results = manager.search_courses(search_name)
            print("Search Results:", results)
        elif choice == '7':
            search_name = input("Enter student name to search: ")
            results = manager.search_students(search_name)
            print("Search Results:", results)
        elif choice == '8':
            try:
                student_id = int(input("Enter student ID: "))
                course_name = input("Enter course name: ")
                grade = float(input("Enter grade: "))
                manager.record_grade(student_id, course_name, grade)
            except ValueError:
                print("Invalid input.")
        elif choice == '9':
            students = manager.get_all_students()
            for student in students:
                print(student)
        elif choice == '10':
            courses = manager.get_all_courses()
            for course in courses:
                print(course)
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    core()