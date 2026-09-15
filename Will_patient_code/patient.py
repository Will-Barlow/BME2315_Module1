import csv #importing data from Metadata and Protein Data for Module 1 csv


class patient_objects: #created class for pateint objects

    def __init__(self, age_of_symptom_onset: int, age_of_diagnosis: int, age_of_death: int): #created the constructor for patient class which will take inputs for age of symptom onset, age of diagnosis, and age of death as integers
        self.age_of_symptom_onset = age_of_symptom_onset
        self.age_of_diagnosis = age_of_diagnosis
        self.age_of_death = age_of_death

    def __repr__(self):  
            return f"Patient: ({self.age_of_symptom_onset} | {self.age_of_diagnosis} | {self.age_of_death})"

patients = [] #creating an empty list to store patient objects

with open("/Users/williambarlow/Library/CloudStorage/OneDrive-UniversityofVirginia/Second Year/First Semester/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv", newline="") as f: #opening the csv file
    reader = csv.DictReader(f) #reading the csv file



    for row in reader: #iterating through the rows of the csv file
         patient = patient_objects(
              int(row["Age of onset cognitive symptoms"]),
              int(row["Age of Dementia diagnosis"]),
              int(row["Age at death"])

            ) #creating a patient object for each row in the csv file and appending it to the patients list

    patients.append(patient)

    for patient in patients:
         print(patient)