class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def details(self):
        return {
            'name': self.name,
            'age': self.age,
            'department': self.department,
            'salary': self.salary
        }

def add_employee(employees):
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
                continue
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            employees[emp_id] = Employee(emp_id, name, age, department, salary)
            print("Employee added successfully!\n")
            break
        except ValueError:
            print("Invalid input! Please enter numbers for ID, Age, and Salary.")

def view_employees(employees):
    if not employees:
        print("No employees available.\n")
        return
    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Department':<15}{'Salary':<10}")
    print("-" * 50)
    for emp_id, emp in employees.items():
        print(f"{emp_id:<6}{emp.name:<15}{emp.age:<6}{emp.department:<15}{emp.salary:<10}")

def search_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee found:")
            print(f"Name: {emp.name}")
            print(f"Age: {emp.age}")
            print(f"Department: {emp.department}")
            print(f"Salary: {emp.salary}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid ID! Please enter a number.")

def main_menu():
    # Initialize with some sample employees
    employees = {
        101: Employee(101, 'Sujal', 22, 'HR', 50000),
        102: Employee(102, 'Ram', 32, 'IT', 60000),
        103: Employee(103, 'Amit', 29, 'Finance', 55000)
    }
    while True:
        print("------EMPLOYEE MANAGEMENT SYSTEM------")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
            print()
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the Employee Management System!\n")
            break
        else:
            print("Invalid choice! Please select from 1-4.")

if __name__ == "__main__":
    main_menu()
