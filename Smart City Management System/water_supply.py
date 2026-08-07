class WaterSupply:

    RATE_PER_LITER = 0.02

    def __init__(self, connection_id, citizen):

        self.__connection_id = connection_id
        self.__citizen = citizen
        self.__liters = 0

    def add_consumption(self, liters):

        if liters <= 0:
            print("Invalid Consumption")
            return

        self.__liters += liters

    def calculate_bill(self):

        return round(
            self.__liters * WaterSupply.RATE_PER_LITER,
            2
        )

    def display(self):

        print("\n========== WATER SUPPLY ==========")
        print("Connection :", self.__connection_id)
        print("Citizen    :", self.__citizen.name)
        print("Consumption:", self.__liters, "Liters")
        print("Bill       : ₹", self.calculate_bill())