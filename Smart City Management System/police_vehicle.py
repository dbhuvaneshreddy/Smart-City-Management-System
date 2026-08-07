from vehicle import Vehicle


class PoliceVehicle(Vehicle):

    def __init__(self,
                 vehicle_number,
                 officer_name,
                 brand,
                 color):

        super().__init__(
            vehicle_number,
            officer_name,
            brand,
            color
        )

        self.__siren = False

    @property
    def siren(self):
        return self.__siren

    def enable_siren(self):

        self.__siren = True
        print("Police Siren ON")

    def disable_siren(self):

        self.__siren = False
        print("Police Siren OFF")

    def patrol(self):

        print("Police Patrol Started")

    def vehicle_type(self):
        return "Police Vehicle"

    def display(self):

        print("\n========== POLICE VEHICLE ==========")
        print("Vehicle Number :", self.vehicle_number)
        print("Officer        :", self.owner_name)
        print("Brand          :", self.brand)
        print("Color          :", self.color)
        print("Siren          :", self.siren)