class ElectricityArea:
    def __init__(self, area_id, area, status, supply_time):
        self.area_id, self.area = area_id, area
        self.status, self.supply_time = status, supply_time

    def __str__(self):
        return f"ID: {self.area_id} | {self.area} | Status: {self.status} | Supply: {self.supply_time}"


class ElectricityComplaint:
    def __init__(self, complaint_id, citizen_id, area, problem, description, status="Pending"):
        self.complaint_id, self.citizen_id = complaint_id, citizen_id
        self.area, self.problem = area, problem
        self.description, self.status = description, status

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return (f"ID: {self.complaint_id} | Citizen: {self.citizen_id} | Area: {self.area}\n"
                f"Problem: {self.problem} | Status: {self.status}\n{self.description}")
