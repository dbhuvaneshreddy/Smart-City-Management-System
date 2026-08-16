class MunicipalComplaint:
    def __init__(self, complaint_id, citizen_id, category, location, description, status="Pending"):
        self.complaint_id, self.citizen_id = complaint_id, citizen_id
        self.category, self.location = category, location
        self.description, self.status = description, status

    def update(self, description=None, status=None):
        if description:
            self.description = description
        if status:
            self.status = status

    def __str__(self):
        return (f"ID: {self.complaint_id} | Citizen: {self.citizen_id} | "
                f"Category: {self.category} | Location: {self.location}\n"
                f"Description: {self.description} | Status: {self.status}")
