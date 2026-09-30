import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "students.json")
students = {
    101: {"name": "Aarav Sharma", "age": 14, "class": "8th", "active": True},
    102: {"name": "Fatima Zahra", "age": 15, "class": "9th", "active": True},
    103: {"name": "Bilal Ahmed", "age": 16, "class": "10th", "active": False},
    104: {"name": "Sara Khan", "age": 14, "class": "8th", "active": True},
    105: {"name": "Zayn Malik", "age": 15, "class": "9th", "active": False},
    106: {"name": "Ananya Patel", "age": 16, "class": "10th", "active": True},
    107: {"name": "Hamza Ali", "age": 13, "class": "7th", "active": True},
    108: {"name": "Mariam Tariq", "age": 15, "class": "9th", "active": True},
    109: {"name": "Rohan Gupta", "age": 17, "class": "11th", "active": False},
    110: {"name": "Ayesha Siddiqui", "age": 14, "class": "8th", "active": True},
    111: {"name": "Usman Sheikh", "age": 16, "class": "10th", "active": True},
    112: {"name": "Diya Sen", "age": 13, "class": "7th", "active": False},
    113: {"name": "Omar Farooq", "age": 18, "class": "12th", "active": True},
    114: {"name": "Khadija Noor", "age": 15, "class": "9th", "active": True},
    115: {"name": "Kabir Mehta", "age": 17, "class": "11th", "active": True},
    116: {"name": "Zoya Akhtar", "age": 14, "class": "8th", "active": False},
    117: {"name": "Mustafa Raza", "age": 16, "class": "10th", "active": True},
    118: {"name": "Pooja Verma", "age": 18, "class": "12th", "active": True},
    119: {"name": "Ibrahim Qureshi", "age": 13, "class": "7th", "active": True},
    120: {"name": "Sana Mirza", "age": 17, "class": "11th", "active": False}
}

def save_to_json():
    with open(JSON_FILE, mode="w", encoding="utf-8") as file:

        json.dump(students, file, indent=4)
def initialize_json():
    global students
    if not os.path.exists(JSON_FILE):
        save_to_json()
    else:
        with open(JSON_FILE, mode="r", encoding="utf-8") as file:
            
            loaded_data = json.load(file)
            students = {int(k): v for k, v in loaded_data.items()}

def search_by_id():
    try:
        x = int(input("Enter the ID of student: "))
        if x in students:
            
            print(f"\n{'Name':<18} {'Age':<8} {'Class':<8} {'Active':<8}")
            
            print("=" * 44)
            print(f"{students[x]['name']:<18} {students[x]['age']:<8} {students[x]['class']:<8} {str(students[x]['active']):<8}")
        else:
            print("Incorrect ID! Please enter a correct ID.")
    except ValueError:
        print("Please enter a valid numeric ID.")

def new_student():
    try:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            print("A student with this ID already exists!")
            return
        student_name = input("Enter student name: ").strip()
        student_age = int(input("Enter student age: "))
        student_class = input("Enter student class: ").strip()
        active = input("Is the student active? (yes/no): ").strip().lower() == "yes"
        students[student_id] = {
            "name": student_name,
            "age": student_age,
            "class": student_class,
            "active": active
        }
        save_to_json()
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Age and ID must be numbers.")

def all_students():
    print(f"\n{'ID':<8} {'Name':<20} {'Age':<8} {'Class':<8} {'Active':<8}")
    print("=" * 52)
    for s_id, info in students.items():
        print(f"{s_id:<8} {info['name']:<20} {info['age']:<8} {info['class']:<8} {str(info['active']):<8}")

def exit_system():
    print("Good Bye! Best of Luck!")

def search_by_name():
    student_name = input("Enter student name: ").strip().lower()
    found = False
    for s_id, info in students.items():
        if info['name'].lower() == student_name:
            print("\n" + "=" * 25)
            print(f"ID:     {s_id}")
            print(f"Name:   {info['name']}")
            print(f"Age:    {info['age']}")
            print(f"Class:  {info['class']}")
            print(f"Active: {info['active']}")
            print("=" * 25)
            found = True
    if not found:
        print("Student not found!")

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        if student_id in students:
            del students[student_id]
            save_to_json()
            print(f"Student {student_id} deleted successfully!")
        else:
            print("Student ID not found!")
    except ValueError:
        print("Please enter a valid numeric ID.")

