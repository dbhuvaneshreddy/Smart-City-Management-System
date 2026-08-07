class FireStation:

    def __init__(self,
                 station_name):

        self.__station_name = station_name
        self.__fire_trucks = []

    def add_fire_truck(self,
                       truck):

        self.__fire_trucks.append(truck)

    def dispatch_fire_truck(self):

        if len(self.__fire_trucks) == 0:

            print("No Fire Truck Available")

            return

        truck = self.__fire_trucks[0]

        truck.extinguish_fire()

    def report(self):

        print("\n========== FIRE STATION ==========")
        print("Station     :", self.__station_name)
        print("Fire Trucks :", len(self.__fire_trucks))