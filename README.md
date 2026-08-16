# 🏙️ Smart City Management System

A **Python OOP-based Smart City Management System** that provides citizens with access to multiple essential city services through a single console application.

The project demonstrates **Python fundamentals, Object-Oriented Programming, modular programming, data management, and service-based application design**.

## 🚀 Features

The application provides six major city services:

### 👮 1. Police Services

* View police stations
* Search police station by area
* View station contact details
* Register police complaints
* View registered complaints
* Update complaint status
* Track complaint progress

### 🏥 2. Hospital & Emergency Services

* View available hospitals
* Check emergency availability
* View available beds
* Find hospitals by area
* Submit emergency requests
* View emergency requests

### ⚡ 3. Electricity Services

* View electricity status
* Check electricity status by area
* Report power cuts
* Report electrical problems
* Track electricity complaints

### 🚌 4. Transport Services

* View available buses
* Search bus routes
* View bus timings
* Check bus fares
* Report transport-related problems

### 💧 5. Water Supply Services

* View water supply schedules
* Check water supply status
* Report water leakage
* Report water shortage
* Request water tankers
* View water complaints

### 🏛️ 6. Municipal / Complaint Services

* Register municipal complaints
* View complaints
* Search complaints by ID
* Update complaints
* Resolve complaints
* View pending complaints
* View resolved complaints

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* Classes & Objects
* Constructors
* Encapsulation
* Methods
* Lists
* Dictionaries
* Functions
* Modules & Packages
* Exception Handling
* Console-based User Interface

No external Python packages are required.

## 📂 Project Structure

```text
Smart_City_Project/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── citizen.py
│   ├── police.py
│   ├── hospital.py
│   ├── electricity.py
│   ├── transport.py
│   ├── water.py
│   └── complaint.py
│
├── services/
│   ├── __init__.py
│   └── city_service.py
│
└── data/
    ├── __init__.py
    ├── citizen_data.py
    ├── police_data.py
    ├── hospital_data.py
    ├── electricity_data.py
    ├── transport_data.py
    ├── water_data.py
    └── complaint_data.py
```

## 🧩 Project Architecture

The project is divided into three major layers:

### Models

Contains the classes representing different entities in the city system.

Examples:

* `Citizen`
* `PoliceStation`
* `PoliceComplaint`
* `Hospital`
* `EmergencyRequest`
* `ElectricityArea`
* `ElectricityComplaint`
* `Bus`
* `TransportComplaint`
* `WaterArea`
* `WaterComplaint`
* `MunicipalComplaint`

### Services

`city_service.py` contains the main application logic.

The `SmartCity` class manages:

* Citizens
* Police services
* Hospital services
* Electricity services
* Transport services
* Water services
* Municipal complaints

### Data

The `data` package contains sample data used by the application.

This makes the project modular and easy to extend with a database in the future.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project directory

```bash
cd Smart_City_Project
```

### 3. Run the application

```bash
python main.py
```

## 💻 Main Menu

```text
=======================================================
        SMART CITY MANAGEMENT SYSTEM
=======================================================
1. Police Services
2. Hospital & Emergency Services
3. Electricity Services
4. Transport Services
5. Water Supply Services
6. Municipal / Complaint Services
0. Exit
```

Select an option to access the corresponding city service.

## 🧑‍💻 OOP Concepts Demonstrated

This project is primarily designed to demonstrate **Object-Oriented Programming in Python**.

### Classes and Objects

Different real-world entities are represented using Python classes.

```python
class Citizen:
    def __init__(self, citizen_id, name, phone, area):
        self.citizen_id = citizen_id
        self.name = name
        self.phone = phone
        self.area = area
```

### Constructors

The `__init__()` method initializes object attributes.

### Encapsulation

Data and related methods are grouped together inside classes.

### Methods

Classes contain methods for operations such as:

```python
update_status()
```

### Modular Programming

The application is divided into separate modules such as:

```text
models/
services/
data/
```

This improves code organization and maintainability.

## 📊 Sample Data

The project includes sample citizens and city services for areas such as:

* Kukatpally
* Madhapur
* Ameerpet

Example services include police stations, hospitals, electricity areas, buses, water supply areas, and citizen complaints.

## 🔮 Future Enhancements

The project can be extended with:

* 🗄️ SQLite/MySQL database integration
* 🌐 Django or Flask web application
* 🖥️ Tkinter GUI
* 🔐 User authentication and login
* 👤 Citizen registration
* 📱 Mobile application
* 📍 Location-based services
* 📊 Admin dashboard
* 🔔 Emergency notifications
* 📧 Email/SMS notifications
* ☁️ Cloud deployment
* 🔎 Advanced complaint tracking
* 📈 Service analytics and reports

## 🎯 Learning Objectives

This project helps demonstrate practical knowledge of:

* Python programming
* OOP concepts
* Classes and objects
* Constructors
* Lists and dictionaries
* Functions and methods
* Modules and packages
* Exception handling
* Data organization
* Application architecture
* Real-world problem solving

## 👨‍💻 Author

**D Bhuvanesh Reddy**

Python Full Stack Trainee

### ⭐ If you find this project useful

Give the repository a **⭐ Star** and feel free to contribute or suggest improvements.

---

**Smart City Management System — Bringing essential city services together in one Python application.**
