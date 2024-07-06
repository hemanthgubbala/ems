import mysql.connector

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="emp"
)

cursor = con.cursor()

# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None

# Function to add an employee
def add_employee():
    employee_id = input("Enter Employee Id: ")
    if check_employee(employee_id):
        print("Employee already exists. Please try again.")
        return
    
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Post: ")
    salary = input("Enter Employee Salary: ")

    sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
    data = (employee_id, name, position, salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to remove an employee
def remove_employee():
    employee_id = input("Enter Employee Id: ")
    if not check_employee(employee_id):
        print("Employee does not exist. Please try again.")
        return
    
    sql = 'DELETE FROM employees WHERE id=%s'
    data = (employee_id,)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to promote an employee
def promote_employee():
    employee_id = input("Enter Employee's Id: ")
    if not check_employee(employee_id):
        print("Employee does not exist. Please try again.")
        return
    
    try:
        amount = float(input("Enter increase in Salary: "))

        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        cursor.execute(sql_select, (employee_id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, employee_id))
        con.commit()
        print("Employee Promoted Successfully")

    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()

# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print(f"Employee Id : {employee[0]}")
            print(f"Employee Name : {employee[1]}")
            print(f"Employee Post : {employee[2]}")
            print(f"Employee Salary : {employee[3]}")
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to display the menu
def menu():
    options = {
        '1': add_employee,
        '2': remove_employee,
        '3': promote_employee,
        '4': display_employees,
        '5': exit_program
    }

    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
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
