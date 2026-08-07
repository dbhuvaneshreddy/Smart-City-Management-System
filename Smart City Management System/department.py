class Department:

    department_count = 0

    def __init__(self,
                 department_id,
                 department_name):

        Department.department_count += 1

        self.__department_id = department_id
        self.__department_name = department_name
        self.__employees = []

    @property
    def department_id(self):
        return self.__department_id

    @property
    def department_name(self):
        return self.__department_name

    def add_employee(self, employee):

        self.__employees.append(employee)

        print(employee.name, "added to", self.department_name)

    def remove_employee(self, employee_id):

        for employee in self.__employees:

            if employee.person_id == employee_id:

                self.__employees.remove(employee)

                print("Employee Removed")
                return

        print("Employee Not Found")

    def total_employees(self):

        return len(self.__employees)

    def display(self):

        print("\n========== Department ==========")
        print("Department ID :", self.department_id)
        print("Department    :", self.department_name)
        print("Employees     :", len(self.__employees))