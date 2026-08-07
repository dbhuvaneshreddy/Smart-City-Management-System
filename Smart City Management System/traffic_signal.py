class TrafficSignal:

    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"

    def __init__(self,
                 signal_id,
                 location):

        self.__signal_id = signal_id
        self.__location = location
        self.__status = TrafficSignal.RED

    @property
    def signal_id(self):
        return self.__signal_id

    @property
    def location(self):
        return self.__location

    @property
    def status(self):
        return self.__status

    def change_to_red(self):

        self.__status = TrafficSignal.RED

    def change_to_yellow(self):

        self.__status = TrafficSignal.YELLOW

    def change_to_green(self):

        self.__status = TrafficSignal.GREEN

    def display(self):

        print("\n========== TRAFFIC SIGNAL ==========")
        print("Signal ID :", self.signal_id)
        print("Location  :", self.location)
        print("Status    :", self.status)