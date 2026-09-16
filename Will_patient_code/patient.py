import csv #importing data from Metadata and Protein Data for Module 1 csv


class patient_objects: #created class for pateint objects

    all_patients = [] #creating an empty list to store patient objects

    def __init__(self, age_of_symptom_onset: int, age_of_diagnosis: int, age_of_death: int, sex:str): #created the constructor for patient class which will take inputs for age of symptom onset, age of diagnosis, and age of death as integers, later added sex for question 7
        self.age_of_symptom_onset = age_of_symptom_onset
        self.age_of_diagnosis = age_of_diagnosis
        self.age_of_death = age_of_death
        self.sex = sex

        patient_objects.all_patients.append(self) #appending the patient object to the all_patients list

    def __repr__(self):  
            return f"Patient: ({self.age_of_symptom_onset} | {self.age_of_diagnosis} | {self.age_of_death} | {self.sex})" #returning the string representation of the patient object


    def get_age_of_diagnosis(self):# Returns diagnosis age to sort, moves empty values to end of the list
            if self.age_of_diagnosis == "":
                return 1000# python returns a large number for empty values so that they are moved to the end of the list when sorted
            else:
                return self.age_of_diagnosis

    
             
    @classmethod
    def instantiate_from_csv(cls, filename):

         with open(filename, "r") as f:
              reader = csv.DictReader(f)

              for row in reader: #iterating through the rows of the csv file
                       patient = patient_objects(
                            convert_age(row["Age of onset cognitive symptoms"]),
                            convert_age(row["Age of Dementia diagnosis"]),
                            convert_age(row["Age at Death"]),
                            row["Sex"]
              
                          ) #creating a patient object for each row in the csv file and appending it to the patients list


    @classmethod
    def filter_age_range(cls, diagnosis_min, diagnosis_max, death_min, death_max):
        filtered_patients = []

        for patient in cls.all_patients:
            if patient.age_of_diagnosis != "" and patient.age_of_death != "":
                if (diagnosis_min <= patient.age_of_diagnosis <= diagnosis_max
                        and death_min <= patient.age_of_death <= death_max):
                    filtered_patients.append(patient)

        return filtered_patients


              

def convert_age(value): #keeps missing csv ages as blank strings and converts recorded ages to integers
    if value == "":
        return ""
    else:
        return int(value)




         

