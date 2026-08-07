from employee import Employee


class Admin(Employee):

    def __init__(self,
                 person_id,
                 name,
                 age,
                 gender,
                 phone,
                 address,
                 salary):

        super().__init__(
            person_id,
            name,
            age,
            gender,
            phone,
            address,
            "Administration",
            salary
        )

    def add_citizen(self,
                    city,
                    citizen):

        city.add_citizen(citizen)

    def remove_citizen(self,
                       city,
                       citizen_id):

        city.remove_citizen(citizen_id)

    def announce(self,
                 message):

        print("\nCITY ANNOUNCEMENT")
        print(message)

    def display(self):

        print("\n========== ADMIN ==========")
        print("Admin ID   :", self.person_id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Salary     :", self.salary)