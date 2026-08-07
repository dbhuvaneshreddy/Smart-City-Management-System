class Zone:

    zone_count = 0

    def __init__(self,
                 zone_id,
                 zone_name):

        Zone.zone_count += 1

        self.__zone_id = zone_id
        self.__zone_name = zone_name
        self.__citizens = []
        self.__departments = []

    @property
    def zone_id(self):
        return self.__zone_id

    @property
    def zone_name(self):
        return self.__zone_name

    def add_citizen(self, citizen):

        self.__citizens.append(citizen)

    def add_department(self, department):

        self.__departments.append(department)

    def total_citizens(self):

        return len(self.__citizens)

    def total_departments(self):

        return len(self.__departments)

    def display(self):

        print("\n========== Zone ==========")
        print("Zone ID      :", self.zone_id)
        print("Zone Name    :", self.zone_name)
        print("Citizens     :", len(self.__citizens))
        print("Departments  :", len(self.__departments))