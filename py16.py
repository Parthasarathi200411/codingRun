def filter_employees(employees, min_salary, max_salary):
    filtered_employees = []
    for name, job_title, salary in employees:
        if min_salary <= salary <= max_salary:
            filtered_employees.append((name, job_title))
    filtered_employees.sort(key=lambda x: x[1], reverse=True)  # Sorting by salary (largest first)
    return filtered_employees

def read_file(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, job_title, salary = line.strip().split(',')
                salary = int(salary.strip())
                employees.append((name.strip(), job_title.strip(), salary))
        return employees
    except FileNotFoundError:
        return None

def main():
    while True:
        filename = input("Enter the filename: ")
        employees = read_file(filename)
        if employees:
            break
        else:
            print("File not found. Please try again.")

    print("List of tuples:", employees)

    while True:
        try:
            min_salary = int(input("Enter the minimum salary: "))
            max_salary = int(input("Enter the maximum salary: "))
            if min_salary < 0 or max_salary < 0:
                print("Salary cannot be negative.")
                continue
            if min_salary > max_salary:
                min_salary, max_salary = max_salary, min_salary
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    filtered_employees = filter_employees(employees, min_salary, max_salary)
    
    if filtered_employees:
        print("\nEmployees with salaries between {} and {}:".format(min_salary, max_salary))
        for name, job_title in filtered_employees:
            print("{:<20} {:<20}".format(name, job_title))
    else:
        print("No employees found within the specified salary range.")

    while True:
        choice = input("Do you wish to quit? (yes/no): ").lower()
        if choice in ('yes', 'no'):
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if choice == 'yes':
        print("Exiting program.")
        return
    else:
        main()

if __name__ == "__main__":
    main()
