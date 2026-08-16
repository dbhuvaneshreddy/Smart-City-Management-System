from services.city_service import SmartCity

def main():
    city = SmartCity()
    while True:
        print("\n" + "=" * 55)
        print("        SMART CITY MANAGEMENT SYSTEM")
        print("=" * 55)
        print("1. Police Services")
        print("2. Hospital & Emergency Services")
        print("3. Electricity Services")
        print("4. Transport Services")
        print("5. Water Supply Services")
        print("6. Municipal / Complaint Services")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1": city.police_menu()
        elif choice == "2": city.hospital_menu()
        elif choice == "3": city.electricity_menu()
        elif choice == "4": city.transport_menu()
        elif choice == "5": city.water_menu()
        elif choice == "6": city.complaint_menu()
        elif choice == "0":
            print("Thank you for using Smart City Management System.")
            break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