def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        if student_id not in students:
            print("Student ID not found!")
            return
        print("\nCurrent Student Information:")
        print(f"Name: {students[student_id]['name']}")
        print(f"Age: {students[student_id]['age']}")
        print(f"Class: {students[student_id]['class']}")
        print(f"Active: {students[student_id]['active']}")
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Class")
        print("4. Active Status")
        choice = input("Choose an option: ")
        if choice == "1":
            new_name = input("Enter new name: ").strip()
            students[student_id]["name"] = new_name
        elif choice == "2":
            new_age = int(input("Enter new age: "))
            students[student_id]["age"] = new_age
        elif choice == "3":
            new_class = input("Enter new class: ").strip()
            students[student_id]["class"] = new_class
        elif choice == "4":
            new_status = input("Is the student active? (yes/no): ").strip().lower()
            if new_status == "yes":
                students[student_id]["active"] = True
            elif new_status == "no":
                students[student_id]["active"] = False
            else:
                print("Please enter yes or no.")
                return
        else:
            print("Invalid option!")
            return
        save_to_json()
        print("\nStudent information updated successfully!")
    except ValueError:
        print("Please enter a valid number.")



def search_by_class():
    student_class = input("Enter class to search: ").strip().lower()
    found = False
    print("\nStudents in this class:")
    print(f"{'ID':<8} {'Name':<20} {'Age':<8} {'Active':<8}")
    print("=" * 50)
    for student_id, info in students.items():
        if info["class"].lower() == student_class:
            print(
                f"{student_id:<8} "
                f"{info['name']:<20} "
                f"{info['age']:<8} "
                f"{str(info['active']):<8}"
            )
            found = True
    if not found:
        print("No students found in this class.")




def active_students():
    found = False
    print("\n--- Active Students ---")
    print(f"{'ID':<8} {'Name':<20} {'Age':<8} {'Class':<8}")
    print("=" * 48)
    for student_id, info in students.items():
        if info["active"] == True:
            print(
                f"{student_id:<8} "
                f"{info['name']:<20} "
                f"{info['age']:<8} "
                f"{info['class']:<8}"
            )
            found = True
    if not found:
        print("There are no active students.")


def inactive_students():
    found = False
    print("\n--- Inactive Students ---")
    print(f"{'ID':<8} {'Name':<20} {'Age':<8} {'Class':<8}")
    print("=" * 48)
    for student_id, info in students.items():
        if info["active"] == False:
            print(
                f"{student_id:<8} "
                f"{info['name']:<20} "
                f"{info['age']:<8} "
                f"{info['class']:<8}"
            )
            found = True
    if not found:
        print("There are no inactive students.")

def school_statistics():
    total_students = 0
    active_students_count = 0
    inactive_students_count = 0
    for student_id, info in students.items():
        total_students = total_students + 1
        if info["active"] == True:
            active_students_count = active_students_count + 1
        else:
            inactive_students_count = inactive_students_count + 1
    print("\n================================")
    print("       SCHOOL STATISTICS")
    print("================================")
    print(f"Total Students:    {total_students}")
    print(f"Active Students:   {active_students_count}")
    print(f"Inactive Students: {inactive_students_count}")
    print("================================")

def class_statistics():
    seventh = 0
    eighth = 0
    ninth = 0
    tenth = 0
    eleventh = 0
    twelfth = 0
    for student_id, info in students.items():
        if info["class"] == "7th":
            seventh = seventh + 1
        elif info["class"] == "8th":
            eighth = eighth + 1
        elif info["class"] == "9th":
            ninth = ninth + 1
        elif info["class"] == "10th":
            tenth = tenth + 1
        elif info["class"] == "11th":
            eleventh = eleventh + 1
        elif info["class"] == "12th":
            twelfth = twelfth + 1
    print("\n--- Students by Class ---")
    print(f"7th Class:  {seventh}")
    print(f"8th Class:  {eighth}")
    print(f"9th Class:  {ninth}")
    print(f"10th Class: {tenth}")
    print(f"11th Class: {eleventh}")
    print(f"12th Class: {twelfth}")

initialize_json()


TEACHER_JSON_FILE = os.path.join(BASE_DIR, "teachers.json")



teachers = {}

def save_teachers_to_json():
    with open(TEACHER_JSON_FILE, mode="w", encoding="utf-8") as file:
        json.dump(teachers, file, indent=4)


def initialize_teachers_json():
    global teachers
    if not os.path.exists(TEACHER_JSON_FILE):
        save_teachers_to_json()
    else:
        with open(TEACHER_JSON_FILE, mode="r", encoding="utf-8") as file:
            loaded_data = json.load(file)
            teachers = {int(k): v for k, v in loaded_data.items()}
