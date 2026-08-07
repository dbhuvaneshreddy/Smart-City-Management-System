class Report:

    @staticmethod
    def city_summary(city):

        print("\n========== CITY SUMMARY ==========")

        print("City Name       :", city.city_name)
        print("Mayor           :", city.mayor)
        print("Zones           :", city.total_zones())
        print("Departments     :", city.total_departments())
        print("Citizens        :", city.total_citizens())
        print("Employees       :", city.total_employees())

    @staticmethod
    def citizen_report(citizen):

        print("\n========== CITIZEN REPORT ==========")

        citizen.display()

    @staticmethod
    def employee_report(employee):

        print("\n========== EMPLOYEE REPORT ==========")

        employee.display()

    @staticmethod
    def vehicle_report(vehicle):

        print("\n========== VEHICLE REPORT ==========")

        vehicle.display()

    @staticmethod
    def complaint_report(complaint):

        print("\n========== COMPLAINT REPORT ==========")

        complaint.display()

    @staticmethod
    def electricity_report(connection):

        print("\n========== ELECTRICITY REPORT ==========")

        connection.display()

    @staticmethod
    def water_report(connection):

        print("\n========== WATER REPORT ==========")

        connection.display()

    @staticmethod
    def hospital_report(hospital):

        hospital.hospital_report()

    @staticmethod
    def traffic_report(traffic):

        traffic.traffic_report()

    @staticmethod
    def parking_report(parking):

        parking.parking_report()