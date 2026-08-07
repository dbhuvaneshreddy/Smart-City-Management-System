class SmartCityException(Exception):
    pass


class CitizenNotFoundException(SmartCityException):

    def __init__(self):

        super().__init__("Citizen Not Found")


class EmployeeNotFoundException(SmartCityException):

    def __init__(self):

        super().__init__("Employee Not Found")


class VehicleNotFoundException(SmartCityException):

    def __init__(self):

        super().__init__("Vehicle Not Found")


class SlotUnavailableException(SmartCityException):

    def __init__(self):

        super().__init__("Parking Slot Unavailable")


class ComplaintNotFoundException(SmartCityException):

    def __init__(self):

        super().__init__("Complaint Not Found")


class InvalidInputException(SmartCityException):

    def __init__(self):

        super().__init__("Invalid Input")


class DepartmentNotFoundException(SmartCityException):

    def __init__(self):

        super().__init__("Department Not Found")