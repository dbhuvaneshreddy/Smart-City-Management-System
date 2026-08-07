class Parking:

    def __init__(self):

        self.__slots = []

    def add_slot(self, slot):

        self.__slots.append(slot)

        print("Slot Added")

    def available_slots(self):

        count = 0

        for slot in self.__slots:

            if not slot.occupied:
                count += 1

        return count

    def park_vehicle(self, vehicle):

        vehicle_name = vehicle.vehicle_type()

        for slot in self.__slots:

            if (not slot.occupied and
                slot.vehicle_type == vehicle_name):

                slot.park_vehicle(vehicle)

                return

        print("No Available Slot")

    def exit_vehicle(self,
                     vehicle_number):

        for slot in self.__slots:

            if slot.occupied:

                if slot.vehicle.vehicle_number == vehicle_number:

                    slot.remove_vehicle()

                    return

        print("Vehicle Not Found")

    def parking_report(self):

        print("\n========== PARKING REPORT ==========")

        print("Total Slots :", len(self.__slots))

        print("Available   :", self.available_slots())

        print("Occupied    :",
              len(self.__slots) -
              self.available_slots())

    def display_slots(self):

        for slot in self.__slots:

            slot.display()