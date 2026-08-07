class Ambulance:

    ambulance_count = 0

    def __init__(self,
                 ambulance_id,
                 driver_name):

        Ambulance.ambulance_count += 1

        self.__ambulance_id = ambulance_id
        self.__driver_name = driver_name
        self.__status = "Available"

    @property
    def ambulance_id(self):
        return self.__ambulance_id

    @property
    def status(self):
        return self.__status

    def dispatch(self):

        if self.__status == "Available":

            self.__status = "Busy"

            print("Ambulance Dispatched")

        else:

            print("Ambulance Already Busy")

    def complete_trip(self):

        self.__status = "Available"

        print("Ambulance Available Again")

    def display(self):

        print("\n========== AMBULANCE ==========")
        print("Ambulance ID :", self.__ambulance_id)
        print("Driver       :", self.__driver_name)
        print("Status       :", self.__status)