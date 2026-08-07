from abc import ABC, abstractmethod


class Vehicle(ABC):

    vehicle_count = 0

    def __init__(self,
                 vehicle_number,
                 owner_name,
                 brand,
                 color):

        Vehicle.vehicle_count += 1

        self._vehicle_number = vehicle_number
        self._owner_name = owner_name
        self._brand = brand
        self._color = color
        self._is_parked = False

    @property
    def vehicle_number(self):
        return self._vehicle_number

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def brand(self):
        return self._brand

    @property
    def color(self):
        return self._color

    @property
    def is_parked(self):
        return self._is_parked

    def park(self):
        self._is_parked = True
        print(f"{self.vehicle_number} Parked Successfully")

    def leave_parking(self):
        self._is_parked = False
        print(f"{self.vehicle_number} Left Parking")

    @classmethod
    def total_vehicles(cls):
        return cls.vehicle_count

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def display(self):
        pass