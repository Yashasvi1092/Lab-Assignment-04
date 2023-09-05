class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = [
            Employee("161E90", "Raman", 41, 56000),
            Employee("161F91", "Himadri", 38, 67500),
            Employee("161F99", "Jaya", 51, 82100),
            Employee("171E20", "Tejas", 30, 55000),
            Employee("171G30", "Ajay", 45, 44000)
        ]

    def search_employee(self, search_parameter, value):
        results = []
        for employee in self.employees:
            if search_parameter == "1":  # Age
                if employee.age == int(value):
                    results.append(employee)
            elif search_parameter == "2":  # Name
                if employee.name.lower() == value.lower():
                    results.append(employee)
            elif search_parameter == "3":  # Salary
                operator, salary_value_str = value.split()
                salary_value = int(salary_value_str)
                if operator == ">":
                    if employee.salary > salary_value:
                        results.append(employee)
                elif operator == "<":
                    if employee.salary < salary_value:
                        results.append(employee)
                elif operator == ">=":
                    if employee.salary >= salary_value:
                        results.append(employee)
                elif operator == "<=":
                    if employee.salary <= salary_value:
                        results.append(employee)
        return results

def main():
    employee_table = EmployeeTable()

    print("Employee Table Search")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    search_parameter = input("Enter your choice: ")
    search_value = input("Enter the search value: ")

    results = employee_table.search_employee(search_parameter, search_value)

    if results:
        print("Employee(s) found:")
        for employee in results:
            print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No employees found matching the criteria.")

if __name__ == "__main__":
    main()
