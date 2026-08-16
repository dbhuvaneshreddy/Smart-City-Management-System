from models.citizen import Citizen
from models.police import PoliceStation, PoliceComplaint
from models.hospital import Hospital, EmergencyRequest
from models.electricity import ElectricityArea, ElectricityComplaint
from models.transport import Bus, TransportComplaint
from models.water import WaterArea, WaterComplaint
from models.complaint import MunicipalComplaint

from data.citizen_data import citizens
from data.police_data import police_stations, police_complaints
from data.hospital_data import hospitals
from data.electricity_data import electricity_areas, electricity_complaints
from data.transport_data import buses
from data.water_data import water_areas, water_complaints
from data.complaint_data import municipal_complaints


class SmartCity:
    def __init__(self):
        self.citizens = [Citizen(*x) for x in citizens]
        self.police_stations = [PoliceStation(*x) for x in police_stations]
        self.police_complaints = [PoliceComplaint(*x) for x in police_complaints]
        self.hospitals = [Hospital(*x) for x in hospitals]
        self.emergency_requests = []
        self.electricity_areas = [ElectricityArea(*x) for x in electricity_areas]
        self.electricity_complaints = [ElectricityComplaint(*x) for x in electricity_complaints]
        self.buses = [Bus(*x) for x in buses]
        self.transport_complaints = []
        self.water_areas = [WaterArea(*x) for x in water_areas]
        self.water_complaints = [WaterComplaint(*x) for x in water_complaints]
        self.water_tankers = []
        self.municipal_complaints = [MunicipalComplaint(*x) for x in municipal_complaints]

    def next_id(self, items, attr, start):
        return max([getattr(x, attr) for x in items], default=start - 1) + 1

    def valid_citizen(self, cid):
        return any(c.citizen_id == cid for c in self.citizens)

    def police_menu(self):
        while True:
            print("\n--- POLICE SERVICES ---")
            print("1.View Stations  2.Contact by Area  3.Register Complaint")
            print("4.View Complaints  5.Update Status  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                for x in self.police_stations: print(x)
            elif ch == "2":
                area = input("Area: ").lower()
                for x in self.police_stations:
                    if area in x.area.lower(): print(x)
            elif ch == "3":
                cid = int(input("Citizen ID: "))
                if not self.valid_citizen(cid): print("Citizen not found."); continue
                new = self.next_id(self.police_complaints, "complaint_id", 1001)
                self.police_complaints.append(PoliceComplaint(
                    new, cid, input("Complaint type: "), input("Location: "),
                    input("Description: ")))
                print("Registered. ID:", new)
            elif ch == "4":
                for x in self.police_complaints: print("\n", x)
            elif ch == "5": self.change_status(self.police_complaints)
            elif ch == "0": break
            else: print("Invalid choice.")

    def hospital_menu(self):
        while True:
            print("\n--- HOSPITAL & EMERGENCY ---")
            print("1.View Hospitals  2.Emergency Availability  3.Available Beds")
            print("4.Find by Area  5.Request Emergency  6.View Requests  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                for x in self.hospitals: print("\n", x)
            elif ch == "2":
                for x in self.hospitals: print(x.name, "->", x.emergency)
            elif ch == "3":
                for x in self.hospitals: print(x.name, "->", x.beds)
            elif ch == "4":
                area = input("Area: ").lower()
                for x in self.hospitals:
                    if area in x.area.lower(): print(x)
            elif ch == "5":
                cid = int(input("Citizen ID: "))
                if not self.valid_citizen(cid): print("Citizen not found."); continue
                rid = self.next_id(self.emergency_requests, "request_id", 5001)
                self.emergency_requests.append(EmergencyRequest(
                    rid, cid, input("Emergency type: "), input("Location: ")))
                print("Emergency request ID:", rid)
            elif ch == "6":
                for x in self.emergency_requests: print(x)
            elif ch == "0": break
            else: print("Invalid choice.")

    def electricity_menu(self):
        while True:
            print("\n--- ELECTRICITY SERVICES ---")
            print("1.View Status  2.Check Area  3.Report Power Cut")
            print("4.Report Electrical Problem  5.Track Complaint  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                for x in self.electricity_areas: print(x)
            elif ch == "2":
                area = input("Area: ").lower()
                for x in self.electricity_areas:
                    if area in x.area.lower(): print(x)
            elif ch in ("3", "4"):
                cid = int(input("Citizen ID: "))
                area = input("Area: ")
                problem = "Power Cut" if ch == "3" else "Electrical Problem"
                new = self.next_id(self.electricity_complaints, "complaint_id", 2001)
                self.electricity_complaints.append(ElectricityComplaint(
                    new, cid, area, problem, input("Description: ")))
                print("Complaint ID:", new)
            elif ch == "5": self.search(self.electricity_complaints)
            elif ch == "0": break
            else: print("Invalid choice.")

    def transport_menu(self):
        while True:
            print("\n--- TRANSPORT SERVICES ---")
            print("1.View Buses  2.Search Route  3.View Timings  4.View Fare")
            print("5.Report Transport Problem  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                for x in self.buses: print("\n", x)
            elif ch == "2":
                route = input("Route keyword: ").lower()
                for x in self.buses:
                    if route in x.route.lower(): print(x)
            elif ch == "3":
                for x in self.buses: print(x.number, "->", x.timing)
            elif ch == "4":
                for x in self.buses: print(x.number, "-> Rs.", x.fare)
            elif ch == "5":
                cid = int(input("Citizen ID: "))
                new = self.next_id(self.transport_complaints, "complaint_id", 6001)
                self.transport_complaints.append(TransportComplaint(
                    new, cid, input("Bus number: "), input("Problem: "),
                    input("Description: ")))
                print("Complaint ID:", new)
            elif ch == "0": break
            else: print("Invalid choice.")

    def water_menu(self):
        while True:
            print("\n--- WATER SUPPLY SERVICES ---")
            print("1.View Schedule  2.Check Status  3.Report Leakage")
            print("4.Report Shortage  5.Request Tanker  6.View Complaints  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                for x in self.water_areas: print(x)
            elif ch == "2":
                area = input("Area: ").lower()
                for x in self.water_areas:
                    if area in x.area.lower(): print(x)
            elif ch in ("3", "4"):
                cid = int(input("Citizen ID: "))
                area = input("Area: ")
                problem = "Leakage" if ch == "3" else "Water Shortage"
                new = self.next_id(self.water_complaints, "complaint_id", 3001)
                self.water_complaints.append(WaterComplaint(
                    new, cid, area, problem, input("Description: ")))
                print("Complaint ID:", new)
            elif ch == "5":
                cid = int(input("Citizen ID: "))
                self.water_tankers.append({
                    "citizen_id": cid, "area": input("Area: "),
                    "reason": input("Reason: "), "status": "Pending"})
                print("Tanker request submitted.")
            elif ch == "6":
                for x in self.water_complaints: print("\n", x)
            elif ch == "0": break
            else: print("Invalid choice.")

    def complaint_menu(self):
        while True:
            print("\n--- MUNICIPAL / COMPLAINT SERVICES ---")
            print("1.Register  2.View  3.Search ID  4.Update")
            print("5.Resolve  6.Pending  7.Resolved  0.Back")
            ch = input("Choice: ")
            if ch == "1":
                cid = int(input("Citizen ID: "))
                new = self.next_id(self.municipal_complaints, "complaint_id", 4001)
                self.municipal_complaints.append(MunicipalComplaint(
                    new, cid, input("Category: "), input("Location: "),
                    input("Description: ")))
                print("Complaint ID:", new)
            elif ch == "2":
                for x in self.municipal_complaints: print("\n", x)
            elif ch == "3": self.search(self.municipal_complaints)
            elif ch == "4":
                try: cid = int(input("Complaint ID: "))
                except ValueError: print("Invalid ID."); continue
                x = next((z for z in self.municipal_complaints if z.complaint_id == cid), None)
                if x: x.update(description=input("New description: ")); print("Updated.")
                else: print("Not found.")
            elif ch == "5": self.resolve(self.municipal_complaints)
            elif ch == "6": self.filter_status(self.municipal_complaints, "Pending")
            elif ch == "7": self.filter_status(self.municipal_complaints, "Resolved")
            elif ch == "0": break
            else: print("Invalid choice.")

    def search(self, items):
        try: cid = int(input("Complaint ID: "))
        except ValueError: print("Invalid ID."); return
        x = next((z for z in items if z.complaint_id == cid), None)
        print(x if x else "Complaint not found.")

    def change_status(self, items):
        try: cid = int(input("Complaint ID: "))
        except ValueError: print("Invalid ID."); return
        x = next((z for z in items if z.complaint_id == cid), None)
        if not x: print("Not found."); return
        print("1.Pending  2.In Progress  3.Resolved")
        statuses = {"1":"Pending", "2":"In Progress", "3":"Resolved"}
        s = statuses.get(input("Status: "))
        if s: x.update_status(s); print("Updated.")
        else: print("Invalid status.")

    def resolve(self, items):
        try: cid = int(input("Complaint ID: "))
        except ValueError: print("Invalid ID."); return
        x = next((z for z in items if z.complaint_id == cid), None)
        if x: x.update_status("Resolved"); print("Resolved.")
        else: print("Not found.")

    def filter_status(self, items, status):
        found = False
        for x in items:
            if x.status == status:
                print("\n", x); found = True
        if not found: print("No", status, "complaints.")
