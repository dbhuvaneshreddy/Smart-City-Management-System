from vehicle import Vehicle


class FireTruck(Vehicle):

    def __init__(self,
                 vehicle_number,
                 driver_name,
                 brand,
                 color,
                 water_capacity):

        super().__init__(
            vehicle_number,
            driver_name,
            brand,
            color
        )

        self.__water_capacity = water_capacity

    @property
    def water_capacity(self):
        return self.__water_capacity

    def extinguish_fire(self):

        print("Fire Extinguished Successfully")

    def refill_water(self):

        print("Water Tank Refilled")

    def vehicle_type(self):
        return "Fire Truck"

    def display(self):

        print("\n========== FIRE TRUCK ==========")
        print("Vehicle Number :", self.vehicle_number)
        print("Driver         :", self.owner_name)
        print("Brand          :", self.brand)
        print("Water Capacity :", self.water_capacity, "Liters")