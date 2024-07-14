import mysql.connector
from datetime import datetime

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="school"
)

cursor = con.cursor()

# Function to check if a student exists
def check_student(student_id):
    sql = 'SELECT * FROM students WHERE id=%s'
    cursor.execute(sql, (student_id,))
    return cursor.fetchone() is not None

# Function to add a student
def add_student():
    student_id = input("Enter Student Id: ")
    if check_student(student_id):
        print("Student already exists. Please try again.")
        return
    
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    age = input("Enter Student Age: ")
    address = input("Enter Student Address: ")
    phone = input("Enter Student Phone Number: ")
    email = input("Enter Student Email: ")
    department = input("Enter Student Department: ")

    sql = 'INSERT INTO students (id, name, grade, age, address, phone, email, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    data = (student_id, name, grade, age, address, phone, email, department)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Student Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to remove a student
def remove_student():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return
    
    sql = 'DELETE FROM students WHERE id=%s'
    data = (student_id,)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Student Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to promote a student
def promote_student():
    student_id = input("Enter Student's Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return
    
    try:
        new_grade = input("Enter new Grade: ")

        sql_update = 'UPDATE students SET grade=%s WHERE id=%s'
        cursor.execute(sql_update, (new_grade, student_id))
        con.commit()
        print("Student Promoted Successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        con.rollback()

# Function to update student details
def update_student():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return
    
    name = input("Enter new Student Name: ")
    grade = input("Enter new Student Grade: ")
    age = input("Enter new Student Age: ")
    address = input("Enter new Student Address: ")
    phone = input("Enter new Student Phone Number: ")
    email = input("Enter new Student Email: ")
    department = input("Enter new Student Department: ")

    sql_update = 'UPDATE students SET name=%s, grade=%s, age=%s, address=%s, phone=%s, email=%s, department=%s WHERE id=%s'
    data = (name, grade, age, address, phone, email, department, student_id)
    try:
        cursor.execute(sql_update, data)
        con.commit()
        print("Student Details Updated Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to search for a student
def search_student():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return
    
    sql = 'SELECT * FROM students WHERE id=%s'
    cursor.execute(sql, (student_id,))
    student = cursor.fetchone()
    if student:
        print(f"Student Id : {student[0]}")
        print(f"Student Name : {student[1]}")
        print(f"Student Grade : {student[2]}")
        print(f"Student Age : {student[3]}")
        print(f"Student Address : {student[4]}")
        print(f"Student Phone : {student[5]}")
        print(f"Student Email : {student[6]}")
        print(f"Student Department : {student[7]}")
        print("------------------------------------")

# Function to display all students
def display_students():
    try:
        sql = 'SELECT * FROM students'
        cursor.execute(sql)
        students = cursor.fetchall()
        for student in students:
            print(f"Student Id : {student[0]}")
            print(f"Student Name : {student[1]}")
            print(f"Student Grade : {student[2]}")
            print(f"Student Age : {student[3]}")
            print(f"Student Address : {student[4]}")
            print(f"Student Phone : {student[5]}")
            print(f"Student Email : {student[6]}")
            print(f"Student Department : {student[7]}")
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to mark attendance
def mark_attendance():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return

    date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Attendance Status (Present/Absent): ")

    sql = 'INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)'
    data = (student_id, date, status)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Attendance Marked Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to record grades
def record_grades():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return

    subject = input("Enter Subject: ")
    grade = input("Enter Grade: ")

    sql = 'INSERT INTO grades (student_id, subject, grade) VALUES (%s, %s, %s)'
    data = (student_id, subject, grade)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Grade Recorded Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to enroll in a course
def enroll_course():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return

    course_id = input("Enter Course Id: ")

    sql = 'INSERT INTO course_enrollment (student_id, course_id) VALUES (%s, %s)'
    data = (student_id, course_id)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Course Enrolled Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to record fees payment
def record_fees():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return

    amount = input("Enter Payment Amount: ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = 'INSERT INTO fees (student_id, amount, date) VALUES (%s, %s, %s)'
    data = (student_id, amount, date)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Fees Payment Recorded Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to generate student report
def generate_student_report():
    student_id = input("Enter Student Id: ")
    if not check_student(student_id):
        print("Student does not exist. Please try again.")
        return

    print("\nStudent Details:")
    search_student(student_id)

    print("\nAttendance:")
    sql = 'SELECT * FROM attendance WHERE student_id=%s'
    cursor.execute(sql, (student_id,))
    attendance_records = cursor.fetchall()
    for record in attendance_records:
        print(f"Date: {record[1]}, Status: {record[2]}")

    print("\nGrades:")
    sql = 'SELECT * FROM grades WHERE student_id=%s'
    cursor.execute(sql, (student_id,))
    grades_records = cursor.fetchall()
    for record in grades_records:
        print(f"Subject: {record[1]}, Grade: {record[2]}")

    print("\nCourses Enrolled:")
    sql = 'SELECT * FROM course_enrollment WHERE student_id=%s'
    cursor.execute(sql, (student_id,))
    course_records = cursor.fetchall()
    for record in course_records:
        print(f"Course Id: {record[1]}")

    print("\nFees Payments:")
    sql = 'SELECT * FROM fees WHERE student_id=%s'
    cursor.execute(sql, (student_id,))
    fees_records = cursor.fetchall()
    for record in fees_records:
        print(f"Amount: {record[1]}, Date: {record[2]}")

# Function to display the menu
def menu():
    options = {
        '1': add_student,
        '2': remove_student,
        '3': promote_student,
        '4': update_student,
        '5': search_student,
        '6': display_students,
        '7': mark_attendance,
        '8': record_grades,
        '9': enroll_course,
        '10': record_fees,
        '11': generate_student_report,
        '12': exit_program
    }

    while True:
        print("\nWelcome to Student Management System")
        print("Press:")
        print("1 to Add Student")
        print("2 to Remove Student")
        print("3 to Promote Student")
        print("4 to Update Student Details")
        print("5 to Search for a Student")
        print("6 to Display Students")
        print("7 to Mark Attendance")
        print("8 to Record Grades")
        print("9 to Enroll in a Course")
        print("10 to Record Fees Payment")
        print("11 to Generate Student Report")
        print("12 to Exit")
        
        choice = input("Enter your Choice: ")

        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid Choice! Please try again.")

def exit_program():
    print("Exiting the program. Goodbye!")
    con.close()

if __name__ == "__main__":
    menu()
