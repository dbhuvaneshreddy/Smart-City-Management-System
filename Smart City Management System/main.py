# ==========================================
# SMART CITY MANAGEMENT SYSTEM
# MAIN.PY (SECTION 1)
# ==========================================

# -------- PEOPLE --------
from citizen import Citizen
from employee import Employee
from admin import Admin

# -------- CITY --------
from city import City
from zone import Zone
from department import Department

# -------- VEHICLES --------
from car import Car
from bike import Bike
from bus import Bus

# -------- TRAFFIC --------
from traffic import Traffic
from traffic_signal import TrafficSignal

# -------- PARKING --------
from parking import Parking
from parking_slot import ParkingSlot

# -------- UTILITIES --------
from electricity import Electricity
from water_supply import WaterSupply
from garbage import Garbage

# -------- HOSPITAL --------
from hospital import Hospital
from ambulance import Ambulance

# -------- POLICE --------
from police_station import PoliceStation
from police_vehicle import PoliceVehicle

# -------- FIRE --------
from fire_station import FireStation
from fire_truck import FireTruck

# -------- COMPLAINT --------
from complaint import Complaint
from notification import Notification

# -------- REPORTS --------
from report import Report

# -------- UTILS --------
from utils import Utility


# ==========================================
# GLOBAL OBJECTS
# ==========================================

city = City(
    "Hyderabad Smart City",
    "City Commissioner"
)

traffic = Traffic()

parking = Parking()

hospital = Hospital(
    "Government Hospital"
)

police_station = PoliceStation(
    "Ameerpet Police Station"
)

fire_station = FireStation(
    "Hyderabad Fire Station"
)

notification = Notification()


# Master Collections

citizens = []

employees = []

vehicles = []

complaints = []

departments = []

zones = []


# ==========================================
# CREATE DEFAULT DATA
# ==========================================

def initialize_city():

    traffic_department = Department(
        "D101",
        "Traffic Department"
    )

    electricity_department = Department(
        "D102",
        "Electricity Department"
    )

    health_department = Department(
        "D103",
        "Health Department"
    )

    city.add_department(traffic_department)
    city.add_department(electricity_department)
    city.add_department(health_department)

    departments.extend([
        traffic_department,
        electricity_department,
        health_department
    ])

    zone1 = Zone(
        "Z101",
        "Ameerpet"
    )

    zone2 = Zone(
        "Z102",
        "Madhapur"
    )

    city.add_zone(zone1)
    city.add_zone(zone2)

    zones.extend([
        zone1,
        zone2
    ])

    signal1 = TrafficSignal(
        "S101",
        "Ameerpet"
    )

    signal2 = TrafficSignal(
        "S102",
        "Madhapur"
    )

    traffic.add_signal(signal1)
    traffic.add_signal(signal2)

    parking.add_slot(
        ParkingSlot(
            "C1",
            "Car"
        )
    )

    parking.add_slot(
        ParkingSlot(
            "B1",
            "Bike"
        )
    )

    parking.add_slot(
        ParkingSlot(
            "BUS1",
            "Bus"
        )
    )

    ambulance = Ambulance(
        "AMB101",
        "Ramesh"
    )

    hospital.add_ambulance(
        ambulance
    )

    police_vehicle = PoliceVehicle(
        "TS09POLICE01",
        "Inspector Ravi",
        "Mahindra",
        "White"
    )

    police_station.add_vehicle(
        police_vehicle
    )

    fire_truck = FireTruck(
        "TS09FIRE01",
        "Driver Suresh",
        "Tata",
        "Red",
        10000
    )

    fire_station.add_fire_truck(
        fire_truck
    )


# ==========================================
# MAIN MENU
# ==========================================

def display_main_menu():

    Utility.line()

    print(" SMART CITY MANAGEMENT SYSTEM ")

    Utility.line()

    print("1. Citizen Management")

    print("2. Employee Management")

    print("3. Vehicle Management")

    print("4. Traffic Management")

    print("5. Parking Management")

    print("6. Electricity Service")

    print("7. Water Supply")

    print("8. Garbage Management")

    print("9. Hospital Services")

    print("10. Police Services")

    print("11. Fire Station")

    print("12. Complaint Management")

    print("13. Notifications")

    print("14. Reports")

    print("15. Admin Panel")

    print("0. Exit")

    Utility.line()

