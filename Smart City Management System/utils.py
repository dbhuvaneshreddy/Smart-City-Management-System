from datetime import datetime


class Utility:

    citizen_counter = 100
    employee_counter = 100
    complaint_counter = 1000

    @staticmethod
    def generate_citizen_id():

        Utility.citizen_counter += 1

        return f"C{Utility.citizen_counter}"

    @staticmethod
    def generate_employee_id():

        Utility.employee_counter += 1

        return f"E{Utility.employee_counter}"

    @staticmethod
    def generate_complaint_id():

        Utility.complaint_counter += 1

        return f"CMP{Utility.complaint_counter}"

    @staticmethod
    def current_date():

        return datetime.now().strftime("%d-%m-%Y")

    @staticmethod
    def current_time():

        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def line():

        print("=" * 60)

    @staticmethod
    def heading(title):

        Utility.line()
        print(title.center(60))
        Utility.line()