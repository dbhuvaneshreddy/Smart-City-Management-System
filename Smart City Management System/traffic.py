from traffic_signal import TrafficSignal


class Traffic:

    def __init__(self):

        self.__signals = []
        self.__vehicles = []

    def add_signal(self, signal):

        self.__signals.append(signal)

        print("Traffic Signal Added")

    def register_vehicle(self, vehicle):

        self.__vehicles.append(vehicle)

        print(vehicle.vehicle_number, "entered traffic")

    def remove_vehicle(self, vehicle_number):

        for vehicle in self.__vehicles:

            if vehicle.vehicle_number == vehicle_number:

                self.__vehicles.remove(vehicle)

                print(vehicle_number, "left traffic")

                return

        print("Vehicle Not Found")

    def total_vehicles(self):

        return len(self.__vehicles)

    def emergency_mode(self):

        print("\nEmergency Mode Activated")

        for signal in self.__signals:

            signal.change_to_green()

    def normal_mode(self):

        print("\nNormal Traffic Mode")

        for index, signal in enumerate(self.__signals):

            if index % 3 == 0:
                signal.change_to_green()

            elif index % 3 == 1:
                signal.change_to_yellow()

            else:
                signal.change_to_red()

    def display_signals(self):

        print("\n===== Traffic Signals =====")

        for signal in self.__signals:
            signal.display()

    def traffic_report(self):

        print("\n========== TRAFFIC REPORT ==========")
        print("Signals :", len(self.__signals))
        print("Vehicles:", len(self.__vehicles))