from abc import ABC


class ParkingSlot(ABC):

    slot_count = 0

    def __init__(self,
                 slot_number,
                 vehicle_type):

        ParkingSlot.slot_count += 1

        self._slot_number = slot_number
        self._vehicle_type = vehicle_type
        self._occupied = False
        self._vehicle = None

    @property
    def slot_number(self):
        return self._slot_number

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @property
    def occupied(self):
        return self._occupied

    @property
    def vehicle(self):
        return self._vehicle

    def park_vehicle(self, vehicle):

        if self._occupied:
            print("Slot Already Occupied")
            return False

        self._vehicle = vehicle
        self._occupied = True

        vehicle.park()

        print(vehicle.vehicle_number,
              "Parked in Slot",
              self.slot_number)

        return True

    def remove_vehicle(self):

        if not self._occupied:
            print("Slot Empty")
            return None

        vehicle = self._vehicle

        vehicle.leave_parking()

        self._vehicle = None
        self._occupied = False

        print(vehicle.vehicle_number,
              "Removed from Slot",
              self.slot_number)

        return vehicle

    def display(self):

        print("\n========== SLOT ==========")

        print("Slot Number :", self.slot_number)
        print("Vehicle Type:", self.vehicle_type)

        if self.occupied:
            print("Status      : Occupied")
            print("Vehicle     :", self.vehicle.vehicle_number)
        else:
            print("Status      : Available")