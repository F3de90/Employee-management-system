# Employee Management System (Employee ID, Name, Department)

employees = [
    (101, "Federico", "Order Team"),
    (102, "Alice", "Customer Service"),
    (104, "Flavio", "System Analyst"),
    (105, "Carla", "Logistic"),
    (106, "Alessandra", "Logistic"),
    (107, "Rebecca", "Facility"),
    (108, "David", "Logistic"),
    (109, "Jimmy", "Management"),
    (110, "Carlos", "Customer Service"),
    (111, "Frank", "Order Team"),   
    
]

while True:
    print("\n1. Display Employee")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Display all employees
        print("\nEmployee Records:")
        print("-----------------")
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}")
        print("-----------------\n")

    elif choice == "2":  # Search employee by ID
        search_id = input("Enter Employee ID to Search: ")
        if search_id.isdigit(): #isdigit is a function included in Python that looks for numbers
            search_id = int(search_id)
            found = False
            for employee in employees:
                if employee[0] == search_id:
                    print(f"\nemployee Found: ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}\n")
                    found = True
                    break
            if not found:
                print("\nemployee Not Found!\n")
        else:
            print("\nInvalid Input! Please enter a valid numeric ID.\n")

    elif choice == "3":  # Add a new employee
        employee_id = input("Enter Employee ID: ")
        if employee_id.isdigit():
            employee_id = int(employee_id)
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ").upper()

            employees.append((employee_id, name, department))  # Append a new tuple
            print("\nStudent Added Successfully!\n")
        else:
            print("\nInvalid Input! Employee ID must be a number.\n")
            
            
    elif choice == "4":  # Remove an employee
        employee_id = input("Enter Employee ID: ")
        if employee_id.isdigit():
            employee_id = int(employee_id)
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ").upper()
            employees.remove((employee_id, name, department)) # Removed the tuple
            print("\nStudent Removed Successfully!\n")
        else:
            print("\nInvalid Input! Employee ID must be a number.\n")
            
            
            

    elif choice == "5":  # Exit the program
        print("Exiting Program...")
        break

    else:
        print("\nInvalid Choice! Try Again.\n")