def search_teacher_by_id():
    try:
        teacher_id = int(input("Enter teacher ID: "))
        if teacher_id in teachers:
            teacher = teachers[teacher_id]
            print("\n================================")
            print("        TEACHER INFORMATION")
            print("================================")
            print(f"ID:         {teacher_id}")
            print(f"Name:       {teacher['name']}")
            print(f"Age:        {teacher['age']}")
            print(f"Subject:    {teacher['subject']}")
            print(f"Class:      {teacher['class']}")
            print(f"Experience: {teacher['experience']} years")
            print(f"Phone:      {teacher['phone']}")
            print(f"Active:     {teacher['active']}")
            print("================================")
        else:
            print("Teacher ID not found!")
    except ValueError:
        print("Please enter a valid numeric ID.")

def add_teacher():
    try:
        teacher_id = int(input("Enter teacher ID: "))
        if teacher_id in teachers:
            print("A teacher with this ID already exists!")
            return
        teacher_name = input("Enter teacher name: ").strip()
        teacher_age = int(input("Enter teacher age: "))
        teacher_subject = input("Enter subject: ").strip()
        teacher_class = input("Enter class: ").strip()
        teacher_experience = int(
            input("Enter years of experience: ")
        )
        teacher_phone = input("Enter phone number: ").strip()
        teacher_active = (
            input("Is the teacher active? (yes/no): ")
            .strip()
            .lower()
            == "yes"
        )
        teachers[teacher_id] = {
            "name": teacher_name,
            "age": teacher_age,
            "subject": teacher_subject,
            "class": teacher_class,
            "experience": teacher_experience,
            "phone": teacher_phone,
            "active": teacher_active
        }
        save_teachers_to_json()
        print("Teacher added successfully!")
    except ValueError:
        print("ID, age and experience must be numbers.")
def all_teachers():
    if len(teachers) == 0:
        print("There are no teachers.")
        return
    print(
        f"\n{'ID':<8}"
        f"{'Name':<20}"
        f"{'Subject':<18}"
        f"{'Class':<10}"
        f"{'Active':<10}"
    )
    print("=" * 66)
    for teacher_id, info in teachers.items():
        print(
            f"{teacher_id:<8}"
            f"{info['name']:<20}"
            f"{info['subject']:<18}"
            f"{info['class']:<10}"
            f"{str(info['active']):<10}"
        )


def search_teacher_by_name():
    teacher_name = input(
        "Enter teacher name: "
    ).strip().lower()
    found = False
    for teacher_id, info in teachers.items():
        if info["name"].lower() == teacher_name:
            print("\n================================")
            print("        TEACHER FOUND")
            print("================================")
            print(f"ID:         {teacher_id}")
            print(f"Name:       {info['name']}")
            print(f"Age:        {info['age']}")
            print(f"Subject:    {info['subject']}")
            print(f"Class:      {info['class']}")
            print(f"Experience: {info['experience']} years")
            print(f"Phone:      {info['phone']}")
            print(f"Active:     {info['active']}")
            print("================================")
            found = True
    if not found:
        print("Teacher not found!")
    

def delete_teacher():
    try:
        teacher_id = int(
            input("Enter teacher ID to delete: ")
        )
        if teacher_id in teachers:
            del teachers[teacher_id]
            save_teachers_to_json()
            print("Teacher deleted successfully!")
        else:
            print("Teacher ID not found!")
    except ValueError:
        print("Please enter a valid teacher ID.")


def update_teacher():
    try:
        teacher_id = int(
            input("Enter teacher ID to update: ")
        )
        if teacher_id not in teachers:
            print("Teacher ID not found!")
            return
        teacher = teachers[teacher_id]
        print("\nCurrent Teacher Information:")
        print(f"Name:       {teacher['name']}")
        print(f"Age:        {teacher['age']}")
        print(f"Subject:    {teacher['subject']}")
        print(f"Class:      {teacher['class']}")
        print(f"Experience: {teacher['experience']}")
        print(f"Phone:      {teacher['phone']}")
        print(f"Active:     {teacher['active']}")
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Subject")
        print("4. Class")
        print("5. Experience")
        print("6. Phone")
        print("7. Active Status")
        choice = input("Choose an option: ")
        if choice == "1":
            teacher["name"] = input(
                "Enter new name: "
            ).strip()
        elif choice == "2":
            teacher["age"] = int(
                input("Enter new age: ")
            )
        elif choice == "3":
            teacher["subject"] = input(
                "Enter new subject: "
            ).strip()
        elif choice == "4":
            teacher["class"] = input(
                "Enter new class: "
            ).strip()
        elif choice == "5":
            teacher["experience"] = int(
                input("Enter new experience: ")
            )
        elif choice == "6":
            teacher["phone"] = input(
                "Enter new phone number: "
            ).strip()
        elif choice == "7":
            status = input(
                "Is teacher active? (yes/no): "
            ).strip().lower()
            if status == "yes":
                teacher["active"] = True
            elif status == "no":
                teacher["active"] = False
            else:
                print("Please enter yes or no.")
                return
        else:
            print("Invalid option!")
            return
        save_teachers_to_json()
        print("Teacher information updated successfully!")
    except ValueError:
        print("Please enter valid information.")


