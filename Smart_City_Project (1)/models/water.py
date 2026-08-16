class WaterArea:
    def __init__(self, area_id, area, supply_time, status):
        self.area_id, self.area = area_id, area
        self.supply_time, self.status = supply_time, status

    def __str__(self):
        return f"ID: {self.area_id} | {self.area} | Supply: {self.supply_time} | Status: {self.status}"


class WaterComplaint:
    def __init__(self, complaint_id, citizen_id, area, problem, description, status="Pending"):
        self.complaint_id, self.citizen_id = complaint_id, citizen_id
        self.area, self.problem = area, problem
        self.description, self.status = description, status

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return (f"ID: {self.complaint_id} | Citizen: {self.citizen_id} | Area: {self.area}\n"
                f"Problem: {self.problem} | Status: {self.status}\n{self.description}")
