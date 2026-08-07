class Garbage:

    request_counter = 100

    def __init__(self, citizen):

        Garbage.request_counter += 1

        self.__request_id = Garbage.request_counter
        self.__citizen = citizen
        self.__status = "Pending"

    @property
    def request_id(self):
        return self.__request_id

    @property
    def status(self):
        return self.__status

    def collect(self):

        self.__status = "Collected"

        print("Garbage Collected Successfully")

    def display(self):

        print("\n========== GARBAGE ==========")
        print("Request ID :", self.request_id)
        print("Citizen    :", self.__citizen.name)
        print("Status     :", self.status)