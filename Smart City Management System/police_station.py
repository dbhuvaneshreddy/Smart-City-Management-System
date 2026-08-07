class PoliceStation:

    def __init__(self,
                 station_name):

        self.__station_name = station_name
        self.__vehicles = []
        self.__complaints = []

    def add_vehicle(self,
                    vehicle):

        self.__vehicles.append(vehicle)

    def register_complaint(self,
                           citizen,
                           complaint):

        self.__complaints.append(
            (citizen, complaint)
        )

        print("Police Complaint Registered")

    def dispatch_vehicle(self):

        if len(self.__vehicles) == 0:

            print("No Police Vehicle Available")

            return

        vehicle = self.__vehicles[0]

        vehicle.enable_siren()

        vehicle.patrol()

    def report(self):

        print("\n========== POLICE REPORT ==========")
        print("Station     :", self.__station_name)
        print("Vehicles    :", len(self.__vehicles))
        print("Complaints  :", len(self.__complaints))