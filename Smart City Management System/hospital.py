class Hospital:

    def __init__(self,
                 hospital_name):

        self.__hospital_name = hospital_name
        self.__patients = []
        self.__ambulances = []

    @property
    def hospital_name(self):
        return self.__hospital_name

    def add_ambulance(self,
                      ambulance):

        self.__ambulances.append(ambulance)

        print("Ambulance Added")

    def admit_patient(self,
                      citizen):

        self.__patients.append(citizen)

        print(citizen.name,
              "Admitted Successfully")

    def discharge_patient(self,
                          citizen_id):

        for patient in self.__patients:

            if patient.person_id == citizen_id:

                self.__patients.remove(patient)

                print(patient.name,
                      "Discharged")

                return

        print("Patient Not Found")

    def request_ambulance(self):

        for ambulance in self.__ambulances:

            if ambulance.status == "Available":

                ambulance.dispatch()

                return ambulance

        print("No Ambulance Available")

        return None

    def hospital_report(self):

        print("\n========== HOSPITAL REPORT ==========")

        print("Hospital      :", self.__hospital_name)

        print("Patients      :", len(self.__patients))

        print("Ambulances    :", len(self.__ambulances))

    def display_patients(self):

        print("\n===== Patient List =====")

        if len(self.__patients) == 0:

            print("No Patients")

            return

        for patient in self.__patients:

            patient.display()