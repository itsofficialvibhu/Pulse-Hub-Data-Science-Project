import csv
import matplotlib.pyplot as plt

class PatientRecordsSystem:
    def __init__(self, data_file="patient_records.csv"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                # Convert PatientID to strings to ensure consistency
                self.records = {str(row['PatientID']): row for row in reader}
        except FileNotFoundError:
            self.records = {}

    def save_data(self):
        with open(self.data_file, 'w', newline='') as file:
            fieldnames = ['PatientID', 'Name', 'Address', 'Phone Number', 'Age', 'Health Problem']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.records.values())

    def add_patient(self, patient_id, name, address, phone_number, age, health_problem):
        # Convert PatientID to string to ensure consistency
        patient_id = str(patient_id)
        if patient_id not in self.records:
            self.records[patient_id] = {
                "PatientID": patient_id,
                "Name": name,
                "Address": address,
                "Phone Number": phone_number,
                "Age": age,
                "Health Problem": health_problem
            }
            self.save_data()
            print(f"Patient {name} added successfully.")
        else:
            print(f"Patient with ID {patient_id} already exists.")

    def get_patient_info(self, patient_id):
        # Convert PatientID to string to ensure consistency
        patient_id = str(patient_id)
        return self.records.get(patient_id)

    def display_all_patients(self):
        print("\nPatient Records:")
        for info in self.records.values():
            print(f"ID: {info.get('PatientID', 'N/A')}, Name: {info.get('Name', 'N/A')}, Address: {info.get('Address', 'N/A')}, Phone Number: {info.get('Phone Number', 'N/A')}, Age: {info.get('Age', 'N/A')}, Health Problem: {info.get('Health Problem', 'N/A')}")

    def update_patient_info(self, patient_id, name, address, phone_number, age, health_problem):
        # Convert PatientID to string to ensure consistency
        patient_id = str(patient_id)
        if patient_id in self.records:
            self.records[patient_id] = {
                "PatientID": patient_id,
                "Name": name,
                "Address": address,
                "Phone Number": phone_number,
                "Age": age,
                "Health Problem": health_problem
            }
            self.save_data()
            print(f"Patient {name} information updated successfully.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def delete_patient(self, patient_id):
        # Convert PatientID to string to ensure consistency
        patient_id = str(patient_id)
        if patient_id in self.records:
            del self.records[patient_id]
            self.save_data()
            print(f"Patient with ID {patient_id} deleted successfully.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def search_by_age_range(self, min_age, max_age):
        results = [info for info in self.records.values() if min_age <= int(info.get('Age', 0)) <= max_age]
        return results

    def plot_age_distribution(self):
        ages = [int(info.get('Age', 0)) for info in self.records.values() if info.get('Age').isdigit()]
        plt.hist(ages, bins=range(min(ages), max(ages) + 5, 5), edgecolor='black')
        plt.title('Age Distribution of Patients')
        plt.xlabel('Age')
        plt.ylabel('Number of Patients')
        plt.show()

    def plot_health_problem_distribution(self):
        health_problems = [info.get('Health Problem', 'N/A') for info in self.records.values()]
        health_problem_counts = {problem: health_problems.count(problem) for problem in set(health_problems) if problem != 'N/A'}

        labels = list(health_problem_counts.keys())
        counts = list(health_problem_counts.values())

        plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Health Problems Distribution of Patients')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

# Interactive User Input
if __name__ == "__main__":
    records_system = PatientRecordsSystem()

    while True:
        print("\nOptions:")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Display All Patients")
        print("4. Update Patient Information")
        print("5. Delete Patient Record")
        print("6. Search Patients by Age Range")
        print("7. Plot Age Distribution")
        print("8. Plot Health Problem Distribution")
        print("9. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            address = input("Enter Patient Address: ")
            phone_number = input("Enter Patient Phone Number: ")
            age = input("Enter Patient Age: ")
            health_problem = input("Enter Patient Health Problem: ")

            records_system.add_patient(patient_id, name, address, phone_number, age, health_problem)

        elif choice == "2":
            patient_id_to_search = input("Enter Patient ID to search: ")
            patient_info = records_system.get_patient_info(patient_id_to_search)

            if patient_info:
                print(f"\nPatient Information for ID {patient_id_to_search}:")
                print(f"Name: {patient_info.get('Name', 'N/A')}, Address: {patient_info.get('Address', 'N/A')}, Phone Number: {patient_info.get('Phone Number', 'N/A')}, Age: {patient_info.get('Age', 'N/A')}, Health Problem: {patient_info.get('Health Problem', 'N/A')}")
            else:
                print(f"\nPatient with ID {patient_id_to_search} not found.")

        elif choice == "3":
            records_system.display_all_patients()

        elif choice == "4":
            patient_id_to_update = input("Enter Patient ID to update: ")
            if patient_id_to_update in records_system.records:
                name = input("Enter updated Patient Name: ")
                address = input("Enter updated Patient Address: ")
                phone_number = input("Enter updated Patient Phone Number: ")
                age = input("Enter updated Patient Age: ")
                health_problem = input("Enter updated Patient Health Problem: ")

                records_system.update_patient_info(patient_id_to_update, name, address, phone_number, age, health_problem)
            else:
                print(f"\nPatient with ID {patient_id_to_update} not found.")

        elif choice == "5":
            patient_id_to_delete = input("Enter Patient ID to delete: ")
            records_system.delete_patient(patient_id_to_delete)


        elif choice == "6":
            min_age = int(input("Enter minimum age: "))
            max_age = int(input("Enter maximum age: "))
            patients_in_age_range = records_system.search_by_age_range(min_age, max_age)
            if patients_in_age_range:
                print("\nPatients in Age Range:")
                for info in patients_in_age_range:
                    print(f"ID: {info.get('PatientID', 'N/A')}, Name: {info.get('Name', 'N/A')}, Age: {info.get('Age', 'N/A')}")
            else:
                print(f"\nNo patients found in the specified age range.")

        elif choice == "7":
            records_system.plot_age_distribution()

        elif choice == "8":
            records_system.plot_health_problem_distribution()

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