def active_teachers():
    found = False
    print("\n--- Active Teachers ---")
    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Subject':<18}"
        f"{'Class':<10}"
    )
    print("=" * 56)
    for teacher_id, info in teachers.items():
        if info["active"] == True:
            print(
                f"{teacher_id:<8}"
                f"{info['name']:<20}"
                f"{info['subject']:<18}"
                f"{info['class']:<10}"
            )
            found = True
    if not found:
        print("There are no active teachers.")



def inactive_teachers():
    found = False
    print("\n--- Inactive Teachers ---")
    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Subject':<18}"
        f"{'Class':<10}"
    )
    print("=" * 56)
    for teacher_id, info in teachers.items():
        if info["active"] == False:
            print(f"{teacher_id:<8}{info['name']:<20}{info['subject']:<18}{info['class']:<10}")
            found = True
    if not found:
        print("There are no inactive teachers.")


def search_teacher_by_subject():
    subject = input(
        "Enter subject: "
    ).strip().lower()
    found = False
    print("\nTeachers of this subject:")
    for teacher_id, info in teachers.items():
        if info["subject"].lower() == subject:
            print(
    f"ID: {teacher_id} | Name: {info['name']} | "
    f"Subject: {info['subject']} | Class: {info['class']}"
                )
            found = True
    if not found:
        print("No teacher found for this subject.")


def student_contact():
    try:
        student_id = int(
            input("Enter student ID: ")
        )
        if student_id in students:
            if "phone" in students[student_id]:
                print(
                    f"Student Name: "
                    f"{students[student_id]['name']}"
                )
                print(
                    f"Phone Number: "
                    f"{students[student_id]['phone']}"
                )
            else:
                print("Phone number is not available.")
        else:
            print("Student ID not found!")
    except ValueError:
        print("Please enter a valid ID.")

def update_student_attendance():
    try:
        student_id = int(
            input("Enter student ID: ")
        )
        if student_id not in students:
            print("Student not found!")
            return
        attendance = float(
            input("Enter attendance percentage: ")
        )
        if attendance < 0 or attendance > 100:
            print("Attendance must be between 0 and 100.")
            return
        students[student_id]["attendance"] = attendance
        save_to_json()
        print("Attendance updated successfully!")
    except ValueError:
        print("Please enter a valid number.")

def show_student_attendance():
    try:
        student_id = int(
            input("Enter student ID: ")
        )
        if student_id in students:
            if "attendance" in students[student_id]:
                print(
                    f"Student: "
                    f"{students[student_id]['name']}"
                )
                print(
                    f"Attendance: "
                    f"{students[student_id]['attendance']}%"
                )
            else:
                print("Attendance information is not available.")
        else:
            print("Student not found!")
    except ValueError:
        print("Please enter a valid ID.")

def update_student_marks():
    try:
        student_id = int(
            input("Enter student ID: ")
        )
        if student_id not in students:
            print("Student not found!")
            return
        marks = float(
            input("Enter marks percentage: ")
        )
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
        students[student_id]["marks"] = marks
        save_to_json()
        print("Marks updated successfully!")
    except ValueError:
        print("Please enter valid marks.")



def show_student_result():
    try:
        student_id = int(
            input("Enter student ID: ")
        )
        if student_id not in students:
            print("Student not found!")
            return
        student = students[student_id]
        print("\n================================")
        print("          STUDENT RESULT")
        print("================================")
        print(f"Name:       {student['name']}")
        print(f"Class:      {student['class']}")
        if "marks" in student:
            print(f"Marks:      {student['marks']}%")
            if student["marks"] >= 80:
                print("Grade:      A")
            elif student["marks"] >= 70:
                print("Grade:      B")
            elif student["marks"] >= 60:
                print("Grade:      C")
            elif student["marks"] >= 50:
                print("Grade:      D")
            else:
                print("Grade:      F")
        else:
            print("Marks are not available.")
        print("================================")
    except ValueError:
        print("Please enter a valid ID.")


