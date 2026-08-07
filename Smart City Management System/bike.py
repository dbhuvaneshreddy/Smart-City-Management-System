from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self,
                 vehicle_number,
                 owner_name,
                 brand,
                 color,
                 engine_cc):

        super().__init__(
            vehicle_number,
            owner_name,
            brand,
            color
        )

        self.__engine_cc = engine_cc

    @property
    def engine_cc(self):
        return self.__engine_cc

    def vehicle_type(self):
        return "Bike"

    def display(self):

        print("\n========== BIKE ==========")
        print("Vehicle Number :", self.vehicle_number)
        print("Owner          :", self.owner_name)
        print("Brand          :", self.brand)
        print("Color          :", self.color)
        print("Engine         :", self.engine_cc, "CC")
        print("Parked         :", self.is_parked)