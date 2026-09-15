import csv #so python can read csv files


class Patient: #defining Patient class

    all_patients = [] #list for patient info that gets inputs from for loop
#defining constructor function
    def __init__(self, age_of_diagnosis, age_of_death, sex, dementia, abeta42):
        self.age_of_diagnosis = age_of_diagnosis
        self.age_of_death = age_of_death
        self.sex = sex
        self.dementia = dementia
        self.abeta42 = abeta42

    def __repr__(self): #function that defines how info will be printed in a specfic way
        return f"({self.age_of_diagnosis}, {self.age_of_death}), ({self.sex}, {self.dementia})"

    @classmethod
    def instantiate_from_csv(cls, filename):

        with open(filename, "r") as file: #opens .csv file for reading
            reader = csv.DictReader(file)

            for row in reader: # goes through each row in for loop

                diagnosis = row["Age of Dementia diagnosis"]

                if diagnosis == "": #if pt(patient) not diagnosed then it enters none
                    diagnosis = None
                else:
                    diagnosis = int(diagnosis) #otherwise it converts pt age of diagonsis to integer

                abeta42 = row["ABeta42 pg/ug"]

                if abeta42 == "": #same thing as line 28 but with abeta
                    abeta42 = None 

                else:
                    abeta42 = float(abeta42) #otherwise it converts abeta levels to decimal

                patient = cls(  #creates object with information from each row that we want
                    diagnosis,
                    int(row["Age at Death"]),
                    row["Sex"],
                    row["Cognitive Status"] == "Dementia",
                    abeta42
                )
                cls.all_patients.append(patient)

    def get_age_of_death(self): #getter which finds age of death when we want it
        return self.age_of_death
    @classmethod
    def filter(cls, patients, sex=None, dementia=None):
         filtered_patients = [] # initializes filtered list

         for patient in patients:

            if sex is not None and patient.sex != sex: # skips pt whose sex does not match filter
                continue

            if dementia is not None and patient.dementia != dementia: # skips pt whose dementia status does not match filter
                continue

            filtered_patients.append(patient) # adds matching patient to filtered list

         return filtered_patients