def students_with_low_attendance():
    found = False
    print("\n--- Students With Low Attendance ---")
    for student_id, info in students.items():
        if "attendance" in info:
            if info["attendance"] < 75:
                print(
                    f"ID: {student_id} | "
                    f"Name: {info['name']} | "
                    f"Attendance: {info['attendance']}%"
                )
                found = True
    if not found:
        print("No students have attendance below 75%.")

def students_with_unpaid_fees():
    found = False
    print("\n--- Students With Unpaid Fees ---")
    for student_id, info in students.items():
        if "fees_paid" in info:
            if info["fees_paid"] == False:
                print(
                    f"ID: {student_id} | "
                    f"Name: {info['name']} | "
                    f"Class: {info['class']}"
                )
                found = True
    if not found:
        print("All students have paid their fees.")



def school_overall_statistics():
    total_students = len(students)
    total_teachers = len(teachers)
    active_students_count = 0
    active_teachers_count = 0
    for student_id, info in students.items():
        if info["active"] == True:
            active_students_count = (
                active_students_count + 1
            )
    for teacher_id, info in teachers.items():
        if info["active"] == True:
            active_teachers_count = (
                active_teachers_count + 1
            )
    print("\n========================================")
    print("       SCHOOL OVERALL STATISTICS")
    print("========================================")
    print(f"Total Students:       {total_students}")
    print(f"Active Students:      {active_students_count}")
    print(f"Total Teachers:       {total_teachers}")
    print(f"Active Teachers:      {active_teachers_count}")
    print("========================================")
initialize_teachers_json()
while True:
    print("\n")
    print("=" * 50)
    print("          SCHOOL MANAGEMENT SYSTEM")
    print("=" * 50)
    print("\n--- STUDENT MANAGEMENT ---")
    print("1.  Search student by ID")
    print("2.  Add a new student")
    print("3.  Print all students")
    print("4.  Search student by name")
    print("5.  Delete student")
    print("6.  Update student")
    print("7.  Search students by class")
    print("8.  Show active students")
    print("9.  Show inactive students")
    print("10. School statistics")
    print("11. Class statistics")
    print("\n--- TEACHER MANAGEMENT ---")
    print("12. Search teacher by ID")
    print("13. Add a new teacher")
    print("14. Print all teachers")
    print("15. Search teacher by name")
    print("16. Delete teacher")
    print("17. Update teacher")
    print("18. Show active teachers")
    print("19. Show inactive teachers")
    print("20. Search teacher by subject")
    print("\n--- STUDENT ACADEMIC INFORMATION ---")
    print("21. Update student marks")
    print("22. Show student result")
    print("\n--- ATTENDANCE MANAGEMENT ---")
    print("23. Update student attendance")
    print("24. Show student attendance")
    print("25. Students with low attendance")
    print("\n--- STUDENT CONTACT ---")
    print("26. Show student contact")
    print("\n--- FEES MANAGEMENT ---")
    print("27. Students with unpaid fees")
    print("\n--- SCHOOL REPORT ---")
    print("28. School overall statistics")
    print("\n29. Exit")
    print("=" * 50)
    try:
        choice = int(
            input("Choose any option from the list: ")
        )
        if choice == 1:
            search_by_id()
        elif choice == 2:
            new_student()
        elif choice == 3:
            all_students()
        elif choice == 4:
            search_by_name()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            update_student()
        elif choice == 7:
            search_by_class()
        elif choice == 8:
            active_students()
        elif choice == 9:
            inactive_students()
        elif choice == 10:
            school_statistics()
        elif choice == 11:
            class_statistics()
        elif choice == 12:
            search_teacher_by_id()
        elif choice == 13:
            add_teacher()
        elif choice == 14:
            all_teachers()
        elif choice == 15:
            search_teacher_by_name()
        elif choice == 16:
            delete_teacher()
        elif choice == 17:
            update_teacher()
        elif choice == 18:
            active_teachers()
        elif choice == 19:
            inactive_teachers()
        elif choice == 20:
            search_teacher_by_subject()

        elif choice == 21:
            update_student_marks()
        elif choice == 22:
            show_student_result()
        elif choice == 23:
            update_student_attendance()
        elif choice == 24:
            show_student_attendance()
        elif choice == 25:
            students_with_low_attendance()

        elif choice == 26:
            student_contact()

        elif choice == 27:
            students_with_unpaid_fees()
        elif choice == 28:
            school_overall_statistics()
        elif choice == 29:
            exit_system()
            break
        else:
            print(
                "Invalid choice! "
                "Choose a number between 1 and 29."
            )
    except ValueError:
        print("Please enter a valid number.")