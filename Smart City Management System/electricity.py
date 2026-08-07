class Electricity:

    UNIT_PRICE = 8.5

    def __init__(self, connection_id, citizen):

        self.__connection_id = connection_id
        self.__citizen = citizen
        self.__units = 0

    @property
    def connection_id(self):
        return self.__connection_id

    @property
    def units(self):
        return self.__units

    def add_units(self, units):

        if units <= 0:
            print("Invalid Units")
            return

        self.__units += units

        print("Units Updated Successfully")

    def calculate_bill(self):

        return self.__units * Electricity.UNIT_PRICE

    def reset_units(self):

        self.__units = 0

    def display(self):

        print("\n========== ELECTRICITY ==========")
        print("Connection ID :", self.connection_id)
        print("Citizen       :", self.__citizen.name)
        print("Units Used    :", self.units)
        print("Bill Amount   : ₹", self.calculate_bill())