# ==========================================
# CITIZEN MANAGEMENT
# ==========================================

def register_citizen():

    print("\n------ Register Citizen ------")

    citizen_id = Utility.generate_citizen_id()

    name = input("Enter Name : ")

    age = int(input("Enter Age : "))

    gender = input("Enter Gender : ")

    phone = input("Enter Phone : ")

    address = input("Enter Address : ")

    citizen = Citizen(
        citizen_id,
        name,
        age,
        gender,
        phone,
        address
    )

    citizens.append(citizen)

    city.add_citizen(citizen)

    print("\nCitizen Registered Successfully")
    print("Citizen ID :", citizen_id)


def view_all_citizens():

    if len(citizens) == 0:

        print("\nNo Citizens Found")

        return

    print("\n========== CITIZEN LIST ==========")

    for citizen in citizens:

        citizen.display()


def search_citizen():

    citizen_id = input("\nEnter Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen:

        citizen.display()

    else:

        print("Citizen Not Found")


def delete_citizen():

    citizen_id = input("\nEnter Citizen ID : ")

    city.remove_citizen(citizen_id)

    for citizen in citizens:

        if citizen.person_id == citizen_id:

            citizens.remove(citizen)

            print("Citizen Deleted")

            return


# ==========================================
# EMPLOYEE MANAGEMENT
# ==========================================

def add_employee():

    print("\n------ Add Employee ------")

    employee_id = Utility.generate_employee_id()

    name = input("Enter Name : ")

    age = int(input("Enter Age : "))

    gender = input("Enter Gender : ")

    phone = input("Enter Phone : ")

    address = input("Enter Address : ")

    department = input("Department : ")

    salary = float(input("Salary : "))

    employee = Employee(
        employee_id,
        name,
        age,
        gender,
        phone,
        address,
        department,
        salary
    )

    employees.append(employee)

    city.add_employee(employee)

    print("\nEmployee Added Successfully")


def view_all_employees():

    if len(employees) == 0:

        print("\nNo Employees Found")

        return

    print("\n========== EMPLOYEE LIST ==========")

    for employee in employees:

        employee.display()


def search_employee():

    employee_id = input("\nEnter Employee ID : ")

    employee = city.search_employee(employee_id)

    if employee:

        employee.display()

    else:

        print("Employee Not Found")


def update_salary():

    employee_id = input("\nEnter Employee ID : ")

    employee = city.search_employee(employee_id)

    if employee:

        percent = float(input("Increase Percentage : "))

        employee.increase_salary(percent)

        print("Salary Updated Successfully")

    else:

        print("Employee Not Found")


def delete_employee():

    employee_id = input("\nEnter Employee ID : ")

    for employee in employees:

        if employee.person_id == employee_id:

            employees.remove(employee)

            print("Employee Removed")

            return

    print("Employee Not Found")


# ==========================================
# CITIZEN MENU
# ==========================================

def citizen_menu():

    while True:

        print("\n========== CITIZEN MENU ==========")

        print("1. Register Citizen")

        print("2. View Citizens")

        print("3. Search Citizen")

        print("4. Delete Citizen")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            register_citizen()

        elif choice == "2":

            view_all_citizens()

        elif choice == "3":

            search_citizen()

        elif choice == "4":

            delete_citizen()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")


# ==========================================
# EMPLOYEE MENU
# ==========================================

def employee_menu():

    while True:

        print("\n========== EMPLOYEE MENU ==========")

        print("1. Add Employee")

        print("2. View Employees")

        print("3. Search Employee")

        print("4. Update Salary")

        print("5. Delete Employee")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_employee()

        elif choice == "2":

            view_all_employees()

        elif choice == "3":

            search_employee()

        elif choice == "4":

            update_salary()

        elif choice == "5":

            delete_employee()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")

# ==========================================
# VEHICLE MANAGEMENT
# ==========================================

def register_car():

    print("\n========== REGISTER CAR ==========")

    vehicle_number = input("Vehicle Number : ")
    owner = input("Owner Name : ")
    brand = input("Brand : ")
    color = input("Color : ")
    fuel = input("Fuel Type : ")

    car = Car(
        vehicle_number,
        owner,
        brand,
        color,
        fuel
    )

    vehicles.append(car)

    print("Car Registered Successfully")


def register_bike():

    print("\n========== REGISTER BIKE ==========")

    vehicle_number = input("Vehicle Number : ")
    owner = input("Owner Name : ")
    brand = input("Brand : ")
    color = input("Color : ")
    cc = int(input("Engine CC : "))

    bike = Bike(
        vehicle_number,
        owner,
        brand,
        color,
        cc
    )

    vehicles.append(bike)

    print("Bike Registered Successfully")


def register_bus():

    print("\n========== REGISTER BUS ==========")

    vehicle_number = input("Vehicle Number : ")
    owner = input("Owner Name : ")
    brand = input("Brand : ")
    color = input("Color : ")
    seats = int(input("Seating Capacity : "))

    bus = Bus(
        vehicle_number,
        owner,
        brand,
        color,
        seats
    )

    vehicles.append(bus)

    print("Bus Registered Successfully")


def view_all_vehicles():

    if len(vehicles) == 0:

        print("\nNo Vehicles Registered")

        return

    print("\n========== VEHICLE LIST ==========")

    for vehicle in vehicles:

        vehicle.display()


def search_vehicle():

    vehicle_number = input("\nVehicle Number : ")

    for vehicle in vehicles:

        if vehicle.vehicle_number == vehicle_number:

            vehicle.display()

            return

    print("Vehicle Not Found")


def delete_vehicle():

    vehicle_number = input("\nVehicle Number : ")

    for vehicle in vehicles:

        if vehicle.vehicle_number == vehicle_number:

            vehicles.remove(vehicle)

            print("Vehicle Deleted Successfully")

            return

    print("Vehicle Not Found")


# ==========================================
# VEHICLE MENU
# ==========================================

def vehicle_menu():

    while True:

        print("\n========== VEHICLE MENU ==========")

        print("1. Register Car")
        print("2. Register Bike")
        print("3. Register Bus")
        print("4. View All Vehicles")
        print("5. Search Vehicle")
        print("6. Delete Vehicle")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            register_car()

        elif choice == "2":

            register_bike()

        elif choice == "3":

            register_bus()

        elif choice == "4":

            view_all_vehicles()

        elif choice == "5":

            search_vehicle()

        elif choice == "6":

            delete_vehicle()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")

# ==========================================
# TRAFFIC MANAGEMENT
# ==========================================

def add_traffic_signal():

    print("\n========== ADD TRAFFIC SIGNAL ==========")

    signal_id = input("Signal ID : ")
    location = input("Location : ")

    signal = TrafficSignal(
        signal_id,
        location
    )

    traffic.add_signal(signal)

    print("Traffic Signal Added Successfully")


def register_vehicle_to_traffic():

    if len(vehicles) == 0:

        print("No Vehicles Registered")

        return

    vehicle_number = input("Vehicle Number : ")

    for vehicle in vehicles:

        if vehicle.vehicle_number == vehicle_number:

            traffic.register_vehicle(vehicle)

            return

    print("Vehicle Not Found")


def remove_vehicle_from_traffic():

    vehicle_number = input("Vehicle Number : ")

    traffic.remove_vehicle(vehicle_number)


def normal_traffic():

    traffic.normal_mode()

    print("Traffic Changed To Normal Mode")


def emergency_traffic():

    traffic.emergency_mode()

    print("Emergency Traffic Mode Activated")


def view_traffic_signals():

    traffic.display_signals()


def traffic_report():

    traffic.traffic_report()


# ==========================================
# TRAFFIC MENU
# ==========================================

def traffic_menu():

    while True:

        print("\n========== TRAFFIC MENU ==========")

        print("1. Add Traffic Signal")

        print("2. Register Vehicle")

        print("3. Remove Vehicle")

        print("4. Normal Traffic Mode")

        print("5. Emergency Mode")

        print("6. View Traffic Signals")

        print("7. Traffic Report")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_traffic_signal()

        elif choice == "2":

            register_vehicle_to_traffic()

        elif choice == "3":

            remove_vehicle_from_traffic()

        elif choice == "4":

            normal_traffic()

        elif choice == "5":

            emergency_traffic()

        elif choice == "6":

            view_traffic_signals()

        elif choice == "7":

            traffic_report()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# PARKING MANAGEMENT
# ==========================================

def add_parking_slot():

    print("\n========== ADD PARKING SLOT ==========")

    slot_number = input("Enter Slot Number : ")

    print("\nVehicle Types")
    print("1. Car")
    print("2. Bike")
    print("3. Bus")

    choice = input("Choose Vehicle Type : ")

    if choice == "1":
        vehicle_type = "Car"

    elif choice == "2":
        vehicle_type = "Bike"

    elif choice == "3":
        vehicle_type = "Bus"

    else:
        print("Invalid Choice")
        return

    slot = ParkingSlot(
        slot_number,
        vehicle_type
    )

    parking.add_slot(slot)

    print("Parking Slot Added Successfully")


# ------------------------------------------

def park_vehicle():

    if len(vehicles) == 0:

        print("No Vehicles Registered")
        return

    vehicle_number = input("Vehicle Number : ")

    for vehicle in vehicles:

        if vehicle.vehicle_number == vehicle_number:

            parking.park_vehicle(vehicle)

            return

    print("Vehicle Not Found")


# ------------------------------------------

def exit_vehicle():

    vehicle_number = input("Vehicle Number : ")

    parking.exit_vehicle(vehicle_number)


# ------------------------------------------

def view_parking_slots():

    parking.display_slots()


# ------------------------------------------

def parking_report():

    parking.parking_report()


# ------------------------------------------

def available_slots():

    print()

    print("Available Slots :", parking.available_slots())


# ==========================================
# PARKING MENU
# ==========================================

def parking_menu():

    while True:

        print("\n========== PARKING MENU ==========")

        print("1. Add Parking Slot")
        print("2. Park Vehicle")
        print("3. Remove Vehicle")
        print("4. View Parking Slots")
        print("5. Available Slots")
        print("6. Parking Report")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_parking_slot()

        elif choice == "2":

            park_vehicle()

        elif choice == "3":

            exit_vehicle()

        elif choice == "4":

            view_parking_slots()

        elif choice == "5":

            available_slots()

        elif choice == "6":

            parking_report()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# ELECTRICITY MANAGEMENT
# ==========================================

electricity_connections = []


def add_electricity_connection():

    if len(citizens) == 0:
        print("No Citizens Available")
        return

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:
        print("Citizen Not Found")
        return

    connection_id = input("Connection ID : ")

    connection = Electricity(
        connection_id,
        citizen
    )

    electricity_connections.append(connection)

    print("Electricity Connection Added")


def add_electricity_units():

    connection_id = input("Connection ID : ")

    for connection in electricity_connections:

        if connection.connection_id == connection_id:

            units = float(input("Units Consumed : "))

            connection.add_units(units)

            print("Units Updated")

            return

    print("Connection Not Found")


def electricity_report():

    if len(electricity_connections) == 0:

        print("No Connections")

        return

    for connection in electricity_connections:

        connection.display()


# ==========================================
# WATER MANAGEMENT
# ==========================================

water_connections = []


def add_water_connection():

    if len(citizens) == 0:

        print("No Citizens")

        return

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")

        return

    connection_id = input("Connection ID : ")

    connection = WaterSupply(
        connection_id,
        citizen
    )

    water_connections.append(connection)

    print("Water Connection Added")


def add_water_consumption():

    connection_id = input("Connection ID : ")

    for connection in water_connections:

        if connection.connection_id == connection_id:

            liters = float(input("Water Consumed (Liters): "))

            connection.add_consumption(liters)

            print("Water Consumption Updated")

            return

    print("Connection Not Found")


def water_report():

    if len(water_connections) == 0:

        print("No Water Connections")

        return

    for connection in water_connections:

        connection.display()


# ==========================================
# GARBAGE MANAGEMENT
# ==========================================

garbage_requests = []


def request_garbage_collection():

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")

        return

    request = Garbage(citizen)

    garbage_requests.append(request)

    print("Garbage Collection Requested")


def collect_garbage():

    request_id = int(input("Request ID : "))

    for request in garbage_requests:

        if request.request_id == request_id:

            request.collect()

            return

    print("Request Not Found")


def garbage_report():

    if len(garbage_requests) == 0:

        print("No Requests")

        return

    for request in garbage_requests:

        request.display()


# ==========================================
# UTILITY MENU
# ==========================================

def utility_menu():

    while True:

        print("\n========== UTILITY SERVICES ==========")

        print("1. Add Electricity Connection")
        print("2. Update Electricity Units")
        print("3. Electricity Report")

        print("4. Add Water Connection")
        print("5. Update Water Consumption")
        print("6. Water Report")

        print("7. Garbage Collection Request")
        print("8. Collect Garbage")
        print("9. Garbage Report")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_electricity_connection()

        elif choice == "2":

            add_electricity_units()

        elif choice == "3":

            electricity_report()

        elif choice == "4":

            add_water_connection()

        elif choice == "5":

            add_water_consumption()

        elif choice == "6":

            water_report()

        elif choice == "7":

            request_garbage_collection()

        elif choice == "8":

            collect_garbage()

        elif choice == "9":

            garbage_report()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# HOSPITAL MANAGEMENT
# ==========================================

ambulances = []
patients = []


def add_ambulance():

    print("\n========== ADD AMBULANCE ==========")

    ambulance_id = input("Ambulance ID : ")
    driver = input("Driver Name : ")

    ambulance = Ambulance(
        ambulance_id,
        driver
    )

    ambulances.append(ambulance)

    hospital.add_ambulance(ambulance)

    print("Ambulance Added Successfully")


# ------------------------------------------

def admit_patient():

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")

        return

    hospital.admit_patient(citizen)

    patients.append(citizen)


# ------------------------------------------

def discharge_patient():

    citizen_id = input("Citizen ID : ")

    hospital.discharge_patient(citizen_id)

    for patient in patients:

        if patient.person_id == citizen_id:

            patients.remove(patient)

            print("Patient Discharged")

            return


# ------------------------------------------

def request_ambulance():

    ambulance = hospital.request_ambulance()

    if ambulance:

        print()

        ambulance.display()


# ------------------------------------------

def complete_ambulance_trip():

    ambulance_id = input("Ambulance ID : ")

    for ambulance in ambulances:

        if ambulance.ambulance_id == ambulance_id:

            ambulance.complete_trip()

            return

    print("Ambulance Not Found")


# ------------------------------------------

def hospital_report():

    hospital.hospital_report()


# ------------------------------------------

def patient_list():

    hospital.display_patients()


# ==========================================
# HOSPITAL MENU
# ==========================================

def hospital_menu():

    while True:

        print("\n========== HOSPITAL MENU ==========")

        print("1. Add Ambulance")

        print("2. Admit Patient")

        print("3. Discharge Patient")

        print("4. Request Ambulance")

        print("5. Complete Trip")

        print("6. Patient List")

        print("7. Hospital Report")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_ambulance()

        elif choice == "2":

            admit_patient()

        elif choice == "3":

            discharge_patient()

        elif choice == "4":

            request_ambulance()

        elif choice == "5":

            complete_ambulance_trip()

        elif choice == "6":

            patient_list()

        elif choice == "7":

            hospital_report()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# POLICE MANAGEMENT
# ==========================================

police_vehicles = []


def add_police_vehicle():

    print("\n========== ADD POLICE VEHICLE ==========")

    vehicle_number = input("Vehicle Number : ")
    officer = input("Officer Name : ")
    brand = input("Brand : ")
    color = input("Color : ")

    vehicle = PoliceVehicle(
        vehicle_number,
        officer,
        brand,
        color
    )

    police_vehicles.append(vehicle)

    police_station.add_vehicle(vehicle)

    print("Police Vehicle Added Successfully")


# ------------------------------------------

def police_complaint():

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")

        return

    complaint = input("Complaint : ")

    police_station.register_complaint(
        citizen,
        complaint
    )


# ------------------------------------------

def dispatch_police():

    police_station.dispatch_vehicle()


# ------------------------------------------

def police_report():

    police_station.report()


# ==========================================
# FIRE STATION MANAGEMENT
# ==========================================

fire_trucks = []


def add_fire_truck():

    print("\n========== ADD FIRE TRUCK ==========")

    vehicle_number = input("Vehicle Number : ")

    driver = input("Driver Name : ")

    brand = input("Brand : ")

    color = input("Color : ")

    capacity = int(
        input("Water Capacity : ")
    )

    truck = FireTruck(
        vehicle_number,
        driver,
        brand,
        color,
        capacity
    )

    fire_trucks.append(truck)

    fire_station.add_fire_truck(truck)

    print("Fire Truck Added Successfully")


# ------------------------------------------

def dispatch_fire_truck():

    fire_station.dispatch_fire_truck()


# ------------------------------------------

def fire_report():

    fire_station.report()


# ==========================================
# POLICE & FIRE MENU
# ==========================================

def police_fire_menu():

    while True:

        print("\n========== PUBLIC SAFETY ==========")

        print("1. Add Police Vehicle")
        print("2. Register Police Complaint")
        print("3. Dispatch Police Vehicle")
        print("4. Police Report")

        print("5. Add Fire Truck")
        print("6. Dispatch Fire Truck")
        print("7. Fire Station Report")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            add_police_vehicle()

        elif choice == "2":

            police_complaint()

        elif choice == "3":

            dispatch_police()

        elif choice == "4":

            police_report()

        elif choice == "5":

            add_fire_truck()

        elif choice == "6":

            dispatch_fire_truck()

        elif choice == "7":

            fire_report()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# COMPLAINT MANAGEMENT
# ==========================================

complaints = []


def register_complaint():

    print("\n========== REGISTER COMPLAINT ==========")

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")
        return

    print("\nDepartments")
    print("1. Electricity")
    print("2. Water Supply")
    print("3. Garbage")
    print("4. Traffic")
    print("5. Police")
    print("6. Fire Station")
    print("7. Hospital")

    option = input("Choose Department : ")

    department = {
        "1": "Electricity",
        "2": "Water Supply",
        "3": "Garbage",
        "4": "Traffic",
        "5": "Police",
        "6": "Fire Station",
        "7": "Hospital"
    }.get(option)

    if department is None:

        print("Invalid Department")
        return

    title = input("Complaint Title : ")

    description = input("Description : ")

    complaint = Complaint(
        citizen,
        department,
        title,
        description
    )

    complaints.append(complaint)

    citizen.raise_complaint(title)

    print("\nComplaint Registered Successfully")
# ==========================================
# VIEW COMPLAINTS
# ==========================================

def view_all_complaints():

    if len(complaints) == 0:

        print("\nNo Complaints Found")
        return

    for complaint in complaints:

        complaint.display()
# ==========================================
# SEARCH COMPLAINT
# ==========================================

def search_complaint():

    complaint_id = int(input("Complaint ID : "))

    for complaint in complaints:

        if complaint.complaint_id == complaint_id:

            complaint.display()
            return

    print("Complaint Not Found")
# ==========================================
# ASSIGN COMPLAINT
# ==========================================

def assign_complaint():

    complaint_id = int(input("Complaint ID : "))

    for complaint in complaints:

        if complaint.complaint_id == complaint_id:

            complaint.assign()
            return

    print("Complaint Not Found")
# ==========================================
# RESOLVE COMPLAINT
# ==========================================

def resolve_complaint():

    complaint_id = int(input("Complaint ID : "))

    for complaint in complaints:

        if complaint.complaint_id == complaint_id:

            complaint.resolve()
            return

    print("Complaint Not Found")
# ==========================================
# NOTIFICATION MANAGEMENT
# ==========================================

def send_notification():

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen is None:

        print("Citizen Not Found")
        return

    message = input("Message : ")

    notification.send_notification(
        citizen,
        message
    )
# ==========================================
# BROADCAST NOTIFICATION
# ==========================================

def broadcast_notification():

    message = input("Broadcast Message : ")

    notification.broadcast(
        citizens,
        message
    )

    print("Broadcast Completed")
# ==========================================
# VIEW NOTIFICATIONS
# ==========================================

def view_notifications():

    citizen_id = input("Citizen ID : ")

    citizen = city.search_citizen(citizen_id)

    if citizen:

        citizen.view_notifications()

    else:

        print("Citizen Not Found")
# ==========================================
# COMPLAINT & NOTIFICATION MENU
# ==========================================

def complaint_menu():

    while True:

        print("\n========== COMPLAINT MANAGEMENT ==========")

        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Search Complaint")
        print("4. Assign Complaint")
        print("5. Resolve Complaint")

        print("\n========== NOTIFICATION ==========")

        print("6. Send Notification")
        print("7. Broadcast Notification")
        print("8. View Citizen Notifications")

        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            register_complaint()

        elif choice == "2":

            view_all_complaints()

        elif choice == "3":

            search_complaint()

        elif choice == "4":

            assign_complaint()

        elif choice == "5":

            resolve_complaint()

        elif choice == "6":

            send_notification()

        elif choice == "7":

            broadcast_notification()

        elif choice == "8":

            view_notifications()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# DASHBOARD
# ==========================================

def dashboard():

    print("\n" + "=" * 60)
    print(" SMART CITY DASHBOARD ".center(60))
    print("=" * 60)

    print(f"Total Citizens        : {city.total_citizens()}")
    print(f"Total Employees       : {city.total_employees()}")
    print(f"Total Departments     : {city.total_departments()}")
    print(f"Total Zones           : {city.total_zones()}")

    print(f"Registered Vehicles   : {len(vehicles)}")
    print(f"Traffic Signals       : {traffic.total_signals()}")
    print(f"Parking Slots         : {parking.available_slots()}")

    print(f"Electricity Users     : {len(electricity_connections)}")
    print(f"Water Connections     : {len(water_connections)}")
    print(f"Garbage Requests      : {len(garbage_requests)}")

    print(f"Hospital Patients     : {len(patients)}")
    print(f"Police Complaints     : {len(complaints)}")

    print("=" * 60)
# ==========================================
# REPORT MENU
# ==========================================

def report_menu():

    while True:

        print("\n========== REPORT MENU ==========")

        print("1. City Summary")
        print("2. Citizen Report")
        print("3. Employee Report")
        print("4. Vehicle Report")
        print("5. Traffic Report")
        print("6. Parking Report")
        print("7. Hospital Report")
        print("8. Dashboard")

        print("0. Back")

        choice = input("Choice : ")

        if choice == "1":

            Report.city_summary(city)

        elif choice == "2":

            view_all_citizens()

        elif choice == "3":

            view_all_employees()

        elif choice == "4":

            view_all_vehicles()

        elif choice == "5":

            traffic_report()

        elif choice == "6":

            parking_report()

        elif choice == "7":

            hospital_report()

        elif choice == "8":

            dashboard()

        elif choice == "0":

            break

        else:

            print("Invalid Choice")
# ==========================================
# ADMIN LOGIN
# ==========================================

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Username : ")

    password = input("Password : ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

        print("\nLogin Successful")

        admin_panel()

    else:

        print("Invalid Credentials")
# ==========================================
# ADMIN PANEL
# ==========================================

def admin_panel():

    while True:

        print("\n========== ADMIN PANEL ==========")

        print("1. Dashboard")
        print("2. Reports")
        print("3. View Citizens")
        print("4. View Employees")
        print("5. View Vehicles")
        print("6. View Complaints")
        print("7. Notification Report")

        print("0. Logout")

        choice = input("Choice : ")

        if choice == "1":

            dashboard()

        elif choice == "2":

            report_menu()

        elif choice == "3":

            view_all_citizens()

        elif choice == "4":

            view_all_employees()

        elif choice == "5":

            view_all_vehicles()

        elif choice == "6":

            view_all_complaints()

        elif choice == "7":

            notification.report()

        elif choice == "0":

            print("Logged Out")

            break

        else:

            print("Invalid Choice")
            