from vehicle import Vehicle


class Bus(Vehicle):

    def __init__(self,
                 vehicle_number,
                 owner_name,
                 brand,
                 color,
                 seating_capacity):

        super().__init__(
            vehicle_number,
            owner_name,
            brand,
            color
        )

        self.__seating_capacity = seating_capacity

    @property
    def seating_capacity(self):
        return self.__seating_capacity

    def vehicle_type(self):
        return "Bus"

    def display(self):

        print("\n========== BUS ==========")
        print("Vehicle Number :", self.vehicle_number)
        print("Owner          :", self.owner_name)
        print("Brand          :", self.brand)
        print("Color          :", self.color)
        print("Seats          :", self.seating_capacity)
        print("Parked         :", self.is_parked)