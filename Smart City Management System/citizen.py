from person import Person


class Citizen(Person):

    citizen_count = 0

    def __init__(self,
                 person_id,
                 name,
                 age,
                 gender,
                 phone,
                 address):

        super().__init__(
            person_id,
            name,
            age,
            gender,
            phone,
            address
        )

        Citizen.citizen_count += 1

        self.__complaints = []
        self.__notifications = []

    def raise_complaint(self, complaint):

        self.__complaints.append(complaint)

        print("Complaint Registered Successfully")

    def view_complaints(self):

        if len(self.__complaints) == 0:
            print("No Complaints")
            return

        print("\nComplaint History")

        for complaint in self.__complaints:
            print("-", complaint)

    def add_notification(self, message):

        self.__notifications.append(message)

    def view_notifications(self):

        if len(self.__notifications) == 0:
            print("No Notifications")
            return

        print("\nNotifications")

        for notification in self.__notifications:
            print(notification)

    def display(self):

        print("\n========== Citizen ==========")
        print("Citizen ID :", self.person_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Phone      :", self.phone)
        print("Address    :", self.address)