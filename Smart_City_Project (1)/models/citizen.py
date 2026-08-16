class Citizen:
    def __init__(self, citizen_id, name, phone, area):
        self.citizen_id = citizen_id
        self.name = name
        self.phone = phone
        self.area = area

    def __str__(self):
        return f"ID: {self.citizen_id} | {self.name} | {self.phone} | {self.area}"
