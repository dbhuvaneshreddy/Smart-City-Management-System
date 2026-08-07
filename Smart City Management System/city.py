class City:

    def __init__(self,
                 city_name,
                 mayor):

        self.__city_name = city_name
        self.__mayor = mayor

        self.__zones = []
        self.__citizens = []
        self.__employees = []
        self.__departments = []

    @property
    def city_name(self):
        return self.__city_name

    @property
    def mayor(self):
        return self.__mayor

    def add_zone(self, zone):

        self.__zones.append(zone)

        print("Zone Added")

    def add_department(self, department):

        self.__departments.append(department)

        print("Department Added")

    def add_citizen(self, citizen):

        self.__citizens.append(citizen)

        print(citizen.name, "Registered")

    def add_employee(self, employee):

        self.__employees.append(employee)

        print(employee.name, "Joined City")

    def remove_citizen(self, citizen_id):

        for citizen in self.__citizens:

            if citizen.person_id == citizen_id:

                self.__citizens.remove(citizen)

                print("Citizen Removed")

                return

        print("Citizen Not Found")

    def search_citizen(self, citizen_id):

        for citizen in self.__citizens:

            if citizen.person_id == citizen_id:

                return citizen

        return None

    def search_employee(self, employee_id):

        for employee in self.__employees:

            if employee.person_id == employee_id:

                return employee

        return None

    def total_citizens(self):

        return len(self.__citizens)

    def total_employees(self):

        return len(self.__employees)

    def total_departments(self):

        return len(self.__departments)

    def total_zones(self):

        return len(self.__zones)

    def city_report(self):

        print("\n========== SMART CITY REPORT ==========")
        print("City Name       :", self.city_name)
        print("Mayor           :", self.mayor)
        print("Zones           :", self.total_zones())
        print("Departments     :", self.total_departments())
        print("Citizens        :", self.total_citizens())
        print("Employees       :", self.total_employees())

    def display_all_citizens(self):

        print("\n===== Citizens =====")

        if len(self.__citizens) == 0:
            print("No Citizens")
            return

        for citizen in self.__citizens:
            citizen.display()

    def display_all_employees(self):

        print("\n===== Employees =====")

        if len(self.__employees) == 0:
            print("No Employees")
            return

        for employee in self.__employees:
            employee.display()