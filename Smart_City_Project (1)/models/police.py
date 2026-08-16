class PoliceStation:
    def __init__(self, station_id, name, area, phone):
        self.station_id, self.name, self.area, self.phone = station_id, name, area, phone

    def __str__(self):
        return f"ID: {self.station_id} | {self.name} | Area: {self.area} | Phone: {self.phone}"


class PoliceComplaint:
    def __init__(self, complaint_id, citizen_id, complaint_type, location, description, status="Pending"):
        self.complaint_id = complaint_id
        self.citizen_id = citizen_id
        self.complaint_type = complaint_type
        self.location = location
        self.description = description
        self.status = status

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return (f"ID: {self.complaint_id} | Citizen: {self.citizen_id} | "
                f"Type: {self.complaint_type} | Location: {self.location} | "
                f"Status: {self.status}\nDescription: {self.description}")
