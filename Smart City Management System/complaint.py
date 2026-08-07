from datetime import datetime


class Complaint:

    complaint_counter = 1000

    def __init__(self,
                 citizen,
                 department,
                 title,
                 description):

        Complaint.complaint_counter += 1

        self.__complaint_id = Complaint.complaint_counter
        self.__citizen = citizen
        self.__department = department
        self.__title = title
        self.__description = description
        self.__status = "Pending"
        self.__created_date = datetime.now()

    @property
    def complaint_id(self):
        return self.__complaint_id

    @property
    def status(self):
        return self.__status

    @property
    def department(self):
        return self.__department

    def assign(self):

        self.__status = "Assigned"

        print("Complaint Assigned")

    def resolve(self):

        self.__status = "Resolved"

        print("Complaint Resolved")

    def reopen(self):

        self.__status = "Reopened"

    def display(self):

        print("\n========== COMPLAINT ==========")
        print("Complaint ID :", self.__complaint_id)
        print("Citizen      :", self.__citizen.name)
        print("Department   :", self.__department)
        print("Title        :", self.__title)
        print("Description  :", self.__description)
        print("Status       :", self.__status)
        print("Created On   :", self.__created_date.strftime("%d-%m-%Y %H:%M"))