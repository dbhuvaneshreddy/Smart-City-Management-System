from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self,
                 vehicle_number,
                 owner_name,
                 brand,
                 color,
                 fuel_type):

        super().__init__(
            vehicle_number,
            owner_name,
            brand,
            color
        )

        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type

    def vehicle_type(self):
        return "Car"

    def display(self):

        print("\n========== CAR ==========")
        print("Vehicle Number :", self.vehicle_number)
        print("Owner          :", self.owner_name)
        print("Brand          :", self.brand)
        print("Color          :", self.color)
        print("Fuel           :", self.fuel_type)
        print("Parked         :", self.is_parked)