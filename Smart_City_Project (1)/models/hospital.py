class Hospital:
    def __init__(self, hospital_id, name, area, phone, emergency, beds):
        self.hospital_id, self.name, self.area = hospital_id, name, area
        self.phone, self.emergency, self.beds = phone, emergency, beds

    def __str__(self):
        return (f"ID: {self.hospital_id} | {self.name} | Area: {self.area}\n"
                f"Phone: {self.phone} | Emergency: {self.emergency} | Beds: {self.beds}")


class EmergencyRequest:
    def __init__(self, request_id, citizen_id, emergency_type, location, status="Pending"):
        self.request_id, self.citizen_id = request_id, citizen_id
        self.emergency_type, self.location, self.status = emergency_type, location, status

    def __str__(self):
        return (f"Request: {self.request_id} | Citizen: {self.citizen_id} | "
                f"Type: {self.emergency_type} | Location: {self.location} | Status: {self.status}")
