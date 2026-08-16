class Bus:
    def __init__(self, number, route, timing, fare, status="Running"):
        self.number, self.route, self.timing = number, route, timing
        self.fare, self.status = fare, status

    def __str__(self):
        return (f"Bus: {self.number} | Route: {self.route}\n"
                f"Time: {self.timing} | Fare: Rs.{self.fare} | Status: {self.status}")


class TransportComplaint:
    def __init__(self, complaint_id, citizen_id, bus_number, problem, description, status="Pending"):
        self.complaint_id, self.citizen_id = complaint_id, citizen_id
        self.bus_number, self.problem = bus_number, problem
        self.description, self.status = description, status

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return (f"ID: {self.complaint_id} | Citizen: {self.citizen_id} | Bus: {self.bus_number}\n"
                f"Problem: {self.problem} | Status: {self.status}\n{self.description}")
