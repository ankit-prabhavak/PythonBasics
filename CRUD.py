import sqlite3

# Create a connection to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create an Employee table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    )
''')

# Function to add an employee
def add_employee(name, position, salary):
    cursor.execute('''
        INSERT INTO employees (name, position, salary)
        VALUES (?, ?, ?)
    ''', (name, position, salary))
    conn.commit()
    print(f"Employee {name} added successfully!")

# Function to view all employees
def view_employees():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    if employees:
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")
    else:
        print("No employees found.")

# Function to update an employee's details
def update_employee(employee_id, name, position, salary):
    cursor.execute('''
        UPDATE employees
        SET name = ?, position = ?, salary = ?
        WHERE id = ?
    ''', (name, position, salary, employee_id))
    conn.commit()
    print(f"Employee ID {employee_id} updated successfully!")

# Function to delete an employee
def delete_employee(employee_id):
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    print(f"Employee ID {employee_id} deleted successfully!")

# Main Menu
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            add_employee(name, position, salary)
        
        elif choice == '2':
            view_employees()
        
        elif choice == '3':
            employee_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name: ")
            position = input("Enter new position: ")
            salary = float(input("Enter new salary: "))
            update_employee(employee_id, name, position, salary)
        
        elif choice == '4':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_id)
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()

# Close the database connection when done
conn.close()
