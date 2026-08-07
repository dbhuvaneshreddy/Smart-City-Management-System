from person import Person


class Employee(Person):

    employee_count = 0

    def __init__(self,
                 person_id,
                 name,
                 age,
                 gender,
                 phone,
                 address,
                 department,
                 salary):

        super().__init__(
            person_id,
            name,
            age,
            gender,
            phone,
            address
        )

        Employee.employee_count += 1

        self.__department = department
        self.__salary = salary

    @property
    def department(self):
        return self.__department

    @property
    def salary(self):
        return self.__salary

    def increase_salary(self, percent):

        self.__salary += self.__salary * percent / 100

    def display(self):

        print("\n========== Employee ==========")
        print("Employee ID :", self.person_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      :", self.salary)